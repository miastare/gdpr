# Resend: processor and international transfer record

**Prepared:** 25 November 2026 (rewritten the same day from a first draft made with ChatGPT: its guesses about how the
site uses Resend were replaced with what the code does, and its open questions with the controller's answers).
**Supplier:** Resend (Plus Five Five, Inc.)
**Status:** in use. UK Extension certification active (re-certification under review); the participant page was saved
as `processors/resend/dpf_listing_2026-11-25.png` on 25 November 2026.
**Record owner:** Samuel Kinshuck, controller of Parliament Pulse.
**Next review:** with the DPIA (before the site opens, then yearly), and after 3 March 2027 (the listing's next
certification date), or sooner if Resend gives notice of a change of sub-processor, its certification lapses, or the
site starts using another Resend feature.

The DPA itself is `processors/resend/resend_dpa_2025-12-31.md` (the version of 31 December 2025). The record of processing (section 4, "Who receives
personal data") and the DPIA (risk 2a) carry the summary; the privacy notice (section 5) says what a reader needs.

## 1. Supplier

| Field | Details |
| --- | --- |
| Trading name | Resend |
| Legal entity | Plus Five Five, Inc., 2261 Market Street #5039, San Francisco, CA 94114, United States |
| Privacy contact | privacy@resend.com |
| Service used | The Emails API (sending) only |
| Role | Processor for the emails the site sends. Resend is a controller only of its own account and service-usage data about us as its customer (DPA section 9) |
| Contract | Data Processing Addendum of 31 December 2025, part of Resend's terms of service and binding from the account's sign-up (preamble and signature note of the DPA). The executed copy can be downloaded from the Resend dashboard (Settings, Documents) |

## 2. What the site sends through Resend

Every email goes through one function, `helpers/auth_email._send`, which calls `resend.Emails.send` with a sender, one
recipient, a subject and an HTML and a plain-text body. `helpers/moderation.py` and `helpers/data_requests.py` send
through it too.

| Field | Details |
| --- | --- |
| Emails | Sign-up confirmation; password reset; engagement emails (someone liked or replied to the account's comment or chart: asked once, off with one click); moderation decisions to the people concerned and alerts to the moderator; data protection acknowledgements, answers, extensions and the operator's alert of a new request |
| Personal data | The recipient's email address; the subject and body. A body can carry another person's words (an engagement email quotes the reply; a moderation decision gives the moderator's explanation; a data protection answer whatever the request was about) |
| Sender | `ParliamentPulse <accounts@auth.parliamentpulse.co.uk>` (env `RESEND_FROM_EMAIL` can change it) |
| Not used | Contact lists or audiences, broadcasts or marketing, inbound email, webhooks, attachments, open and click tracking (both off in the Resend dashboard: checked by the controller, 25 November 2026) |
| Never sent | An address on a reserved test domain (`is_test_address`: example.com, .test and the like) is printed, not sent |
| Lawful basis | As for the purpose of each email in the record of processing: contract for the account emails; legitimate interests for engagement and moderation emails; legal obligation for answers to data protection requests. Appointing Resend needs no basis of its own |
| Special category data | Not sent on purpose. A data protection answer about a parliamentarian's recorded religion or sexuality could mention it; that is the person's own request and the answer goes only to them |
| Credentials | `RESEND_API_KEY` in the server's environment, never in the repository |

## 3. Where the data goes and the transfer

Resend names the United States as its main place of processing and storage, so every email is a restricted transfer
under UK GDPR Chapter V.

| Item | Position |
| --- | --- |
| Primary mechanism | UK adequacy regulations for the UK Extension to the EU-US Data Privacy Framework (the "UK-US data bridge"). Resend (Plus Five Five, Inc.) is certified; participant record https://www.dataprivacyframework.gov/participant/8907 |
| Certification checked | 25 November 2026, participant page saved as `processors/resend/dpf_listing_2026-11-25.png`: both the EU-US Framework and the UK Extension "Active" (re-certification under review), first certified 20 February 2025, next certification due 3 March 2027, non-HR data, self-assessed, with the ICO as the recourse body for UK complaints. The listing names the DPA at resend.com/legal/dpa as Resend's policy for the data |
| Fallback | The DPA incorporates the EU standard contractual clauses, with the UK International Data Transfer Addendum for UK data (section 6.4), and supplementary measures (section 6.6). If the certification lapsed these would apply, with a transfer risk assessment |
| Commitment | DPA section 11: Resend keeps its certification and tells us if it can no longer meet the Framework's principles |

## 4. What the DPA provides

| Topic | DPA |
| --- | --- |
| Acting only on our instructions | Section 2 |
| Confidentiality of staff | Section 3 |
| Sub-processors: a published list, at least 14 days' notice of a new one, a right to object, Resend liable for them | Section 4 |
| Security | Section 5 and Exhibit C (encryption at rest and in transit, access control, logging, incident response) |
| International transfers | Section 6 |
| Help with people's rights requests | Section 7 |
| Breach notice without undue delay; help with impact assessments | Section 8 |
| Return or deletion: customer data removed within 90 days of the account ending | Section 2.4 and Exhibit A |

## 5. Sub-processors and retention

- Resend publishes its sub-processor list (https://resend.com/legal/subprocessors). For sending, the ones that matter are
  its hosting and sending infrastructure and TypeSafe AI, which checks a sample of outgoing emails for spam and phishing;
  Resend states that TypeSafe keeps none of it and trains on none of it, and that neither Resend nor its AI
  sub-processors train models on customer content. Resend's other AI features (the dashboard assistant, inbound
  inboxes) are not used.
- Resend keeps each email and its delivery record for 30 days on the Free, Pro and Scale plans, then deletes them. The
  privacy notice says so (section 5). An individual email can be removed earlier only through Resend's support, by its
  message id: worth doing if an email was sent to the wrong person.

## 6. What remains to do

- [x] Screenshot of Resend's Data Privacy Framework entry (participant 8907) saved: `processors/resend/dpf_listing_2026-11-25.png`, 25 November 2026.
- [ ] Look at the entry again after 3 March 2027 (its next certification date; on 25 November 2026 its
      re-certification was under review) and at each yearly review. If it has lapsed, the DPA's contractual clauses
      apply and need a transfer risk assessment.
- [x] Open and click tracking are off in the Resend dashboard (checked 25 November 2026).
- [ ] Optional: download the executed DPA from the dashboard and keep it beside `processors/resend/resend_dpa_2025-12-31.md`.
- [ ] Read Resend's notices of new sub-processors when they arrive, and look again if one would receive email content.

## 7. Decision

Resend is a suitable processor for the site's emails: a DPA meeting Article 28, a current UK Extension certification,
contractual clauses behind it, 30-day retention, and emails that carry no more than each purpose needs (recorded
25 November 2026, with the DPIA's sign-off).

## Log

| Date | Event | Evidence |
| --- | --- | --- |
| 25 November 2026 | DPA of 31 December 2025 saved (`processors/resend/resend_dpa_2025-12-31.md`); UK Extension certification checked as active by the controller; open and click tracking checked off; a test data protection request (DR-43) answered, all three emails received; screenshot of the Data Privacy Framework entry saved (both the EU-US Framework and the UK Extension "Active" (re-certification under review), first certified 20 February 2025, next certification due 3 March 2027, non-HR data, self-assessed, with the ICO as the recourse body for UK complaints); this record written | This folder |
