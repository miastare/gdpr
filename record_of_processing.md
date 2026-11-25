# Parliament Pulse: record of processing, legal bases and processors

**Controller:** Samuel Kinshuck (an individual, United Kingdom). **Written:** 24 November 2026. **Review:** before the
site opens, then yearly with the Online Safety review, and whenever a row below changes.

This one file is the record of processing (UK GDPR Article 30), the note of the legal basis for each activity, the
legitimate interests assessment, the retention schedule and the list of processors. The legal reasoning for the
research data is in `Parliament_Pulse_GDPR_justification.md`; the position on ChatGPT and international transfers is
in `background.md`; the risks are in `DPIA.md`. The published version of all this is the privacy notice
(`helpers/privacy.py`, at `/privacy`).

Rule: when the app starts doing something new with personal data, add or change a row here and the matching
sentence in `helpers/privacy.py` first.

## 1. What is processed, why, and on what basis

### A. People who use the site

| Activity | Personal data | Basis (Article 6) | Special category (Article 9) | Who receives it |
|---|---|---|---|---|
| Accounts | Email address, password hash, screen name and its history, sign-up and last log-in times, Terms version accepted, email choices | Contract (6(1)(b)) | None | Resend (emails) |
| Sign-up age question | A count per month of first answers; nothing linked to a person | Not personal data once counted. The browser marks: strictly necessary storage | None | Nobody |
| Publishing what users post | Comments, shared charts, scores, new columns, under a screen name | Contract (6(1)(b)) | Political opinions in comments: manifestly made public by the person (9(2)(e)) | The public |
| Likes and dislikes, public per account | Which account liked or disliked what, including politicians, candidates and donors | Contract (6(1)(b)) | Political opinions: manifestly made public (9(2)(e)). This holds only because the site says plainly that they are public: the one-time notice at the first click, Terms rule 1, the privacy notice | The public |
| Blocks | Blocker, blocked, when | Legitimate interests (6(1)(f)): letting a user avoid another | None | Nobody (the blocker sees their own) |
| Engagement emails | Which milestones were emailed | Legitimate interests (6(1)(f)): telling a user that someone responded to what they posted. Not marketing. Asked once, and a switch in the account menu turns them off | None | Resend |
| Usage log | Which saved score, column or chart was opened, when, by which account or internet address | Legitimate interests (6(1)(f)): running the site, limiting heavy use | None | Nobody |
| Text filter and word list | The comment; which rules matched; the decision that closed the flag | Legitimate interests + legal obligation (6(1)(c), Online Safety Act 2023) | Political opinions: 9(2)(e) (public comments) | Nobody |
| OpenAI's moderation check | The comment and its context (no screen name, account or email); flags, categories, scores | As above | 9(2)(e) | OpenAI (API; processor) |
| Standing | Points worked out from how an account's comments fared; not stored | Legitimate interests. It is close to profiling: its only effect is whether an OpenAI flag holds a comment back in popularity orders | None | Nobody |
| AI-assisted review (batches and review keys) | Public comments and their context with screen names and account IDs (no report counts, reasons or flags since 24 November 2026: the server only serves reported and flagged comments first); the assessments returned; the log of what each key was sent | Legitimate interests + legal obligation | 9(2)(e) | OpenAI (ChatGPT; see section 4 and `background.md`) |
| Reports, appeals, complaints | What was sent; the account or a contact email; the client address (90 days); outcome; a "vexatious" mark | Legal obligation (Online Safety Act) + legitimate interests | Whatever the text contains: 9(2)(g) is not relied on; processed only to deal with the report | Nobody. The person reported is never told who reported |
| Decision log | What was decided about which item or account, why, with a copy of the item | Legal obligation + legitimate interests | As the content | Nobody |
| Archive of deleted content | A copy of what users delete, and of closed or removed accounts, for 90 days | Legitimate interests + legal obligation (reporting child sexual abuse material to the NCA) | As the content | The NCA or police where the law requires |
| Sign-up bars | Hashed internet addresses per account (90 days); on removal or serious suspension, hashed email (no end date) and hashed addresses (180 days) | Child sexual abuse and terrorism: recognised legitimate interest, crime prevention (6(1)(ea), Annex 1). Otherwise legitimate interests (6(1)(f)) | Criminal-offence data by implication for a CSEA bar: DPA 2018 Schedule 1 paragraph 10 (preventing unlawful acts) | Nobody |
| Data protection requests | The request, a contact email, the account, the client address (90 days), how identity was checked, our answer | Legal obligation (6(1)(c)) | Whatever the person tells us | Nobody |

### B. People who appear in the data

| Activity | Personal data | Basis (Article 6) | Special category (Article 9) | Source |
|---|---|---|---|---|
| Parliamentarians' careers, votes, posts, interests | Names, seats, parties, votes, offices, declared interests, portraits | Legitimate interests (6(1)(f)): research, journalism, democratic transparency | Party and votes reveal political opinions: manifestly made public (9(2)(e)) and research (9(2)(j) + DPA Schedule 1 paragraph 4) | Parliament's data services, Hansard, the Register of Interests, Wikidata |
| Parliamentarians' biography | Dates and places of birth, education, occupation, family links to other parliamentarians, gender | Legitimate interests | None, except as below | Wikidata, Wikipedia, Parliament |
| Parliamentarians' religion, denomination, sexuality | Guesses by OpenAI's GPT from the Wikipedia biography, with the model's own certainty for religion. For sexuality the model had only two answers (heterosexual or homosexual) and no "unknown": it was told to assume heterosexual when it could not tell | Legitimate interests | Research (9(2)(j) + Schedule 1 paragraph 4, Articles 84B and 84C); where the person has stated it publicly, 9(2)(e); for identifiable publication, the special purposes exemption (DPA Schedule 2 paragraph 26) | Our own inference from public biographies |
| Ideology scores | Scores our statistical model derives from recorded votes | Legitimate interests | Political opinions: 9(2)(e) (public votes) and research | Our own model |
| Election candidates | Names, parties, results; gender and religious background guessed from the name (the member's own record, with AI-guessed religion, for a candidate who is a parliamentarian) | Legitimate interests | Party: 9(2)(e). Religion name guess: research; paragraph 26 for identifiable publication | Published election results; our own rules |
| Donors and payers | Names, amounts, dates, recipients, company numbers; gender and religious background guessed from the name for individuals (the member's own record, with AI-guessed religion, for a donor or payer who is a parliamentarian) | Legitimate interests | A donation can reveal political opinions: research; statutory public register. Religion name guess: research; paragraph 26 | Electoral Commission, Register of Interests, Companies House; our own rules |
| Others named in the Register | Family members employed, landlords, employers, as the Register prints them | Legitimate interests | None normally | Register of Interests |
| GPT summaries of Register entries | Public Register text summarised | Legitimate interests | None normally | OpenAI API (past processing) |

People who have died are outside UK GDPR. Most of the data (back to 1832) concerns them.

Article 14 (telling people whose data came from elsewhere): not done individually because it would take
disproportionate effort (14(5)(b)): tens of thousands of people, most historical, with no contact details held. The
privacy notice, section 4, is the public notice, and the "Your data" page is the route to object or correct.

## 2. Legitimate interests assessment

**A. Running and moderating the service.**
Purpose: keep illegal and abusive content off a public political discussion site run by one person, and meet the
Online Safety Act's duties. Necessity: one moderator cannot read everything promptly; the tools order the queue and
never decide. The context sent to OpenAI's check exists to stop a reply being misread. Hashed addresses are the least
that lets a ban hold. Balance: users post publicly and are told about every tool in the Terms (rule 8) and the
privacy notice; a person makes every decision; flags and standing are seen only by the moderator; the one automated
effect (a held comment does not rise in popularity orders) is mild and reversible. Shared addresses (households,
universities) can be caught by an address bar: it lasts 180 days and is lifted on request. Outcome: the interests are
not overridden.

**B. Publishing the research data.** The full reasoning is `Parliament_Pulse_GDPR_justification.md` sections 4 to 6.
In short. Purpose: independent research and journalism on who is elected, who funds politics, how parliamentarians
vote and how groups are represented. Necessity: individual records are needed to link sources, check linkage and let
a reader verify any aggregate; provenance down to the individual observation is a site-wide principle. Balance:
strongest for sitting parliamentarians' public roles; weaker for candidates who never sat and for individual donors;
weakest for inferred religion and sexuality, where the risks are those in `DPIA.md` section 4. The measures relied
on are there too. Outcome, as decided by the controller on 24 November 2026: the processing continues unchanged, with
the measures in the DPIA.

**C. Usage log and (when built) first-party statistics.** Purpose: capacity and improving the site. Necessity: counts
by saved item, with the requester only to count distinct people and limit abuse. Balance: no profile is built, raw
rows go after 90 days, nothing is shared. Statistics of how the site is used, when built, will be the site's own,
with no third party, a plain notice and a simple way to object (PECR Schedule A1 paragraph 5, in force 5 February
2026), so no consent banner is needed. They are NOT built yet and the privacy notice does not mention them.

## 3. Retention

The periods are data in `helpers/retention.py` (`SCHEDULE`), which also deletes: the app runs `retention.purge()` at
every start, and `python -m helpers.retention` shows what is due. The privacy notice prints the same table.
`python -m helpers.retention --schedule` prints it as markdown. In brief: accounts and what they post, until closed
or deleted; the words of a deleted comment and the archive of deleted things, 90 days; reports, cases, data
protection requests, the decision log, AI assessments and the review-key record, two years (a decision stays longer
only while it is the reason for a suspension or bar still in force); client addresses on forms and raw usage rows,
90 days; hashed addresses per account, 90 days after last use; address bars 180 days; a barred email hash, no end
date.

Not adopted: deleting accounts that have not logged in for a long time. Revisit at the yearly review.

## 4. Who receives personal data

| Recipient | Role | What | Where | Terms and transfer | To do |
|---|---|---|---|---|---|
| Resend | Processor | Email addresses and the content of our emails | United States | Resend's data processing addendum (part of its terms) | Save a dated copy of the DPA; note the transfer mechanism it names |
| OpenAI, API (`/v1/moderations`) | Processor | Comments with context, no identifiers | United States | OpenAI's Data Processing Addendum, signed by both parties 24 November 2026 (`openai DPA.pdf`), with the UK addendum to the standard contractual clauses | Done. Optional: ask for zero data retention |
| OpenAI, API (GPT, past research on public sources) | Processor | Names and public biographies of parliamentarians; public Register text | United States | As above | Covered by the same signed DPA |
| OpenAI, consumer ChatGPT | Independent controller (the controller's recorded position, `background.md`) | Public comments with screen names and account IDs, read through a review key or pasted batch | United States | None relied on: the position is that no restricted transfer is initiated. `background.md` records that the ICO's guidance points the other way | "Improve the model for everyone" off in the account used. See DPIA risk 3 |
| Cloudflare | Processor | Every request, so internet addresses and content in transit | United States | Cloudflare's DPA (part of its self-serve terms) | Preview only. Will not be used when the site goes live: then remove it from the privacy notice |
| The host at go-live | Processor | Everything | To be decided | To be decided | **Choose a host with a DPA; prefer UK or EEA; update `helpers/privacy.py` `HOSTING` and this row** |
| MEGA | Processor | The repository's backup: the public datasets and this folder. No user accounts (the database is not backed up yet) | New Zealand (adequacy) and EEA | MEGA's terms | When database backups start, they will hold user data: encrypt them and add them here |
| Academic collaborator (University of Manchester) | To settle: separate or joint controller | The research datasets and replication archive | United Kingdom | None needed for a UK recipient | Agree in writing who is controller of what |
| NCA, police, courts, Ofcom, the ICO | Controllers in their own right | What the law requires | United Kingdom | Legal obligation | None |

## 5. Rights: how each is met

| Right | How |
|---|---|
| To be informed | The privacy notice at `/privacy`, linked from the footer, the More menu and the sign-up form |
| Access | `/privacy/request`. A logged-in account can download what it gave us at once. The full answer: `python -m helpers.data_requests export --user U-12` (or the moderation page), read `withheld` and `before_sending`, send within one month |
| Rectification | `/privacy/request`. For a value in the data: the corrections register (`routes/CLAUDE.md`, "Data protection") |
| Erasure | Close the account from `/privacy/request` (at once, with the password) or by request; `helpers/moderation.close_account` |
| Objection, restriction | `/privacy/request`; decided case by case, with reasons |
| Complaint | `/privacy/request` (complaint option): acknowledged by email at once, answered without undue delay (DPA 2018 s.164A) |
| Automated decisions | None that is solely automated with a legal or similarly significant effect (Articles 22A to 22D): a person decides every removal and account action; the one automated effect is the ranking hold described above |

What an answer to an access request leaves out, and why: who reported the person and what the report said, and who
blocked them (other people's data); the existence of a bar made for child sexual abuse or terrorism where telling
them would prejudice the prevention of crime (DPA 2018 Schedule 2 paragraph 2), decided each time.

## 6. Not required, and why

- **Data protection officer:** not required (not a public authority; no large-scale systematic monitoring as a core
  activity). The controller does it.
- **ICO fee:** the controller's position (24 November 2026) is that none is due yet because the site is not trading
  or open. Take the ICO's self-assessment again on the day the site opens to the public.
- **Appropriate policy document:** not needed for the research condition (Schedule 1 paragraph 4) or for 9(2)(e).
  One is needed for a Schedule 1 Part 2 condition: the CSEA sign-up bar relies on paragraph 10, so a short one is
  owed before opening (half a page: what, why, retention).
