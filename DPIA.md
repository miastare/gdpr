# Parliament Pulse: data protection impact assessment

**Controller:** Samuel Kinshuck. **Assessment carried out:** 24 November 2026, by Claude (an AI assistant) at the
controller's instruction, from the code as it stood that day and the controller's two papers in this folder. It is
not legal advice, and nobody has audited the data itself. **Status:** draft for the controller to read, amend and
sign (section 7). **Review:** before the site opens; when a new tool, dataset or recipient is added; yearly.

Why one is needed (UK GDPR Article 35): special category data (political opinions, religion, sexual orientation),
some of it inferred by an AI model or by rules, about identifiable people, published; and new technology (AI
moderation tools) applied to users' political comments.

## 1. What is being assessed

Two different things, assessed separately because their risks are different.

**A. The service: accounts, comments, moderation.** People create an account (email, password hash, screen name),
post public comments and charts, and like or dislike things in public. One person moderates, helped by four tools
(Terms rule 8): a text filter, a word list, OpenAI's moderation API, and an AI-assisted review through ChatGPT.
Supporting records: reports, the decision log, a 90-day archive of deletions, hashed internet addresses, sign-up
bars. Detail: `record_of_processing.md` section 1A and `../Ofcom/GDPR dependencies/README.md`.

**B. The data: people in public political life.** Parliamentarians since 1832, election candidates, donors and
people named in the Register of Interests, from public sources, explorable down to the individual record. It
includes, for identifiable living people:

- religion, denomination and sexuality of parliamentarians, guessed by OpenAI's GPT-4.1 from the person's
  Wikipedia biography. **For sexuality the model was allowed only two answers, heterosexual or homosexual. It had
  no "unknown" answer:** the prompt told it to assume heterosexual whenever it could not tell, to answer homosexual
  where a person was rumoured to be or to have been, and to count bisexual as homosexual. So every parliamentarian
  has a value, "Heterosexual" on the site includes everyone about whom the biography said nothing (15,872 of
  16,157 people in the data are "Heterosexual", 285 the other answer), and the other answer is shown as "Likely
  not heterosexual". Religion is different: there the model could answer "Unknown" (668 people);
- gender and religion of election candidates and of individual donors, guessed from the name by fixed rules
  (for example a surname list), blank for most people.

Scale: about 2 accounts today (the site is not open); the data covers tens of thousands of people, most of them dead
and so outside the law. Nobody under 18 is expected (accounts are for adults; the sign-up form asks).

**Decision recorded by the controller, 24 November 2026:** none of the religion, sexuality or gender information is
to be removed or restricted. The measures open to this assessment are therefore labelling, explanation, correction
and misuse controls.

## 2. Consultation

- Data subjects were not asked. For users, the Terms and privacy notice explain the processing before sign-up. For
  people in the data, asking tens of thousands of people is not practicable; the "Your data" page is the standing
  route for objections.
- The academic collaborator's institution has a data protection team. Asking it to look at section 4 would be the
  cheapest independent check available, and the justification paper suggests it.
- Processors: OpenAI's and Resend's published terms were relied on, not asked.

## 3. Necessity and proportionality

Legal bases are in `record_of_processing.md`. Points that matter here:

- **Minimisation, service side.** OpenAI's moderation API gets no screen name, account or email. The review key gets
  screen names and account IDs because harassment is a pattern across one person's comments. Since 24 November 2026
  it gets nothing a moderator removed, not the count of removals, and no report counts, reasons or flags. Age answers are counted, not stored.
- **Minimisation, data side.** No bulk download. Member and constituency pages are in the sitemap; candidate and
  donor pages are not.
- **Accuracy.** A person decides every moderation action. For the inferred data, accuracy is the weak point: there is
  no measured error rate for the GPT estimates or the name rules (the provenance text says the certainty figure is
  the model's own opinion, not a measurement).
- **Rights.** Built on 24 November 2026: the privacy notice, the request page, the account download, account
  closure, the subject access export, the corrections register, the retention schedule.

## 4. Risks and measures

Likelihood and severity are for the individual, judged after the measures already in place.
Scale: low / medium / high.

### A. The service

| # | Risk | Measures in place | Residual | Further measure |
|---|---|---|---|---|
| 1 | A user's political opinions are exposed further than they expect (comments, likes and dislikes are public per account) | Screen names, not real names; the one-time notice at the first like; Terms rule 1; privacy notice | Low | None |
| 2 | Comments go to OpenAI's moderation API in the United States | No identifiers sent; OpenAI's Data Processing Addendum signed by both parties on 24 November 2026 (`openai DPA.pdf`, version 010126: OpenAI as processor on the controller's instructions, with the UK addendum to the standard contractual clauses for the transfer) | Low | Optional: ask OpenAI for zero data retention on the API account, which the addendum does not itself give. The addendum covers the API account only, not consumer ChatGPT (risk 3) |
| 3 | Comments with screen names and account IDs are read by consumer ChatGPT: no processor contract and no transfer safeguard, on the controller's reading that no restricted transfer is initiated (`background.md`, which itself says the ICO's guidance points the other way) | Only content already public; nothing removed or deleted; no report counts, reasons or flags (since 24 November 2026); temporary read-only keys; a log of everything served; model training switched off; a person decides | **Medium**: low harm to individuals, but the legal position is the least certain in the project | The lower-risk alternative stays available: run the same review through the API under the DPA |
| 4 | An automated tool wrongly marks a comment, or errs more against some views | Nothing is removed automatically; the only automatic effect is that a flagged comment does not rise in popularity orders, and not for accounts in good standing; complaint route in the Terms | Low | Keep a note of how often passed or flagged comments turn out wrong in spot checks; look for a pattern by viewpoint after six months of real use |
| 5 | Standing: a hidden score about a person | Not stored, moderator-only, one mild effect, disclosed on a subject access request | Low | None |
| 6 | Hashed internet and email addresses could be reversed: the hash uses a fixed prefix, not a secret key, so every IPv4 address can be tried | Short retention (90 and 180 days); the table is not public | Low to medium | **Recommended: hash with a secret key (HMAC) held outside the database.** Existing rows would have to be left to expire |
| 7 | An address bar catches an innocent person who shares an address | 180 days only; lifted on request; Terms rule 10 says how to ask | Low | None |
| 8 | A breach of the database (emails, password hashes, moderation records) | Passwords hashed with scrypt; link tokens stored only as hashes; admin routes answer 404 to others; rate limits | **Medium until deployment is settled** | Before opening: security headers and a content security policy; encrypted database backups (none exist); a host with a DPA; a one-page note of what to do on a breach (the ICO must be told within 72 hours if people are at risk) |
| 9 | Records kept too long | The retention schedule, enforced at every start | Low | None |
| 10 | Closing an account also deletes other people's replies to its comments | Stated in the privacy notice and on the closure form | Low | Later: keep the replies and show the parent as removed |

**Settled on 24 November 2026 (risk 3).** The recorded position is that a review key reads only what any visitor
can read. Until this date a key was also given, for each live comment, how many reports it had and the reasons
ticked, and whether the word list, OpenAI's check or an earlier review had flagged it. The controller decided that
none of that goes to ChatGPT. A key now gets none of it and cannot filter or sort by it; the server serves
reported and flagged comments first without saying which they are, so the review still starts where it matters.
Making the counts and flags public instead was considered and rejected: a ticked reason is an unproven accusation
against a named account, public counts invite pile-on reporting, and public flags teach evasion.

### B. The data

| # | Risk | Measures in place | Residual | Further measure |
|---|---|---|---|---|
| 11 | A living parliamentarian is shown as "Likely not heterosexual" when they have not said so themselves, or when it is wrong. Harm: distress; a complaint | The value is an estimate and is labelled as one everywhere it is shown ("Likely not heterosexual", never a statement of fact; "(AI guessed)" in the column's name; the red warning; the provenance answer, which gives the prompt and its default). The opposite error is built into the method and is acknowledged: the model had no "unknown" answer and was told to assume heterosexual, so "Heterosexual" is an assumption for almost everyone it is shown for, and a person who is not heterosexual but whose biography does not say so is shown as "Heterosexual". The site says this wherever sexuality is explained (the column's explanation, the provenance answer, the note beside every chart split by sexuality, the homepage gallery's warning and the privacy notice), and nowhere words it as if the model could have left the question open. **The controller has read every "Likely not heterosexual" case by hand and found none without a basis in public information about the person, such as their Wikipedia page** (his statement, 24 November 2026). The people concerned hold or held public office. Anyone can have their own value set to unknown through the correction route | **Low to medium** | Write down when the hand check was done and against what (one line under section 7) |
| 12 | A living parliamentarian is shown with a religion they do not hold | AI warning; certainty figure; provenance; correction route | Medium | L1, L2 |
| 13 | A living donor or candidate is listed under a religious background read from their name, and the site can show named people by it (for example donors to one party). Harm: a label the person rejects; misuse of such a list to harass a group | The column is named for what it is, the guessed religious background of the NAME, not the person's religion (renamed 24 November 2026; a donor or candidate who is a parliamentarian shows the member's AI-guessed religion instead, labelled so), with a red warning that says a rule read the name and nobody checked; each individual value is labelled by how it was reached; the rule that fired is shown; most cells are blank; the Terms forbid harassment and stirring up hatred, with reporting and moderation; no bulk download; candidate and donor pages are not in the sitemap; the correction route. The same list could be made by anyone from the Electoral Commission's public register and a list of surnames. The column serves research the controller intends on the representation of groups among political donors | **Medium** (the assessor's view; the controller rates it lower. Either way it is not high) | L5: publish how often the rule is right where that can be measured. L3 when the profile pages are revised |
| 14 | A guess or estimate loses its label when it travels: a shared chart, a screenshot, a tile that says "women gave £X" | Column names carry "(name guess)" or "(guessed)" in most places | Medium | L2, L3 |
| 15 | A correction is made and then lost at the next data rebuild | The corrections register is applied every time the app loads its data | Low | Also enter member corrections at source before the next ingestion run |
| 16 | A person cannot find out the site holds an inference about them | Public privacy notice; the page is indexed for parliamentarians | Medium for donors and candidates (they will rarely look) | None proportionate; individual notification is not practicable |
| 17 | Accuracy of the research itself: an unmeasured classifier presented in charts | The methods are described; the certainty figure is described as the model's own | Medium | L5 |

**Labelling measures (none removes data).** L1, L2 and L4 were carried out on 24 November 2026, and L3 for the
profile pages, Interesting Correlates and the homepage gallery texts on the same day. On 25 November 2026 the rest
of L3 followed: the interest cards' confidence wording, the stored titles of the four gallery charts that rest on a
guess, a red "AI guessed" chip in the profile tiles' titles that opens the column's explanation, and a standing
warning on the homepage gallery ("Religion and Sexuality data are AI guesses"). The site's term is "AI
guessed". Since that day a candidate, donor or payer who is a parliamentarian shows the member's own value (for
religion, the AI guess) in place of a name guess, labelled as such row by row. The text
below is the finding as first written; `routes/CLAUDE.md` ("Data protection") records what the code now does.

- **L1. Fix warnings that are wrong or missing** (metadata only): `religion_guess` (candidates) and
  `donor_religion_guess` carry the "guessed by a Large Language Model" warning but are name rules;
  `payer_religion_guess` and every gender guess have no warning at all. Give every name guess one consistent,
  truthful warning ("guessed from the name by a rule; may be wrong"), which needs a third kind of bubble beside the
  two AI ones.
- **L2. Say "guess" or "AI estimate" in the name wherever the value is shown.** The short picker names drop it
  ("Payer's Religion", "Donor's Gender"). Members' columns are called plainly "Religion", "Sexuality", "Recipient's
  Religion". Suggested: "Religion (AI estimate)", "Sexuality (AI estimate)", "Denomination (AI estimate)", and keep
  "(name guess)" in the picker names. Several places show the stored word "homosexual" where the label "Likely not
  heterosexual" should appear (member cards, the bar data modal, two profile tiles): route them through the label.
- **L3. Carry the status into shared charts and summaries.** "What this chart really shows" prints only the column
  name: add "(values estimated by an AI model)" or "(values guessed from names)" from the column's derivation. The
  donor tile "Women gave £X, men £Y" should read as a guess. The Interesting Correlates texts ("gay and lesbian MPs
  disproportionately backed…") and the gallery chart "Non-heterosexual parliamentarians" state estimates as fact:
  add "as estimated by an AI model from public biographies".
- **L4. Correct the confidence tooltip.** "We guessed this member's religion, and we are about N% confident we got
  it right" overstates it: the figure is the model's own rating. Suggested: "An AI model estimated this, and rated
  its own confidence at N%. That is not a measured accuracy."
- **L5. Measure and publish the error.** For a random sample of election candidates and donors with a name guess,
  compare the guess with what can confidently be said from public sources (for most, nothing can), and publish
  the result on the columns' explainers. The controller checked the sample directly, by hand, on 24 November 2026
  (`accuracy_check/RESULTS.md`): of 80 people sampled, nothing public settled the religion of 68; for 10 the guess
  matched the person's own stated religion; for 2 it matched the father's family background but not the religion
  the person states. Published on the columns' explainers. This is the single measure that most strengthens the research basis, because Article 84C asks for
  safeguards and the research condition asks that the processing be necessary for research that is done properly.

### Residual risk, Article 84C and Article 36

The first draft of this assessment (24 November 2026, morning) rated risks 11 and 13 high. It was revised the same
day on facts the controller supplied and changes made since:

- **Risk 11.** The draft assumed a "Likely not heterosexual" could rest on bare rumour and that nobody had checked.
  The controller has checked every case by hand: each rests on public information about the person. Nobody is
  "outed" by a label that repeats, as an estimate, what a public biography already indicates, and a site that says
  its labels are estimates does not carry the authority of a news report. The draft said this check would bring
  the risk down, and it has.
- **Sexuality had no "unknown" answer (recorded 25 November 2026).** The prompt allowed only "homosexual" or
  "heterosexual" and told the model to assume heterosexual when it could not tell. "Heterosexual" is therefore not
  a finding about the person in most cases, which bears on the accuracy principle (Article 5(1)(d)). The measure is
  explanation, not removal: every reader-facing account of the column now says that there was no "unknown" answer
  and that "Heterosexual" includes everyone about whom the sources said nothing, and the two values are shown as
  "Heterosexual" and "Likely not heterosexual". A person's own value can still be removed or changed on request
  through the correction route. The paper's replication archive carries the same two-valued variable.
- **Risk 13.** The column no longer states a person's religion. It states what their name suggests, says so in its
  name and warning, and labels each value by how it was reached. What remains is misuse of a list, which the
  public register already allows and which the Terms and moderation address.
- The same estimates of parliamentarians' sexuality will be in the paper's replication archive if the paper is
  accepted. That is the same controller publishing the same data, so it is within this assessment, not a reason of
  its own for a lower rating. It does mean that restricting the site would protect nobody.

**No residual risk is rated high. Prior consultation with the ICO (Article 36) is therefore not required**, and the
options (a) to (c) of the first draft fall away.

Two points stay worth knowing, because they are where a complaint would be argued:

1. The research safeguards (Article 84C) exclude processing "likely to cause substantial damage or substantial
   distress to a data subject". The controller's assessment, on the facts above, is that this processing is not
   likely to. A person who objects to their own value has the correction route, and using it for them is the
   practical answer to this point.
2. A name-guess column is still handled as special category data here (the legal basis recorded for it is
   research), because sorting people by a presumed religious background is treated in the ICO's guidance as
   processing that reveals religion, whatever the column is called. The rename makes the column accurate; it does
   not take it outside those rules.

## 5. Things to do before the site opens

1. ~~Accept OpenAI's DPA for the API account~~ Signed 24 November 2026 (risk 2). Zero retention: optional, ask.
2. ~~Settle the inconsistency under risk 3~~ Done 24 November 2026: a review key no longer gets report counts or flags.
3. ~~Decide on prior consultation~~ Not required: no residual risk is high.
4. ~~L1, L2, L3 and L4~~ Done 24 November 2026 (see section 4; to be checked in the browser).
5. ~~L5~~ Done 24 November 2026: the controller checked the sample in `accuracy_check/` directly, and the figures are on the
   name-guess columns' explainers.
6. Deployment security and a breach note (risk 8); name the host in the privacy notice.
7. Agree with the academic collaborator who is controller of what.
8. Take the ICO fee self-assessment again on opening day.

Later: the keyed hash (risk 6), the accuracy log (risk 4), the interest cards' confidence wording.

## 6. What was not examined

The data files themselves, beyond the accuracy check in `accuracy_check/` (a sample of election candidates and
donors with a name guess, each checked against public sources directly by the controller). The estimates about parliamentarians were not re-examined: the controller has checked the
"Likely not heterosexual" cases himself. OpenAI's and Resend's actual handling.

The paper's replication archive is frozen on purpose: it exists to reproduce the paper, so a correction made on
the site rightly does not reach it. Should a request ever concern the archive itself, the provision to read is the
research exemption from rectification (DPA 2018 Schedule 2 paragraph 27), which applies where changing the data
would seriously impair the research; that has not been needed and was not examined further.

## 7. Sign-off

| | |
|---|---|
| Measures in section 4 accepted | |
| Residual risks accepted, and by whom | |
| Confirmation that no residual risk is high, so no prior consultation with the ICO | |
| The hand check of every "Likely not heterosexual" case: when, and against what | |
| The accuracy check (`accuracy_check/`): the sample checked directly by the controller, and the figures published | Checked directly by the controller, 24 November 2026 (`accuracy_check/research/controller_review.json`) |
| Decision on the review key's report and flag counts (risk 3) | Withheld from ChatGPT; the server orders the comments. Decided 24 November 2026 |
| Signed and dated | |
| Next review | |
