# What to do if personal data is breached

**Controller:** Samuel Kinshuck. **Written:** 26 November 2026 (DPIA risk 8). **Review:** with the DPIA, and after
any incident. Not legal advice. Keep a printed copy: the day it is needed, this machine may be the problem.

## The two clocks

- **72 hours** from the moment you become aware of a breach to tell the ICO, unless the breach is unlikely to put
  anyone at risk (UK GDPR Article 33). If you cannot find everything out in that time, report what you know and
  add to it later. A report after 72 hours must say why it is late.
- **Without undue delay** to tell the people affected, if the risk to them is high (Article 34).

Every breach is written in the log at the foot of this file, reported or not (Article 33(5)).

## What counts

A breach is any incident in which personal data is lost, destroyed, changed, or seen or taken by someone who
should not have it. For this site that means, for example:

- someone other than you got into the server, the database, the admin account or a backup;
- the settings file with the secrets (`/etc/parliamentpulse/<environment>.env`), the SSH key or the laptop was
  lost, stolen or copied (the laptop holds a database with accounts in it and the repository's own secrets);
- a fault in the app showed one person's private information to another: an email address, a private chart, who
  reported whom, a moderation record, a data protection request;
- an email went to the wrong person;
- user data was lost and there is no backup to restore it from;
- a processor tells you it had a breach touching the site's data (IONOS, Cloudflare, Resend and OpenAI must each
  tell you: their notices go to the email address of your account with them). Your 72 hours start when you read it.

Not a breach: the published research data and public comments being copied (they are public); the site being
down with nothing lost.

## What the site holds, most sensitive first

1. Who reported whom and why; the moderator's decisions; reports of suspected crimes (criminal offence data).
2. Data protection requests and what people wrote in them.
3. Email addresses of account holders, with their screen names (the link between a real address and a public
   political identity).
4. Password hashes (scrypt: slow to crack, but a weak password can still be guessed).
5. Hashed internet addresses, and the key that makes those hashes (`ADDRESS_HASH_KEY`). The hashes are useless
   without the key; with it, an address can be tested against them.

Likes, dislikes, comments and shared charts are public already.

## First hour: stop it and keep the evidence

The commands name `production`; put `staging` for the staging site. The server and its commands are described in
the hansard repository, `DEPLOYMENT.md` and `deploy/README.md`.

1. Write down the time and what you saw. Do not delete anything, and do not rebuild the server yet.
2. If someone may still be inside, take the site off the internet. Either stop the app:
   `ssh parliamentpulse sudo systemctl stop parliamentpulse@production`, or, if you cannot trust the server at
   all, turn off its route in the Cloudflare dashboard (Zero Trust, Networks, Tunnels) and shut the machine down
   from the IONOS panel.
3. Save the logs somewhere off the server before they roll over:
   `ssh parliamentpulse "sudo journalctl -u parliamentpulse@production --since '-14 days'" > incident_app.log` and
   the same for `-u ssh`. Cloudflare's dashboard has the request log for the same days.
4. Replace every secret that could have been seen, at the company that issued it, then in the settings file
   (`sudoedit /etc/parliamentpulse/<environment>.env`) and restart the app:
   - `FLASK_SECRET_KEY`: replacing it logs every account out at once.
   - the database password, the Resend key, the OpenAI key, the Cloudflare tunnel token, the SSH key;
   - `ADDRESS_HASH_KEY` only if the key itself was exposed: replacing it means existing sign-up bars by internet
     address stop matching.
   - your own admin passwords: the ordinary one through "Forgot your password", the second one with
     `ssh -t parliamentpulse pulse-run production -m helpers.auth_store --second-password <email>`.
5. If the admin account was used by someone else, read the decision log for what they did:
   `ssh parliamentpulse pulse-run production -m helpers.moderation log`.

## First day: work out who is affected and how badly

Answer these in writing (they are what the ICO asks):

- What happened, when, and how you found out.
- Which of the kinds of data above, and about how many people and records
  (`ssh parliamentpulse pulse-run production -m helpers.auth_store --list` counts the accounts).
- What could happen to those people: an account taken over here or elsewhere (reused passwords), a reporter
  identified to the person they reported, a political identity tied to a real email address, embarrassment,
  harassment.
- What you have done and will do.

Then decide:

| What was exposed or lost | ICO | The people |
|---|---|---|
| Nothing personal beyond what is public | No. Log it | No |
| Email addresses or password hashes of account holders | Yes | Yes: ask them to change their password here and wherever they used the same one |
| Reports, moderation records, data protection requests, or anything tying a reporter to a report | Yes | Yes, each person named, individually |
| An email sent to the wrong person | Depends on what it said: a sign-up link, no; a moderation decision or a data protection answer, yes | The person it was about, if it said anything about them |
| The address hashes alone | No. Log it | No |
| The address hashes with their key | Yes | Only if the addresses can be tied to named accounts |

If you are unsure whether the risk is real, report: a report that turns out not to have been needed costs nothing.

## Telling the ICO

- Online: ico.org.uk, "Report a breach" (the personal data breach form). By telephone: 0303 123 1113.
- Say: what happened; the kinds of data and roughly how many people and records; the likely consequences; what
  you have done; and how to reach you. Keep the reference they give you.
- If the form asks for an ICO registration number: there is none while the site is not trading
  (`records/record_of_processing.md` section 6). Say so plainly.

## Telling the people

In plain words: what happened and when, what information of theirs was involved, what you have done, what they
should do (a new password here and anywhere they used the same one; be wary of emails pretending to be from the
site), and how to ask you questions (the "Your data" page). Send it by email through the site's own sender. If the
email service itself is what was breached, put a notice on the site instead and email from another service once
you have one. There is no command that forces every account to choose a new password: replacing
`FLASK_SECRET_KEY` logs everyone out, and the email asks each person to use "Forgot your password".

## Who else

- The processor concerned, if the fault may be on their side (IONOS: the panel's support; Cloudflare, Resend,
  OpenAI: their support or security contacts).
- The police, through Report Fraud (the national reporting service for cyber crime, formerly Action Fraud), if
  someone broke in.
- The National Crime Agency only if child sexual abuse material is involved (the moderation handbook, R6, has
  that procedure). Ofcom does not have to be told of a data breach as such.

## Afterwards

Find the cause and fix it before the site goes back up. Restore from the last backup made before the intrusion if
data was changed. Then re-read DPIA risk 8 and the record of processing, and write the incident in the log below
and in the Online Safety review log (R8) if moderation was affected.

## Log

| Found | What happened | Data and people affected | Risk, and why | ICO told (when, reference) | People told (when, how) | What was done |
|---|---|---|---|---|---|---|
| | | | | | | |
