# Parliament Pulse: appropriate policy document (criminal offence data)

**Controller:** Samuel Kinshuck. **Adopted:** 26 November 2026. **Review:** with the DPIA (before the site opens,
then yearly), and whenever the processing below changes. **Kept:** while this processing goes on and for six months
after it ends (DPA 2018 Schedule 1 paragraph 40), and given to the ICO on request.

This is the document DPA 2018 Schedule 1 Part 4 requires where a condition in Schedule 1 Part 2 is relied on. It
covers the site's moderation records that relate to criminal offences. The record of processing
(`records/record_of_processing.md`, section 1A) gives the Article 6 basis for each activity and points here.

## What is covered, and the conditions relied on

The site is a user-to-user service under the Online Safety Act 2023. Some of what it holds about its users is
criminal offence data (UK GDPR Article 10; DPA 2018 section 11(2): it includes the *alleged* commission of offences):

1. **Reports of suspected illegal content** (the report reasons child sexual abuse, terrorism, threats or
   harassment, stirring up hatred, fraud, and "something else against the law"), with the appeals and complaints
   about them.
2. **The moderator's decisions on them** (the decision log, with a copy of the item as it was), and the archive of
   removed content kept so that child sexual abuse material can be reported to the National Crime Agency.
3. **Sign-up bars** made when an account is suspended for child sexual abuse or terrorism, or removed, or barred by
   the moderator for a serious breach: a hash of its email address and keyed hashes of its internet addresses.

Conditions (DPA 2018 Schedule 1, each applied to criminal offence data by paragraph 36, so that the "substantial
public interest" words do not apply):

- **Paragraph 6, statutory purposes**, for 1 and 2: the processing is necessary to carry out the duties the
  Online Safety Act 2023 places on the service (dealing with illegal content, reporting and complaints, keeping
  records), and to report child sexual abuse material to the National Crime Agency as the law requires.
- **Paragraph 10, preventing or detecting unlawful acts**, for 3, and for 1 and 2 so far as they serve the same end:
  a bar exists to stop a person who has used the site for a serious crime from coming back. It must be done without
  the person's consent, since asking would defeat it. A disclosure to the National Crime Agency or the police
  meets paragraph 10 without this document (paragraph 10(2)); it is covered here anyway.

## How the data protection principles are met

- **Lawful, fair and open.** The privacy notice (`helpers/privacy.py`, at `/privacy`) says that reports, decisions
  and an archive are kept, that a removed or seriously suspended account is barred from signing up again by hashed
  email and internet addresses, and on what basis. Terms rules 9 to 11 say how reports, decisions, bars and appeals
  work. A person is told of a decision about them, unless telling them could put someone at risk (content reported
  to the National Crime Agency).
- **Purpose limitation.** Used only to deal with reports, enforce the rules, keep barred people out and meet the
  Online Safety Act and reporting duties. Never published. Reports' reasons and moderator removals are not sent to
  ChatGPT through the review keys.
- **Data minimisation.** A bar holds hashes only: the email as a hash of the normalised address, the internet
  addresses as HMAC-SHA256 with a secret key held outside the database. The moderator's alert of a report of
  illegal content names the item and the reasons ticked, never what was posted or what the report said. The person
  reported is never told who reported them.
- **Accuracy.** A report is recorded as an allegation, not a finding. Nothing is removed and no bar is made
  automatically: a person, the moderator, decides each time. There is an appeal (Terms rule 11); lifting a
  suspension lifts its bars; an internet address bar is lifted when an innocent person sharing the address asks.
- **Storage limitation.** Reports, cases, the decision log: three years, longer only while a decision is the reason
  for a suspension or bar still in force. The archive of removed content: 90 days. An internet address bar: 180
  days. An email bar: no end date, because its purpose (keeping out a person removed for a serious crime) does not
  end; it is deleted 90 days after it is lifted. The periods are in `helpers/retention.py` and are enforced at every
  start of the server, which is restarted at least every 14 days.
- **Security.** Moderation records are read only through the moderator's admin routes; the hashing key is kept
  outside the database, and is to be kept out of any backup of it; every moderation action is logged. The breach plan is DPIA risk 8.
- **Rights.** A subject access request is answered from the full export, but who reported someone, and a bar made
  for child sexual abuse or terrorism, are withheld where disclosure would prejudice the prevention of crime
  (DPA 2018 Schedule 2 paragraph 2), decided each time.

## Retention and erasure of this data

As in the storage limitation paragraph above. The record of processing (sections 1A and 3) records that this data
is kept and erased in line with this document.
