# Data protection (UK GDPR): Parliament Pulse

The controller's own records: what personal data the site uses and on what basis, the risks, the contracts with
the companies that handle it, the evidence behind the published accuracy figures, and what is left to do. This
folder is gitignored by hansard and is its own git repository. The rules for the code are in hansard's
`routes/CLAUDE.md`, section "Data protection".

Paths in these files are written from this folder.

## What is where

| Where | What it is |
|---|---|
| `answering_requests.md` | How to answer a request from someone about their data, and how to correct a value about a person in the data |
| **`records/`** | **The formal records** |
| `records/record_of_processing.md` | What personal data is used, why, on what legal basis, who receives it, how long it is kept, how each right is met, what is not required. Includes the legitimate interests assessment and the list of processors |
| `records/appropriate_policy_document.md` | The policy document the law requires for criminal offence data: reports of suspected illegal content, decisions on them, the archive of removed content and sign-up bars. Adopted 26 November 2026 |
| `records/DPIA.md` | The impact assessment: the risks, the measures, the sign-off. **Signed 25 November 2026**; next review before opening, then by 25 November 2027 |
| **`positions/`** | **Legal reasoning the records rely on** |
| `positions/research_data_justification.md` | The case for publishing the research data, including AI-guessed religion and sexuality (legitimate interests, the research condition, the Schedule 2 paragraph 26 exemption); section 10A records what was adopted and checked since |
| `positions/ai_moderation_and_transfers.md` | The position on consumer ChatGPT, OpenAI and international transfers for the AI-assisted review of comments |
| **`processors/`** | **Contracts and evidence for each company that handles personal data for the site** |
| `processors/openai/openai_dpa_signed_2026-11-24.pdf` | OpenAI's Data Processing Addendum for the API account (the moderation check and any other API use; not consumer ChatGPT) |
| `processors/resend/resend_record.md` | Resend, the email service: what the site sends through it, the transfer, retention, sub-processors, what is left to do. Start here for Resend |
| `processors/resend/resend_dpa_2025-12-31.md` | Resend's Data Processing Addendum (version of 31 December 2025), binding from the account's sign-up |
| `processors/resend/dpf_listing_2026-11-25.png` | Resend's entry on the Data Privacy Framework list (participant 8907), saved 25 November 2026: EU-US and UK Extension both active, next certification due 3 March 2027 |
| **`accuracy_check/`** | **Evidence for the accuracy of the guesses** (only the counts are published; the findings about named people stay here) |
| `accuracy_check/RESULTS.md`, `accuracy_check.xlsx` | The check of the name guesses for 80 election candidates and donors (DPIA measure L5), checked directly by you on 24 November 2026; the figures are on the name-guess columns' explainers |
| `accuracy_check/research/`, `sample.json`, `check_estimates.py` | That check's sample, the verdict and source for each person, your review, and the script |
| `accuracy_check/religion_check_reviewed.csv` | A random sample of 100 living parliamentarians' AI-guessed religion, each checked by you against open-source research on 25 November 2026: 97 agreed |
| **`published_notice/`** | **A dated copy of each version of the privacy notice** (`python -m helpers.privacy --markdown > GDPR/published_notice/<version>.md`, run from hansard) |

## Still to do

**Before the site opens**

- [ ] Read the privacy notice at `/privacy` as a stranger would, and correct anything that is not true of the site.
      The version to read is 2026-11-25b (`published_notice/2026-11-25b.md`); `CHANGES` in `helpers/privacy.py`
      lists what each version changed. The running server shows it only after a restart.
- [ ] Name the host in `helpers/privacy.py` (`HOSTING`) and in `records/record_of_processing.md` section 4, and take
      Cloudflare out of both if it is no longer used. New version and date for the notice.
- [ ] Security at deployment: headers and a content security policy, encrypted database backups (without the
      `ADDRESS_HASH_KEY` key), a note of what to do on a breach (72 hours to tell the ICO where people are at risk).
      DPIA risk 8.
- [ ] Look in the browser at the labelling fixes L1 to L4 (DPIA section 4).
- [ ] The homepage gallery: retake the pictures of the four AI-guess charts (they show the old titles), and reword
      their descriptions in the share dialog, which still state the guesses as fact.
- [ ] Optional: a contact mailbox for data protection. Set `PRIVACY_CONTACT_EMAIL`; without it the notice gives the
      form only.
- [ ] On opening day: the ICO fee self-assessment.

**Later**

- [ ] Analytics: the site's own counts, with a sentence in the notice and a way to object (no banner needed).
- [ ] The accuracy log (DPIA risk 4).
- [ ] Keep other people's replies when an account is closed.
- [ ] Optional: ask OpenAI for zero data retention; download Resend's executed DPA from its dashboard (Settings,
      Documents) and keep it in `processors/resend/`.

**Routine**

- Restart the server at least every 14 days: the deletions run only at start-up, and the notice promises nothing
  is kept more than 14 days beyond its period (`helpers/retention.RESTART_DAYS`).
- The Data requests section, at the Monday and Thursday moderation review (`answering_requests.md`).
- A new version of the privacy notice: save its copy in `published_notice/`.
- Resend's notices of new sub-processors, when they arrive: look again if one would receive email content.
- After 3 March 2027: Resend's Data Privacy Framework entry (https://www.dataprivacyframework.gov/participant/8907)
  is still active, UK Extension included; save a new screenshot in `processors/resend/`.
- Yearly, with the Online Safety review, and by 25 November 2027 at the latest: re-read the record of processing,
  the DPIA and the appropriate policy document against what the app does.

## Done

| Date | What |
|---|---|
| 24 November 2026 | The privacy notice, the data requests page and routine, the retention schedule and the corrections register built (`answering_requests.md`) |
| 24 November 2026 | OpenAI's Data Processing Addendum for the API account signed |
| 24 November 2026 | A review key no longer reads removed comments, report counts, reasons or flags |
| 24 November 2026 | Labelling fixes L1 to L4; the name-guess accuracy check (L5), checked directly by you, figures on the explainers |
| 24 November 2026 | Every member shown as "Likely not heterosexual" checked by hand (285): all reasonable |
| 25 November 2026 | Sexuality recorded everywhere as having had no "unknown" answer (the model could answer only heterosexual or homosexual) |
| 25 November 2026 | Interest cards, gallery chart titles, profile tiles and the homepage gallery labelled as AI guesses (L3) |
| 25 November 2026 | Religion: a random sample of 100 living parliamentarians checked, 97 agreed (`accuracy_check/religion_check_reviewed.csv`) |
| 25 November 2026 | Internet addresses hashed with a secret key (HMAC-SHA256; `ADDRESS_HASH_KEY`, else `secrets/address_hash.key`, gitignored). Keep the key out of any database backup; losing it only means existing bars stop matching. DPIA risk 6 |
| 25 November 2026 | A corrected religion or sexuality shown as "corrected on request", with certainty 100% |
| 25 November 2026 | Controller of everything: Samuel Kinshuck; the academic collaborator is a recipient, not a controller |
| 25 November 2026 | Resend: DPA saved, record written, open and click tracking checked off, Data Privacy Framework entry saved; the notice names the UK-US data bridge, 30-day retention and the spam-checking sub-processor |
| 25 November 2026 | Test of the request emails (DR-43): acknowledgement, moderator's alert and answer all arrived |
| 25 November 2026 | Privacy notice 2026-11-25b: the full paragraph 26 test, "Limits" in section 7, the keyed hash, Resend |
| 25 November 2026 | DPIA signed, accepting the re-rated risks. No consultation with the ICO needed: no risk is rated high |
| 26 November 2026 | Appropriate policy document for criminal offence data adopted (`records/appropriate_policy_document.md`): sign-up bars (child sexual abuse, terrorism, removals), reports of suspected illegal content, decisions, the archive. The record of processing points to it |
