# Cloudflare: processor and international transfer record

**Prepared:** 26 November 2026, from the addendum itself and the way the site uses Cloudflare that day.
**Supplier:** Cloudflare, Inc. (United States).
**Status:** in use: in front of the laptop preview since November 2026 and of the staging site on the server since
26 November 2026. It stays in front of the public site (the controller's decision, 26 November 2026; until then
the records said Cloudflare was for the preview only and would go at go-live).
**Record owner:** Samuel Kinshuck, controller of Parliament Pulse.
**Next review:** with the DPIA (before the site opens, then yearly); when the Data Privacy Framework entry's next
certification date passes; and when another Cloudflare feature is switched on (Turnstile is planned).

The addendum is `processors/cloudflare/cloudflare_customer_dpa-v6.4_april_3_2026.pdf` (version 6.4, 3 April 2026,
downloaded from Cloudflare's site on 26 November 2026). The record of processing (section 4) carries the summary;
the privacy notice (section 5) says what a reader needs.

## 1. Supplier and contract

| Field | Details |
| --- | --- |
| Legal entity | Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, United States |
| Privacy contact | The data protection officer named in the addendum, legal@cloudflare.com |
| Plan | Self-serve (no enterprise contract) |
| Role | Processor for what passes through its network on the site's behalf. Controller of its own account data about the controller as its customer |
| Contract | The Data Processing Addendum "forms part of the Main Agreement", which for this account is the Self-Serve Subscription Agreement accepted when the account was made. It takes effect when the parties "otherwise agreed" to it, so it binds without a signature, and the current version replaces earlier ones. Nothing is signed and nothing needs to be |

## 2. What the site uses, and what Cloudflare sees

| Service | What for | Personal data |
| --- | --- | --- |
| DNS for parliamentpulse.co.uk | Finding the site | None of the site's users' |
| Tunnel (`cloudflared` on the server, and on the laptop for the preview) | The only way in: the server opens no web port | Every request and every answer, in transit: the visitor's internet address, what they send and what the site returns. The encrypted connection from the browser ends at Cloudflare, so this includes passwords at sign-up and log-in, which Cloudflare carries and does not keep |
| Access (Zero Trust) in front of staging and the preview | A login that admits named people only | The email address of each person admitted (the controller's own; for the preview, a few invited people), and a record of their logins |

Not used: Cloudflare's analytics script in the page, Workers, R2, Images, email routing, logs sent elsewhere.
Planned, not built: Turnstile on sign-up and the logged-out forms (it will need a sentence in the privacy notice
first). Cloudflare stores none of the site's database. It does keep its own request records for a time, and may
keep copies of static files (scripts, pictures) at its edge.

**Cookies.** Access sets its own login cookie for the people it admits. On the public site, Cloudflare can set a
security cookie of its own (`__cf_bm` when bot protection is on, `cf_clearance` after a challenge). They are
strictly necessary, so no consent is needed, but section 3 of the privacy notice lists what is kept in the
browser: before the site opens, look at the cookies a logged-out visitor to the public address is given and add
any of Cloudflare's to that section.

## 3. Where the data goes and the transfer

Cloudflare handles a request at a data centre near the visitor (for a visitor in the United Kingdom, usually in
the United Kingdom) and Cloudflare, Inc. is in the United States, so this is treated as a restricted transfer.

| Item | Position |
| --- | --- |
| Primary mechanism | The UK Extension to the EU-US Data Privacy Framework (the "UK-US data bridge"). The addendum says Cloudflare complies with the Framework, which it defines to include the UK Extension, and that such transfers are not restricted transfers (clauses 1.1(h), 1.1(p) and 6.4) |
| Checked on the Framework's own list | **Not yet.** Search for Cloudflare at https://www.dataprivacyframework.gov/list, confirm that the UK Extension is shown as active, and save a screenshot here, as was done for Resend |
| Fallback | If the certification lapses Cloudflare must say so, and the EU standard contractual clauses then apply with the UK's International Data Transfer Addendum, which is "deemed executed" (clauses 6.2(b) and 6.4). That route would need a transfer risk assessment |
| Requests from authorities | Cloudflare tells the customer unless forbidden, sends the authority to the customer, and challenges a request that conflicts with the law protecting the data (clause 8) |

## 4. What the addendum provides (UK GDPR Article 28(3))

| Topic | Clause |
| --- | --- |
| Processing only to provide the service and on the customer's instructions; no use for marketing or advertising | 3.1(a), (b) |
| Security measures (Annex 2: encryption, access control, logging, ISO 27001 and 27701, SOC 2) | 3.1(c) |
| Confidentiality of staff | 3.1(d) |
| Breach: notice without undue delay, with help | 3.1(e) |
| Help with people's rights requests, impact assessments and breach reports (at the customer's cost) | 3.1(g), (h), (j) |
| Deletion or return at the end | 3.1(i) |
| Sub-processors: a published list (https://www.cloudflare.com/gdpr/subprocessors/), 30 days' notice on that list, 10 days to object, Cloudflare liable for them | 4 |
| Audit: an independent audit report, and an audit in person in limited cases | 5 |

## 5. What remains to do

- [ ] The Data Privacy Framework screenshot (section 3).
- [ ] Before the site opens: the cookies check (section 2).
- [ ] When the laptop preview is retired: delete its tunnel and its Access application in the dashboard.
- [ ] Turnstile, when it is built: add it here and to the privacy notice first.
- [ ] Look at Cloudflare's sub-processor list at the yearly review (changes are posted there, not emailed).

## 6. Decision

Cloudflare is a suitable processor for carrying the site's traffic: an addendum meeting Article 28 that binds
without signature, a Framework certification the addendum commits it to keeping (still to be seen on the list),
contractual clauses behind it, and nothing of the site's stored there. The cost is that a United States company
sees every request, passwords included, as they pass. The benefit is that the server opens no web port and the
app, which is one process, is shielded from attack traffic. Recorded 26 November 2026.

## Log

| Date | Event | Evidence |
| --- | --- | --- |
| 26 November 2026 | Addendum version 6.4 (3 April 2026) downloaded and read; the staging site put behind a tunnel and an Access login on the new server; decision to keep Cloudflare in front of the public site; this record written | This folder |
