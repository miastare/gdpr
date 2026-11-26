# Answering a data protection request

How to deal with a request from someone about their personal data: a copy, a correction, deletion, an objection
or a complaint. The legal reasoning behind the answers is in `records/record_of_processing.md` section 5 and
`positions/research_data_justification.md` section 8.

## What the app provides (built 24 November 2026)

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

The register is `ingestion_update/data/manual/data_subject_corrections.json` (in the repository, not this folder).
It is applied every time the app loads its data, so a correction shows from the next restart and survives every
rebuild. Add an entry:

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

What a correction does on the site: the member page shows "corrected on request" in place of "(AI guessed)" and
leaves out the confidence badge. A corrected religion or denomination gets certainty 100% (1 on a 0-to-1 column,
100 on a column stored as a percentage), so it also plots as fully certain wherever the certainty is used. Setting a
value to unknown leaves its certainty empty.

This layer changes what the site shows. It does not change the pipeline's own files, the tables the ideology model
was fitted on, or the paper's replication archive (frozen on purpose: it reproduces the paper). For a
parliamentarian, also enter the correction at source before the next ingestion run
(`ingestion_update/manual_ingestion_info.py`, `FURTHER_MANUAL_INPUT`), so that everything derived from the members
table agrees.

Whether to change a value is your decision each time. "Nothing is removed" (24 November 2026) is about the columns as
a whole; setting one person's disputed estimate to unknown at their request is a correction of an inaccurate value,
and it is what the justification paper (section 8) and the privacy notice promise.
