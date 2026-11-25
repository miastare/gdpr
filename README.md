# Data protection (UK GDPR): where things are and what is left

This folder is gitignored: it holds the controller's own records. The rules for the code are in
`routes/CLAUDE.md`, section "Data protection".

| File | What it is |
|---|---|
| `record_of_processing.md` | What personal data is used, why, on what legal basis, who receives it, how long it is kept, how each right is met. Includes the legitimate interests assessment and the list of processors |
| `DPIA.md` | The impact assessment: the risks, the measures, what is still to decide. **Unsigned** |
| `Parliament_Pulse_GDPR_justification.md` | The legal case for publishing the research data, including inferred religion and sexuality |
| `background.md` | The position on ChatGPT, OpenAI and international transfers |
| `openai DPA.pdf` | OpenAI's Data Processing Addendum for the API account, signed 24 November 2026. It covers the moderation check and any other API use. It does not cover consumer ChatGPT |
| `accuracy_check/` | The check of how often the name guesses for election candidates and donors are right (DPIA measure L5): the script, the sample of 80 people, the verdict and source for each (`research/`), `RESULTS.md` and `accuracy_check.xlsx`. You checked the sample directly on 24 November 2026. Only the counts are published; the findings about named people stay in that folder |
| `published_notice/<version>.md` | A dated copy of each version of the privacy notice (`python -m helpers.privacy --markdown`) |

## What exists in the app (built 24 November 2026)

- The privacy notice at `/privacy` (text: `helpers/privacy.py`).
- "Your data: ask, correct or delete" at `/privacy/request`, in the More menu: anyone can ask for their data, a
  correction, deletion, object or complain, with or without an account. A logged-in account can download what it
  gave us and close itself there.
- Every request gets a reference (`DR-7`), an emailed acknowledgement and a one-month deadline. You are emailed too.
- The moderation page's Data requests section, and the same from the command line.
- The retention schedule, enforced at every start (`helpers/retention.py`).
- The corrections register for values about people in the data.
- A review key no longer reads anything a moderator removed, nor report counts, reasons or flags (the server
  serves reported and flagged comments first without saying so).

## Answering a request

Requests arrive by email alert and wait in the moderation page's Data requests section, the nearest deadline first.
Or: `PYTHONUTF8=1 .venv/Scripts/python.exe -m helpers.data_requests list`, then `show DR-7`.

1. **Check who is asking**, in proportion to what they want. Logged in: the account is the proof. A correction of a
   public fact with a source needs no proof at all. A copy of an account's data, or a deletion, asked for logged out:
   reply only to the account's own email address. Someone claiming to be a parliamentarian or donor asking to change
   a value: an email from an address that is plainly theirs (parliament.uk, their office, their company) is enough.
   Write what you checked in "How identity was checked".
2. **Do it.**
   - *A copy of their data, account holder:* download the full file from the Data requests section (or
     `export --user U-12 --out file.json`). Read `withheld` and `before_sending` in it; take out anything in our
     notes that names another person. Send it to the account's address.
   - *A copy, someone in the data:* everything we hold is on their page with its sources; tell them so, with the
     address of the page, and say which values are estimates or guesses and how they were made (the page's own
     explanations say it).
   - *A correction or a challenge to a guess:* see the next section.
   - *Deletion of an account:* "Close an account at its owner's request" in the same section. It refuses if the
     account is suspended or has reports waiting: deal with those first.
   - *Removal of someone from the data, or an objection:* this is the one that needs judgement. The position in the
     justification paper is that the record stays; what can always be done is to correct what is wrong and to set a
     disputed estimate to "unknown" for that person. Decide, and give the reason in the reply.
   - *A complaint:* look into it, answer it, and note anything to change.
3. **Close it** with an outcome and the reply. The reply is emailed to them and kept.
4. If it cannot be finished in a month, **extend** it once (two more months) with a reason, before the month is up.

A reply that refuses something should say why, and that they can complain to us and to the ICO (the email adds the
ICO line itself).

## Correcting a value about someone in the data

The register is `ingestion_update/data/manual/data_subject_corrections.json`. It is applied every time the app loads
its data, so a correction shows from the next restart and survives every rebuild. Add an entry:

```json
{"id": "K-1", "request": "DR-7", "date": "2026-12-02", "kind": "member", "key": 1234,
 "set": {"religion": "Christian", "sexuality": null},
 "reason": "the person told us the estimate was wrong"}
```

`kind` is `member` (key: the bespoke id), `candidate` (key: the last part of the address of their election
results page) or `donor` (key: the donor key shown in the builders' tables, the name in lower case without
titles; the file's own `_about` gives the other forms). `null` makes the value unknown. A donor key is a name,
so two people of one name share it: for a guess from a name, `null` is the answer that is right for both. Give
sexuality as the data stores it (`heterosexual` or `homosexual`; the site shows "Heterosexual" and "Likely not
heterosexual"). Never reuse an `id`: the site quotes it to readers where the value's source is given.

Then check the file (`python -m helpers.corrections check`), restart Flask, and look for the `CORRECTIONS:` lines
in the start-up log: one per correction (it names the fields, never the values), and a WARNING for any that
matched nobody.

This layer changes what the site shows. It does not change the pipeline's own files, the tables the ideology model
was fitted on, or the paper's replication archive (frozen on purpose: it reproduces the paper). For a parliamentarian, also enter the correction at source before
the next ingestion run (`ingestion_update/manual_ingestion_info.py`, `FURTHER_MANUAL_INPUT`), so that everything
derived from the members table agrees.

Whether to change a value is your decision each time. "Nothing is removed" (24 November 2026) is about the columns as
a whole; setting one person's disputed estimate to unknown at their request is a correction of an inaccurate value,
and it is what the justification paper (section 8) and the privacy notice promise.

## Still to do

**Before the site opens**

- [ ] Read the privacy notice at `/privacy` as a stranger would, and correct anything that is not true of the site.
- [ ] Read `DPIA.md`, fill in
      the line about your hand check of the "Likely not heterosexual" cases, and sign it. No consultation with the
      ICO is needed: no risk is rated high.
- [x] OpenAI: Data Processing Addendum for the API account signed 24 November 2026 (`openai DPA.pdf`). Optional:
      ask for zero data retention.
- [ ] Save a dated copy of Resend's data processing terms here.
- [ ] Name the host in `helpers/privacy.py` (`HOSTING`) and in `record_of_processing.md` section 4, and take
      Cloudflare out of both if it is no longer used. New version and date for the notice.
- [ ] A contact mailbox for data protection, if you want one published: set `PRIVACY_CONTACT_EMAIL`. Without it the
      notice gives the form only.
- [x] Labelling fixes L1, L2 and L4 (24 November 2026; check them in the browser). The hand check of members shown
      as "Likely not heterosexual" is done (yours).
- [x] The accuracy check: the sample checked directly by you on 24 November 2026; the figures are on the name-guess columns'
      explainers.
- [x] Sexuality had no "unknown" answer (25 November 2026): the AI model could answer only heterosexual or
      homosexual and was told to assume heterosexual when it could not tell. The site, the privacy notice, the DPIA
      (section 1 and risk 11) and the record of processing now say so, and nothing words it as if the model could
      have left it open.
- [ ] Before the first correction to a parliamentarian's religion or sexuality is recorded: the member page would
      still label the corrected value "(AI guessed)" and show a confidence badge, because the corrections layer
      leaves no mark on the row that the page can read (a corrected candidate or donor value is marked, through its
      basis). Nothing is wrong today: the register is empty. Fix: have the layer mark the row, and the page read it.
- [ ] A half-page policy note for the child-sexual-abuse sign-up bar (`record_of_processing.md` section 6).
- [ ] Agree with the academic collaborator who is controller of what.
- [ ] Security at deployment: headers and a content security policy, encrypted database backups, a note of what to
      do on a breach (72 hours to tell the ICO where people are at risk).
- [ ] The ICO fee self-assessment, on opening day.
- [ ] Send one request through `/privacy/request` yourself and answer it, to see the emails arrive.

**Later**

- [ ] Analytics: the site's own counts, with a sentence in the notice and a way to object (no banner needed).
- [x] L3 in the DPIA: the profile pages, Interesting Correlates and the homepage gallery texts are labelled
      (24 November 2026). On 25 November 2026 the interest cards' "we are about N% confident" wording was replaced
      ("An AI model guessed this, and rated its own confidence at N%. That is not a measured accuracy."), the four
      gallery charts' stored titles were changed to say "AI-guessed" / "an AI model guessed as", the profile tiles'
      titles gained a red "AI guessed" chip that opens the column's explanation, and the homepage gallery gained a
      standing warning box. Still owed: the gallery's pictures of those four charts show the old titles (retake
      them), and the charts' descriptions still state the guesses as fact (yours to reword in the share dialog).
- [ ] Hash internet addresses with a secret key (DPIA risk 6).
- [ ] Keep other people's replies when an account is closed.

**Routine**

- Look at the Data requests section when you do the Monday and Thursday moderation review.
- Yearly, with the Online Safety review: re-read the record of processing and the DPIA against what the app does.
