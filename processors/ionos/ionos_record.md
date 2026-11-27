# IONOS: processor record

**Prepared:** 26 November 2026, from the agreement itself and the server as it was set up that day.
**Supplier:** IONOS Cloud Ltd. (United Kingdom).
**Status:** in use since 26 November 2026 for the staging site; the public site will run on the same server.
**Record owner:** Samuel Kinshuck, controller of Parliament Pulse.
**Next review:** with the DPIA (before the site opens, then yearly), or sooner if IONOS gives notice of a new
sub-processor or the server is moved.

The agreement is `processors/ionos/Data Processing Agreement.pdf` (version 2.0, dated March 2026, downloaded
26 November 2026 from https://www.ionos.co.uk/terms-gtc/data-processing-agreement/). The record of processing
(section 4) and the DPIA (risk 8) carry the summary; the privacy notice (section 5, from version 2026-11-26) says
what a reader needs. What is on the server is described in the hansard repository, `DEPLOYMENT.md`.

## 1. Supplier and service

| Field | Details |
| --- | --- |
| Legal entity | IONOS Cloud Ltd. (the agreement's "IONOS Cloud Limited") |
| Service | One virtual server: VPS Linux XL+ (8 vCores, 16 GB memory, 480 GB disk, Ubuntu 24.04), bought 26 November 2026, monthly |
| Where | A United Kingdom data centre |
| Role | Processor: it provides the machine, its storage and its network. It does not administer the system, the database or the app, which the controller does over SSH with a key only the controller holds |
| Contract | The Data Processing Agreement forms part of the contract for the server (clause 12.2) and began with the order (clause 12.1). Nothing is signed |

## 2. What is on the server

Everything the site holds: the app, the published datasets, and the database with the accounts (email addresses,
password hashes, screen names), what users post, likes and dislikes, reports, the moderator's decisions, the
archive of deleted content, the sign-up bars and the data protection requests. The settings file holds the
secrets, including the key of the internet address hashes. The disk is not encrypted by the controller, so
IONOS's own staff and systems are the trust boundary: the agreement's confidentiality and security clauses are
what covers that.

Not on the server: the repository, the pipelines, the compliance records, any backup (none is made yet; when
database backups start they will be encrypted and kept elsewhere, and are added to the record of processing then).

## 3. Where the data goes

The agreement keeps the processing in the United Kingdom or the European Economic Area, "unless the transfer of
data to third countries becomes necessary in order to provide the service", in which case IONOS must meet the
law's requirements for the transfer (clause 4.3). The EEA is covered by UK adequacy regulations, so no transfer
mechanism of the controller's own is needed. No transfer beyond the UK and EEA is expected for a server in a UK
data centre.

## 4. What the agreement provides (UK GDPR Article 28(3))

| Topic | Clause |
| --- | --- |
| Processing only on documented instructions, including for transfers | 4.2, 5.1 |
| Confidentiality of staff | 5.4 |
| Security measures, reviewed regularly; ISO 27001 certification | 8, 9.2 |
| Sub-processors: general permission, a published list ("IONOS Core Sub Processors"), notice of changes, 14 days to object, the same obligations passed on | 10 |
| Help with people's rights requests (IONOS may charge) | 5.2, 7 |
| Help with security, breach notification and impact assessments (IONOS may charge) | 5.3 |
| Breach: IONOS tells the customer immediately | 5.5 |
| Deletion or return at the end of the contract (deletion if nothing is chosen) | 5.7 |
| Information and audits; an audit in person only if the ISO 27001 certificate lapses or after a notifiable breach | 9 |
| A data protection officer, with a published contact | 5.6 |
| Governing law: England | 12.4 |

The customer's own duty under clause 6.2: before the contract ends, delete whatever personal data is on the
server. So when the server is given up, drop the databases and wipe the disk first.

## 5. What remains to do

- [ ] Check that the IONOS invoice or contract page names IONOS Cloud Ltd., the company in the agreement.
- [ ] Open the two links inside the agreement (clause 8.2, the technical and organisational measures; clause 10.2,
      "IONOS Core Sub Processors") and save each page as a PDF in this folder. Look at the sub-processor list for
      anything outside the UK and EEA that would touch a UK virtual server.
- [ ] IONOS's notices of new sub-processors, when they arrive (to the account's email address): 14 days to object.
- [ ] When database backups start: encrypted, off the server, and never with `ADDRESS_HASH_KEY`.

## 6. Decision

IONOS is a suitable processor for hosting the site: an agreement meeting Article 28, processing kept in the United
Kingdom or the EEA, ISO 27001, and a role limited to providing the machine (recorded 26 November 2026). The
security of the system on that machine is the controller's own job (DPIA risk 8).

## Log

| Date | Event | Evidence |
| --- | --- | --- |
| 26 November 2026 | Server bought; staging site running on it behind a Cloudflare login that admits the controller only. Agreement (version 2.0, March 2026) downloaded and read; this record written; privacy notice 2026-11-26 names IONOS | This folder; `published_notice/2026-11-26.md` |
