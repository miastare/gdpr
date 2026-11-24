"""How often are the name guesses about election candidates and donors right? (DPIA measure L5)

The site guesses a gender and a religious background from the NAME of an
election candidate who never sat in Parliament and of an individual donor
(`interests_ingestion_update/donor_attributes.py`). This compares those
guesses with what public sources say about the person, for a sample.

    sample    draw the sample (fixed seed) and write research/batch_<n>_input.json
    analyse   read research/batch_<n>_output.json (one verdict per person, each
              with its source) and write RESULTS.md and accuracy_check.xlsx

Between the two, each sampled person is checked against public sources; the
rules followed are in RESEARCH_RULES below.
`analyse` also runs two checks that need no research: the same name rules on
candidates and donors who ARE parliamentarians, whose gender is on record.

Run with the repo venv from the repo root:
    PYTHONUTF8=1 .venv/Scripts/python.exe GDPR/accuracy_check/check_estimates.py sample
Nothing here changes any data. The sample is checked directly by the
controller, and nothing is published from it before that.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FULL_FLAT = ROOT / "ingestion_update" / "data" / "output" / "full_flat.parquet"
ELECTIONS = ROOT / "ingestion_update" / "data" / "votes_output" / "election_with_bespoke_id.parquet"
EC_PATH = (ROOT / "interests_ingestion_update" / "electoral_commision" / "electoral_commission_output"
           / "electoral_commission_enriched.parquet")
RESEARCH = HERE / "research"
SAMPLE = HERE / "sample.json"
OUT_XLSX = HERE / "accuracy_check.xlsx"
OUT_MD = HERE / "RESULTS.md"

SEED = 20261124
PER_CLASS = 8           # people sampled per guessed religion, per group
BATCHES = 4
CANDIDATES_SINCE = "2010-01-01"   # candidates whose latest election is on or after this date
RELIGIONS = ["Christian", "Hindu", "Jewish", "Muslim", "Sikh"]

RESEARCH_RULES = """\
For each person: find out, from public sources, whether their religion and gender can be stated with confidence.
- The default answer is "not_known". Most of these people are private individuals about whom little is published.
- "likely_correct" / "likely_wrong" for religion need a source that says it: the person's own statement, a reliable
  biography, profile, obituary or news report, or a role that settles it (an imam, a trustee of a named synagogue,
  a church minister). The verdict compares the source with OUR GUESS.
- Never infer religion from the name, from ethnicity or country of origin, from appearance, or from the party or
  cause supported. Those are what the guess already did.
- First be sure the person found is the same person (the party, seat, years or the recipient of the donation should
  fit). If that is not clear, the answer is "not_known" with identity "not_found" or "uncertain".
- Gender: "correct" / "wrong" when a source refers to the person as he or she, or shows it plainly; else "not_known".
"""


# ---------------------------------------------------------------------------
# sample
# ---------------------------------------------------------------------------
def donor_population() -> pd.DataFrame:
    ec = pd.read_parquet(EC_PATH, columns=[
        "DonorName", "DonorStatus", "ec_donor_key", "donor_bespoke_id", "donor_gender_guess", "donor_religion_guess",
        "donor_religion_guess_basis", "RegulatedEntityName", "ValueGBP", "accepted_year", "donor_description", "donor_url"])
    ec = ec[ec["donor_religion_guess"].notna() & ec["donor_bespoke_id"].isna()]
    people = []
    for key, group in ec.groupby("ec_donor_key"):
        first = group.iloc[0]
        years = group["accepted_year"].dropna()
        people.append({
            "id": f"donor:{key}", "group": "donor", "name": Counter(group["DonorName"].astype(str)).most_common(1)[0][0],
            "religion_guess": first["donor_religion_guess"], "religion_basis": first["donor_religion_guess_basis"],
            "gender_guess": first["donor_gender_guess"],
            "context": {
                "what": "individual donor in the Electoral Commission's register of political donations",
                "gave_to": [k for k, _ in Counter(group["RegulatedEntityName"].astype(str)).most_common(3)],
                "years": f"{int(years.min())} to {int(years.max())}" if len(years) else None,
                "total_gbp": round(float(group["ValueGBP"].fillna(0).sum())),
                "our_note_on_the_donor": first["donor_description"] if isinstance(first["donor_description"], str) else None,
                "link_we_hold": first["donor_url"] if isinstance(first["donor_url"], str) else None,
            },
        })
    return pd.DataFrame(people)


def candidate_population() -> pd.DataFrame:
    el = pd.read_parquet(ELECTIONS)
    el = el[el["bespoke_id"].isna() & el["religion_guess"].notna()]
    basis = el["religion_guess_basis"].astype(str).str.split(":").str[0]
    el = el[basis.isin(["given", "surname"])]          # the name rules only; not the party-name rule
    people = []
    for key, group in el.groupby("candidate_key"):
        dates = pd.to_datetime(group["date"])
        if dates.max() < pd.Timestamp(CANDIDATES_SINCE):
            continue
        first = group.iloc[0]
        people.append({
            "id": f"candidate:{key}", "group": "candidate",
            "name": first["candidate_display_name"] if isinstance(first["candidate_display_name"], str) else str(first["candidate name"]),
            "religion_guess": first["religion_guess"], "religion_basis": first["religion_guess_basis"],
            "gender_guess": first["gender_guess"],
            "context": {
                "what": "candidate for the House of Commons who was never elected",
                "name_as_recorded": sorted(set(group["candidate name"].astype(str)))[:3],
                "parties": sorted(set(group["candidate party"].dropna().astype(str)))[:4],
                "seats": sorted(set(group["constituency_name"].dropna().astype(str)))[:4],
                "elections": sorted({str(d.date()) for d in dates}),
            },
        })
    return pd.DataFrame(people)


def draw_sample() -> None:
    RESEARCH.mkdir(exist_ok=True)
    chosen = []
    sizes = {}
    for name, population in (("donor", donor_population()), ("candidate", candidate_population())):
        for religion in RELIGIONS:
            pool = population[population["religion_guess"] == religion]
            sizes[f"{name}|{religion}"] = len(pool)
            take = pool.sample(n=min(PER_CLASS, len(pool)), random_state=SEED)
            chosen.extend(take.to_dict("records"))
        print(name, {r: sizes[f"{name}|{r}"] for r in RELIGIONS})
    SAMPLE.write_text(json.dumps({"seed": SEED, "per_class": PER_CLASS, "candidates_since": CANDIDATES_SINCE,
                                  "population": sizes, "people": chosen}, ensure_ascii=False, indent=1), encoding="utf-8")
    shuffled = pd.DataFrame(chosen).sample(frac=1, random_state=SEED).to_dict("records")
    for b in range(BATCHES):
        part = shuffled[b::BATCHES]
        (RESEARCH / f"batch_{b + 1}_input.json").write_text(json.dumps(part, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"sampled {len(chosen)} people into {BATCHES} batches in {RESEARCH}")


# ---------------------------------------------------------------------------
# the checks that need no research: the same rules where the answer is on record
# ---------------------------------------------------------------------------
def members_in_the_election_record() -> pd.DataFrame:
    """The name rules run on every parliamentarian's names in the election record."""
    sys.path.insert(0, str(ROOT / "ingestion_update"))
    sys.path.insert(0, str(ROOT))
    try:
        from ingestion_update.election_candidates import consolidate_gender, consolidate_religion
    except Exception:  # the module's own imports are bare
        from election_candidates import consolidate_gender, consolidate_religion
    el = pd.read_parquet(ELECTIONS, columns=["candidate name", "bespoke_id"])
    el = el[el["bespoke_id"].notna() & el["candidate name"].notna()]
    members = pd.read_parquet(FULL_FLAT, columns=["bespoke_id", "itemLabel", "gender", "religion"]).set_index("bespoke_id")
    out = []
    for bespoke_id, group in el.groupby("bespoke_id"):
        key = int(bespoke_id)
        if key not in members.index:
            continue
        spellings = dict(Counter(group["candidate name"].astype(str)))
        gender, gender_basis = consolidate_gender(spellings)
        religion, religion_basis = consolidate_religion(spellings)
        out.append({"bespoke_id": key, "name": members.at[key, "itemLabel"], "spellings": "; ".join(sorted(spellings)),
                    "gender_name_guess": gender, "gender_name_basis": (gender_basis or "").split(":")[0] or None,
                    "gender_on_record": members.at[key, "gender"], "religion_name_guess": religion,
                    "religion_name_basis": religion_basis, "member_religion_ai_estimate": members.at[key, "religion"]})
    return pd.DataFrame(out)


def donors_who_are_members() -> pd.DataFrame:
    sys.path.insert(0, str(ROOT / "interests_ingestion_update"))
    from donor_attributes import guess_gender_evidence, guess_religion

    ec = pd.read_parquet(EC_PATH, columns=["DonorName", "ec_donor_key", "donor_bespoke_id"])
    ec = ec[ec["donor_bespoke_id"].notna()].drop_duplicates("ec_donor_key").copy()
    ec["bespoke_id"] = ec["donor_bespoke_id"].astype(float).astype(int)
    # the name rule run afresh on the recorded name (the stored column holds the member's own value for these donors)
    ec["donor_gender_guess"] = ec["DonorName"].map(lambda n: guess_gender_evidence(n)[0])
    religion = ec["DonorName"].map(lambda n: guess_religion(n, organisation=False))
    ec["donor_religion_guess"] = religion.map(lambda r: r[0])
    ec["donor_religion_guess_basis"] = religion.map(lambda r: r[1])
    members = pd.read_parquet(FULL_FLAT, columns=["bespoke_id", "itemLabel", "gender", "religion"])
    out = ec.merge(members, on="bespoke_id", how="inner").rename(columns={
        "itemLabel": "name", "gender": "gender_on_record", "religion": "member_religion_ai_estimate",
        "DonorName": "donor_name_as_recorded"})
    return out[["name", "donor_name_as_recorded", "donor_gender_guess", "gender_on_record", "donor_religion_guess",
                "donor_religion_guess_basis", "member_religion_ai_estimate", "bespoke_id"]]


# ---------------------------------------------------------------------------
# analyse
# ---------------------------------------------------------------------------
def pct(n: int, d: int) -> str:
    return "n/a" if not d else f"{100 * n / d:.0f}%"


def wilson(n: int, d: int) -> str:
    """95% interval for a share, as text."""
    if not d:
        return ""
    z = 1.96
    p = n / d
    centre = (p + z * z / (2 * d)) / (1 + z * z / d)
    half = z * ((p * (1 - p) / d + z * z / (4 * d * d)) ** 0.5) / (1 + z * z / d)
    return f"{100 * max(0, centre - half):.0f}% to {100 * min(1, centre + half):.0f}%"


def analyse() -> None:
    sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
    people = {p["id"]: p for p in sample["people"]}
    verdicts = {}
    for path in sorted(RESEARCH.glob("batch_*_output.json")):
        for row in json.loads(path.read_text(encoding="utf-8")):
            verdicts[row["id"]] = row
    review_path = RESEARCH / "controller_review.json"
    review = json.loads(review_path.read_text(encoding="utf-8")) if review_path.exists() else {}
    background = review.get("name_background", {})
    rows = []
    for pid, person in people.items():
        v = verdicts.get(pid, {})
        rows.append({
            "group": person["group"], "name": person["name"],
            "our_religion_guess": person["religion_guess"], "read_from": person["religion_basis"],
            "religion_verdict": v.get("religion_verdict", "NOT CHECKED"),
            "name_matches_family_background": background.get(pid),
            "what_sources_say_religion": v.get("religion_public"), "religion_evidence": v.get("religion_evidence"),
            "religion_source": v.get("religion_source_url"),
            "our_gender_guess": person["gender_guess"],
            "gender_verdict": v.get("gender_verdict", "NOT CHECKED") if person["gender_guess"] else "no guess made",
            "what_sources_say_gender": v.get("gender_public"), "gender_source": v.get("gender_source_url"),
            "same_person_found": v.get("identity"), "notes": v.get("notes"),
            "context": json.dumps(person["context"], ensure_ascii=False), "id": pid,
        })
    table = pd.DataFrame(rows)
    lines: list[str] = []

    def say(text: str = "") -> None:
        lines.append(text)
        print(text)

    say("# Accuracy check of the name guesses for election candidates and donors (DPIA measure L5)")
    say()
    if review:
        say(f"Run on {pd.Timestamp.now():%d %B %Y}. **The sample was checked directly by {review['reviewed_by']} on "
            f"{pd.Timestamp(review['reviewed_on']):%d %B %Y}.** {review['statement']}")
    else:
        say(f"Run on {pd.Timestamp.now():%d %B %Y}. NOT PUBLISHED: these figures go on the site only once the controller "
            "has checked the sample directly.")
    say()
    say(f"Sample: {len(table)} people with a religious-background guess, {PER_CLASS} drawn at random (seed {SEED}) for each "
        f"guessed value in each group. Donors: individuals in the Electoral Commission data who are not parliamentarians. "
        f"Candidates: people who never sat, whose latest election was in {CANDIDATES_SINCE[:4]} or later, guessed from the "
        "name (the few guessed from a party's name are left out). Each was looked up in public sources under these rules:")
    say()
    for rule in RESEARCH_RULES.strip().splitlines():
        say(rule if rule.startswith("-") or rule.startswith(" ") else rule)
    done = table[table["religion_verdict"] != "NOT CHECKED"]
    say()
    say(f"Checked: {len(done)} of {len(table)}.")

    def block(frame: pd.DataFrame, heading: str) -> None:
        say()
        say(f"### {heading}")
        say()
        say("| Our guess | People | Not known | Likely correct | Likely wrong | Of those that could be checked, correct |")
        say("|---|---|---|---|---|---|")
        for value, group in list(frame.groupby("our_religion_guess")) + [("all", frame)]:
            c = Counter(group["religion_verdict"])
            ok, bad = c.get("likely_correct", 0), c.get("likely_wrong", 0)
            say(f"| {value} | {len(group)} | {c.get('not_known', 0)} | {ok} | {bad} | "
                f"{f'{ok} of {ok + bad}' if ok + bad else 'none could be checked'} |")

    say()
    say("## Religious background guessed from the name")
    block(done[done["group"] == "donor"], "Donors")
    block(done[done["group"] == "candidate"], "Election candidates")
    block(done, "Both together")
    c = Counter(done["religion_verdict"])
    ok, bad, unknown = c.get("likely_correct", 0), c.get("likely_wrong", 0), c.get("not_known", 0)
    say()
    say(f"In words: of {len(done)} people, the person's religion could not be established from public sources for "
        f"{unknown} ({pct(unknown, len(done))}); the guess was likely correct for {ok} ({pct(ok, len(done))}) and likely wrong for "
        f"{bad} ({pct(bad, len(done))}). Among the {ok + bad} that could be checked, {pct(ok, ok + bad)} were correct "
        f"(95% interval {wilson(ok, ok + bad)}). The sample takes the same number from each guessed value, so the "
        "\"all\" rows are not weighted to the mix of values in the data; the population sizes are in `sample.json`.")
    wrong = done[done["religion_verdict"] == "likely_wrong"]
    kept = wrong[wrong["name_matches_family_background"].notna()]
    if len(kept):
        say()
        say(f"The column is named for what it is, the guessed religious background of the NAME. Read that way, {len(kept)} of "
            f"the {len(wrong)} \"likely wrong\" cases are right about the name and the family, and wrong only about the "
            "religion the person states for themselves:")
        say()
        for _, row in kept.iterrows():
            say(f"- {row['name'].strip()}: {row['name_matches_family_background']}")
        say()
        say(f"So, of the {ok + bad} people whose religion could be established: the guess matched the person's own stated "
            f"religion for {ok}, and for the other {bad} it matched the father's family background but not the religion "
            "the person states.")

    say()
    say("## Gender guessed from the name (the same sampled people)")
    say()
    g = done[done["our_gender_guess"].notna()]
    gc = Counter(g["gender_verdict"])
    say(f"A gender guess exists for {len(g)} of the {len(done)}. Sources confirm it for {gc.get('correct', 0)}, contradict it for "
        f"{gc.get('wrong', 0)}, and say nothing clear for {gc.get('not_known', 0)}.")

    # ---- no research needed -------------------------------------------------
    members = members_in_the_election_record()
    say()
    say("## The same rules where the answer is on record (no research needed)")
    say()
    say(f"The name rules were run on the election-record names of {len(members):,} parliamentarians, whose gender is recorded.")
    say()
    say("| Gender read from | Guesses | Right | Share right | 95% interval |")
    say("|---|---|---|---|---|")
    mg = members[members["gender_name_guess"].notna() & members["gender_on_record"].isin(["Male", "Female"])]
    for basis, group in list(mg.groupby("gender_name_basis")) + [("all", mg)]:
        right = int((group["gender_name_guess"] == group["gender_on_record"]).sum())
        say(f"| {basis} | {len(group):,} | {right:,} | {100 * right / len(group):.1f}% | {wilson(right, len(group))} |")
    none = int(members["gender_name_guess"].isna().sum())
    say()
    say(f"No gender guess could be made for {none:,} of {len(members):,} ({pct(none, len(members))}).")
    donors = donors_who_are_members()
    dg = donors[donors["donor_gender_guess"].notna() & donors["gender_on_record"].isin(["Male", "Female"])]
    right = int((dg["donor_gender_guess"] == dg["gender_on_record"]).sum())
    say()
    say(f"Donors who are themselves parliamentarians ({len(donors):,}), the name rule run on the name as recorded: a gender guess for {len(dg):,}, right for {right:,} "
        f"({100 * right / max(1, len(dg)):.1f}%, 95% interval {wilson(right, len(dg))}).")
    say()
    say("Religion cannot be checked this way: a parliamentarian's religion on the site is itself an AI estimate, not a "
        "record. For what it is worth, where the name rule fires on a parliamentarian the two agree as follows.")
    say()
    say("| Name read as | Parliamentarians | AI estimate from the biography is the same | Share |")
    say("|---|---|---|---|")
    mr = members[members["religion_name_guess"].notna()]
    for value, group in mr.groupby("religion_name_guess"):
        same = int((group["member_religion_ai_estimate"] == value).sum())
        say(f"| {value} | {len(group):,} | {same:,} | {pct(same, len(group))} |")

    say()
    say("## What this does and does not show")
    say()
    say("- \"Not known\" is not an error. It means nothing public settles the person's religion, so the guess stands as a "
        "statement about the name and nothing more.")
    say("- The sample is small, so the shares are rough; the intervals say how rough.")
    say("- The findings about named people stay in this folder. Only the counts are for publication.")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as writer:
        pd.DataFrame({"Read RESULTS.md beside this file for the figures and the method.": [
            "Sheet 'sample': every sampled person, our guess, the verdict, what the source says and the link. Sort by religion_verdict; the 'likely' rows are the ones to open.",
            "Sheet 'members gender wrong': parliamentarians whose gender the name rule got wrong (answer on record).",
            "Sheet 'members religion rule': each religion guess the name rule makes on a parliamentarian, beside the AI estimate.",
            "Sheet 'donors who are members': donors linked to a parliamentarian, the stored guesses and the member's record.",
        ]}).to_excel(writer, sheet_name="read me", index=False)
        table.sort_values(["group", "religion_verdict", "our_religion_guess", "name"]).to_excel(writer, sheet_name="sample", index=False)
        mg[mg["gender_name_guess"] != mg["gender_on_record"]].to_excel(writer, sheet_name="members gender wrong", index=False)
        mr.sort_values(["religion_name_guess", "name"]).to_excel(writer, sheet_name="members religion rule", index=False)
        donors.sort_values(["donor_religion_guess", "name"]).to_excel(writer, sheet_name="donors who are members", index=False)
    print(f"\nwrote {OUT_XLSX}\nwrote {OUT_MD}")


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command == "sample":
        draw_sample()
    elif command == "analyse":
        analyse()
    else:
        print(__doc__)
