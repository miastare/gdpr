# Accuracy check of the name guesses for election candidates and donors (DPIA measure L5)

Run on 24 November 2026. **The sample was checked directly by Samuel Kinshuck (the controller) on 24 November 2026.** He checked each sampled person by hand. His note on one case: 'Tugendhat' is a Jewish name and the father was from a Jewish family, so as a guess of the religious background of the NAME the value 'Jewish' is right. The figures may be used as evidence.

Sample: 80 people with a religious-background guess, 8 drawn at random (seed 20261124) for each guessed value in each group. Donors: individuals in the Electoral Commission data who are not parliamentarians. Candidates: people who never sat, whose latest election was in 2010 or later, guessed from the name (the few guessed from a party's name are left out). Each was looked up in public sources under these rules:

For each person: find out, from public sources, whether their religion and gender can be stated with confidence.
- The default answer is "not_known". Most of these people are private individuals about whom little is published.
- "likely_correct" / "likely_wrong" for religion need a source that says it: the person's own statement, a reliable
  biography, profile, obituary or news report, or a role that settles it (an imam, a trustee of a named synagogue,
  a church minister). The verdict compares the source with OUR GUESS.
- Never infer religion from the name, from ethnicity or country of origin, from appearance, or from the party or
  cause supported. Those are what the guess already did.
- First be sure the person found is the same person (the party, seat, years or the recipient of the donation should
  fit). If that is not clear, the answer is "not_known" with identity "not_found" or "uncertain".
- Gender: "correct" / "wrong" when a source refers to the person as he or she, or shows it plainly; else "not_known".

Checked: 80 of 80.

## Religious background guessed from the name

### Donors

| Our guess | People | Not known | Likely correct | Likely wrong | Of those that could be checked, correct |
|---|---|---|---|---|---|
| Christian | 8 | 8 | 0 | 0 | none could be checked |
| Hindu | 8 | 7 | 0 | 1 | 0 of 1 |
| Jewish | 8 | 7 | 0 | 1 | 0 of 1 |
| Muslim | 8 | 7 | 1 | 0 | 1 of 1 |
| Sikh | 8 | 6 | 2 | 0 | 2 of 2 |
| all | 40 | 35 | 3 | 2 | 3 of 5 |

### Election candidates

| Our guess | People | Not known | Likely correct | Likely wrong | Of those that could be checked, correct |
|---|---|---|---|---|---|
| Christian | 8 | 7 | 1 | 0 | 1 of 1 |
| Hindu | 8 | 8 | 0 | 0 | none could be checked |
| Jewish | 8 | 8 | 0 | 0 | none could be checked |
| Muslim | 8 | 4 | 4 | 0 | 4 of 4 |
| Sikh | 8 | 6 | 2 | 0 | 2 of 2 |
| all | 40 | 33 | 7 | 0 | 7 of 7 |

### Both together

| Our guess | People | Not known | Likely correct | Likely wrong | Of those that could be checked, correct |
|---|---|---|---|---|---|
| Christian | 16 | 15 | 1 | 0 | 1 of 1 |
| Hindu | 16 | 15 | 0 | 1 | 0 of 1 |
| Jewish | 16 | 15 | 0 | 1 | 0 of 1 |
| Muslim | 16 | 11 | 5 | 0 | 5 of 5 |
| Sikh | 16 | 12 | 4 | 0 | 4 of 4 |
| all | 80 | 68 | 10 | 2 | 10 of 12 |

In words: of 80 people, the person's religion could not be established from public sources for 68 (85%); the guess was likely correct for 10 (12%) and likely wrong for 2 (2%). Among the 12 that could be checked, 83% were correct (95% interval 55% to 95%). The sample takes the same number from each guessed value, so the "all" rows are not weighted to the mix of values in the data; the population sizes are in `sample.json`.

The column is named for what it is, the guessed religious background of the NAME. Read that way, 2 of the 2 "likely wrong" cases are right about the name and the family, and wrong only about the religion the person states for themselves:

- Anish Kapoor: The guess (Hindu) matches the father's family background (Punjabi Hindu); he states a different religion himself (Jewish). Recorded on the same reasoning as Tugendhat.
- Michael Tugendhat: The guess (Jewish) matches the father's family background; he states a different religion himself (Catholic). The controller's note, 24 November 2026.

So, of the 12 people whose religion could be established: the guess matched the person's own stated religion for 10, and for the other 2 it matched the father's family background but not the religion the person states.

## Gender guessed from the name (the same sampled people)

A gender guess exists for 68 of the 80. Sources confirm it for 28, contradict it for 1, and say nothing clear for 39.

## The same rules where the answer is on record (no research needed)

The name rules were run on the election-record names of 10,462 parliamentarians, whose gender is recorded.

| Gender read from | Guesses | Right | Share right | 95% interval |
|---|---|---|---|---|
| given | 10,041 | 9,932 | 98.9% | 99% to 99% |
| title | 5 | 5 | 100.0% | 57% to 100% |
| all | 10,046 | 9,937 | 98.9% | 99% to 99% |

No gender guess could be made for 415 of 10,462 (4%).

Donors who are themselves parliamentarians (634), the name rule run on the name as recorded: a gender guess for 612, right for 611 (99.8%, 95% interval 99% to 100%).

Religion cannot be checked this way: a parliamentarian's religion on the site is itself an AI estimate, not a record. For what it is worth, where the name rule fires on a parliamentarian the two agree as follows.

| Name read as | Parliamentarians | AI estimate from the biography is the same | Share |
|---|---|---|---|
| Christian | 102 | 93 | 91% |
| Hindu | 11 | 8 | 73% |
| Jewish | 56 | 43 | 77% |
| Muslim | 37 | 32 | 86% |
| Sikh | 9 | 9 | 100% |

## What this does and does not show

- "Not known" is not an error. It means nothing public settles the person's religion, so the guess stands as a statement about the name and nothing more.
- The sample is small, so the shares are rough; the intervals say how rough.
- The findings about named people stay in this folder. Only the counts are for publication.
