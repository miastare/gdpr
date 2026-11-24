# Parliament Pulse — UK GDPR legal framework and justification

**Date:** 24 November 2026  
**Status:** Internal legal-position paper and proposed compliance framework; not a definitive legal opinion.

## 1. Executive summary

Parliament Pulse is an independent political research and data journalism project. Its purposes include studying British political institutions, political participation and funding, and differences in the representation of demographic groups in politics. It seeks to make both original research and the evidence supporting it accessible, credible and independently verifiable.

The proposed legal framework is:

| Ground | Legislation | Application |
| --- | --- | --- |
| Legitimate interests | UK GDPR Article 6(1)(f) | Ordinary personal data processing; also the Article 6 basis for qualifying sensitive-data research. |
| Scientific or historical research | UK GDPR Article 9(2)(j); Data Protection Act 2018 (DPA), Schedule 1, paragraph 4; UK GDPR Articles 84B–84C | Processing special category data for qualifying public-interest research, including research reproducibility, subject to statutory conditions. |
| Academic and journalistic purposes | DPA Schedule 2, paragraph 26; UK GDPR Article 85 | Exemption from specified GDPR obligations, including Articles 6 and 9, where applying them would be incompatible with the special purposes and the statutory tests are satisfied. Particularly relevant to identifiable publication. |
| Democratic transparency | Public-interest and legitimate-interests reasoning | Substantive justification supporting the above routes; not a freestanding GDPR exemption. |
| Equality of opportunity or treatment | Article 9(2)(g); DPA Schedule 1, paragraph 8 | Additional, narrower condition potentially relevant to qualifying equality research, not a general authority for the portal's public disclosures. |

**Proposed position:** rely on legitimate interests for ordinary political data, and Article 9(2)(j) for qualifying sensitive-data scientific research. Where identifiable publication is integral to academic or journalistic dissemination and ordinary GDPR requirements would prevent that publication, assess reliance on the special purposes exemption in paragraph 26. The exemption is provision-specific and processing-specific, not a general exemption for the organisation.

The key argument for retaining the portal's existing functionality is that **individual-level provenance is an integral, site-wide editorial and research principle, not a feature introduced specifically to expose sensitive characteristics**. The law does not require a particular interface or an aggregate-only journalism model. It does, however, require a defensible justification for the particular information disclosed.

## 2. Project and processing in scope

The following describes the project as represented by its operator:

- The portal covers parliamentarians, election candidates, political donors, people named in parliamentary interests declarations and related political records.
- Users can generate and share their own data visualisations and explore the observations underpinning those visualisations. The site does not offer bulk dataset downloads.
- Provenance is a core principle applied across the entire site, including ordinary non-sensitive information. For example, a historical count of eight Labour MPs for a modern constituency can be explored to identify those MPs, their periods of service and the external evidence (such as Wikidata) for the individual observations. Readers can follow the chain from an aggregate result to underlying records and their sources.
- For candidates, donors and comparable populations, inferred fields are labelled `Religion (name guess)` and `Gender (name guess)`.
- For parliamentarians, some religious classifications have been generated using GPT-4.1 with Wikipedia biographies as context. The current interface uses a red `! AI !` warning with a clickable explanation that the value is an AI guess and may be wrong.
- Unknown or missing data categories are already available. The operator is willing to introduce a mechanism for challenging data correctness.
- The project includes academic research in collaboration with a University of Manchester researcher. A manuscript intended for *Political Analysis* and its replication materials have been prepared. The operator reports that some inferred religion and sexuality variables for parliamentarians are relevant to the replication archive. Further academic research is intended.

The website's research purpose is distinct from using sensitive characteristics to target voters, campaign, make decisions about particular data subjects or determine their access to services. This distinction should remain true in practice. Public users' potential misuse of published information must nevertheless be considered.

## 3. Why the data falls within UK GDPR

UK GDPR Articles 4(1) and 4(2) cover identifiable living individuals and operations such as collecting, generating, analysing, storing and disclosing personal data. Under Article 9(1), data revealing religious beliefs, racial or ethnic origin, political opinions or sexual orientation are special category data. [1][2]

The ICO explicitly addresses inferences from names: deliberately inferring a sensitive characteristic can bring the processing within Article 9 even when confidence is low. [3]

| Information | Proposed compliance treatment |
| --- | --- |
| Names, parliamentary careers and ordinary biographical data | Personal data where they concern identifiable living people. |
| Name-based gender estimates | Usually ordinary personal data, unless the particular processing reveals a protected special category characteristic. |
| Name-based religion estimates | Treat conservatively as special category data because they are used as religion-related proxies in research on representation. |
| Biography-based AI religion estimates | Special category data: the model is being asked to infer personal religious beliefs. |
| Inferred sexuality | Special category data, with its own particularly sensitive disclosure and harm considerations. |
| Party affiliation and political donations | Special category data where they reveal political opinions; not every mention or donation necessarily establishes a person's beliefs. |
| Information concerning deceased persons | Generally outside UK GDPR in relation to the deceased, although it can also reveal information about living people. |

A name-based classification is not a verified fact about a person's beliefs. The statement that ten candidates received a particular name-based classification is different from the statement that ten candidates actually followed that religion. That distinction is important to the scientific interpretation and fairness of the data, but it is not by itself an exclusion from Article 9. An AI guess based on a biography is also not equivalent to the biography explicitly establishing the person's beliefs.

Article 9(2)(e) can sometimes apply to sensitive information that a person has deliberately made public themselves. A candidate's publicly declared party affiliation or a person's own explicit public statement of religion may qualify in appropriate circumstances. A publicly available name, Wikipedia article or statutory donation record does not automatically make any additional inference about that person manifestly public. [2][3]

## 4. Legitimate interests: Article 6(1)(f)

### What the law requires

The processing must be necessary for legitimate interests pursued by the controller or a third party, unless those interests are overridden by the data subject's interests or fundamental rights and freedoms. The ordinary assessment considers purpose, necessity and balancing. [4]

The newer recognised legitimate interests basis (Article 6(1)(ea)) is limited to prescribed purposes. General political transparency or research should not be assumed to qualify. [5]

### Parliament Pulse's justification

**Purpose.** Independent political research, public understanding of democracy, accountability of political institutions, scrutiny of political funding, investigation of demographic representation, and dissemination of research evidence are legitimate interests with wider public benefits.

**Necessity.** Individual political records are needed to link observations across datasets, distinguish people with similar names, verify dates and source material, correct mistakes, reproduce findings and enable the provenance functionality. Aggregate-only publication would not deliver the same ability to check the evidence. For sensitive variables, necessity must address the particular link between the identifiable person, the classification and the research or editorial objective, rather than relying solely on the site's general architecture.

**Balancing.** MPs' official roles, candidates' participation in elections, and publicly reported political funding create relevant public-interest considerations. However, public roles or statutory disclosures do not eliminate privacy interests in sensitive characteristics. The analysis should give additional weight to possible misclassification, unwanted disclosure, harassment and the different expectations of officeholders, candidates, donors and other people. Transparent provenance, explicit uncertainty, meaningful corrections and minimisation of unrelated data help reduce the impact.

Article 6(1)(f) alone does not authorise special category processing. Article 9 must also be satisfied unless a valid exemption applies.

## 5. Scientific and historical research: Article 9(2)(j)

### What the law requires

Article 9(2)(j), DPA section 10(2) and Schedule 1 paragraph 4 provide a route for necessary special category processing for scientific or historical research, statistics or public-interest archiving, subject to domestic-law requirements and safeguards. The Schedule 1 research condition requires necessity, compliance with Article 84B and a public-interest purpose. [2][6]

The Data (Use and Access) Act 2025 amended the UK GDPR's research provisions. The relevant current provisions include Article 4(2), which recognises scientific research regardless of whether it is commercially or publicly funded, and Articles 84B and 84C. The amendments took effect on 5 February 2026. [7]

Article 84B permits collection and anonymisation for research purposes, but requires other research processing to be essential to fulfilling the research purpose. Article 84C requires safeguards protecting individuals' rights and freedoms, including technical and organisational data-minimisation measures. The safeguards requirement is not satisfied if processing is likely to cause substantial damage or substantial distress, or is undertaken for measures or decisions about particular data subjects (apart from the specified medical research exception). [7][8]

The ICO's research guidance, updated on 18 November 2026, recognises social science, independent and commercial scientific research, and expressly includes research replication and reproducibility among qualifying activities. [9]

### Parliament Pulse's justification

The project seeks to undertake systematic political science research, including:

- Studying differences in representation between demographic groups among MPs and election candidates, and how those differences evolve over time.
- Investigating patterns of political funding and participation across demographic groups, parties and time periods.
- Examining relationships between demographic variables and parliamentary behaviour, where a sound research methodology supports this.
- Developing reusable research datasets, publishing findings and providing evidence needed to replicate, validate and extend those findings.

Individual-level research observations allow verification of linkage, classifications and source evidence. The need for provenance is especially acute with inferred variables: aggregate counts cannot reveal which observations were classified, whether the method behaves consistently, or how errors may affect a result.

The existing academic collaboration, manuscript and tested replication archive provide evidence of a genuine research programme. The public portal extends the dissemination of research beyond technically skilled specialists, allowing wider scrutiny of the evidence. These features support a scientific research purpose when the processing genuinely contributes to that purpose.

For internal analysis that does not require names, pseudonymisation or anonymisation should be considered. Identifiable source and classification records can be retained where they are needed for linkage or verification, subject to the statutory conditions. Publication must be assessed as a further processing operation: showing that names are needed to construct or verify a research dataset does not automatically show that all linked sensitive values need to be available without restriction.

### Scientific research is not the same as statistical purposes

Article 4(5) specifies anonymous aggregate results for processing undertaken for statistical purposes. Scientific research is a distinct statutory purpose and does not have that same blanket output definition. This distinction matters for academic publication and replication. It does not remove Article 84B–84C safeguards or the need to justify disclosure. [7][9]

The separate research-related rights exemptions in DPA Schedule 2 paragraph 27 have additional conditions, including an anonymous-output requirement. The project should not assume those rights exemptions merely because Article 9(2)(j) applies. [10]

## 6. Academic and journalistic purposes: Schedule 2 paragraph 26

### What the law requires

DPA Schedule 2, Part 5, paragraph 26 gives effect to the reconciliation of data protection and freedom of expression under UK GDPR Article 85. It covers one or more of journalistic, academic, artistic and literary purposes. [11]

The three central tests are:

1. **Paragraph 26(2)(a):** processing for the special purposes with a view to publishing academic or journalistic material.
2. **Paragraph 26(2)(b):** a reasonable belief that publication of the material would be in the public interest.
3. **Paragraph 26(3):** a reasonable belief that applying the particular GDPR provision would be incompatible with the special purposes, and exemption only to that extent.

Paragraph 26(4) requires particular consideration of the public interest in freedom of expression and information. Paragraph 26(5) requires regard, where relevant, to the specified editorial codes. Paragraph 26(9) lists the provisions that can be disapplied, including Articles 6 and 9 and certain other obligations and rights. It does not disapply the whole GDPR. [11][12]

A controller does not have to belong to an established media organisation to engage in journalism. The ICO's test is not whether it would make the same editorial decision, but whether the controller's belief is reasonable. Incompatibility must amount to more than inconvenience. The assessment should be made and documented at the time of the decision. [12]

### Test 1: Academic and journalistic publication

Parliament Pulse publishes political information, research and analysis with the purpose of informing the public. The public-facing interactive visualisations are themselves a means of communicating information and research, rather than merely an internal analytical tool. The ability for readers to generate and share analyses extends that dissemination.

The site also forms part of an active programme of academic research and reproducibility. The project's manuscript preparation, collaboration and replication work support a genuine academic publication purpose. The exemption is not dependent on acceptance of the manuscript or on every visualisation being part of a journal article. Each activity still needs to serve the relevant special purpose.

### Test 2: Public interest in publication

The public interest includes meaningful scrutiny of British political institutions, the representation of different demographic groups, access to political office, participation in political funding and patterns of parliamentary behaviour.

A further public interest is in the quality and credibility of political information itself. A reader should not have to accept the publisher's authority when assessing a claim: the reader should be able to examine the underlying evidence and judge the validity of the analysis. That capability helps expose inaccuracies, inconsistent methodology and misleading aggregate conclusions.

Providing accessible methods of verification also allows citizens without programming expertise or access to academic research facilities to participate in scrutiny. This is an important aspect of freedom to receive and communicate information.

The public interest is particularly clear for understanding elected representatives and candidates. For donors and other private individuals, the connection to the political activity and the contribution of the particular sensitive information to public understanding require distinct consideration. Inferred personal beliefs or sexuality are not inherently matters of public interest merely because a person is politically active.

### Test 3: Incompatibility and the core provenance principle

The portal's commitment to provenance is general and consistent: a numerical claim can be traced to the observations producing it and then to their sources. It is not a justification created specifically for sensitive-category datasets.

For example, if a visualisation shows that ten election candidates received a particular name-based religion classification, seeing the count alone cannot establish whether the classifier was applied consistently or whether the particular examples look reasonable. A reader cannot assess that question simply by being told that the publisher tested the model. Similar concerns arise with AI-based research variables for parliamentarians.

Publication of the methodology is necessary but does not always provide the same practical means of verification as inspection of the actual observations. The distinction is particularly important for model outputs that may be non-deterministic or dependent on the version of source material used. Independent users must be able to understand which observations contributed to a published result. The portal's academic and editorial argument is that this traceability is part of the publication itself.

If obtaining explicit consent from every person would materially undermine a representative historical dataset through nonresponse, selection bias and loss of observations, that is relevant to why ordinary consent-based processing might be incompatible with the research and publication. But consent is not the only Article 9 condition: the controller must consider whether scientific research or another applicable condition already permits the processing.

For **Article 9**, the proposed exemption argument is therefore that where no ordinary condition adequately permits the particular publication, disapplying the prohibition may be necessary to preserve the ability to disseminate and independently scrutinise research on group representation. For **Article 6**, ordinary legitimate interests should be retained where they work; any exemption from Article 6 needs its own incompatibility reasoning. Other obligations, such as transparency and corrections, should generally be retained unless their application actually conflicts with the special purpose.

The strength of this argument is that identifiability serves a specific evidential objective: it lets readers link research observations to the relevant original political records. The limitation is that different methods of verification offer different public benefits and privacy costs. Code, external sources, anonymised examples and independent audit should be considered as comparators. The operator can explain why they do not fully substitute for the intended public, accessible provenance functionality. They are not automatically required replacements.

The reasonable-belief assessment should distinguish the public interest in showing the actual output of a name classifier from the more intrusive disclosure of an unverified guess about an individual's actual beliefs. The latter raises different questions of relevance, reliability and consequences. A site-wide provenance policy is supporting evidence, not conclusive proof that every individual disclosure is justified.

No specific general legal entitlement to publish named, unverified AI religion estimates has been established by the sources reviewed. Paragraph 26 is the principal route for defending such publication where its actual statutory tests are satisfied; a warning or a declared editorial principle cannot substitute for those tests.

## 7. Equality of representation as an additional public-interest argument

Article 9(2)(g) and DPA Schedule 1 paragraph 8 concern necessary processing to assess equality of opportunity or treatment between specified groups with the aim of promoting or maintaining equality. The specified characteristics include racial or ethnic origin, religious or philosophical beliefs, health and sexual orientation. Paragraph 8 contains restrictions on individual decisions and processing likely to cause substantial damage or distress, and the Schedule 1 policy-document requirements apply where relevant. [13]

This is potentially relevant to targeted studies of barriers to political representation or participation. It is narrower than the project's whole remit: merely finding demographic correlations does not necessarily establish an equality-monitoring purpose. It is not the preferred route for defending public dissemination of identifiable sensitive estimates; the research and special purposes routes better address the stated objectives.

## 8. Proportionate improvements while preserving the site's functionality

These are functional and editorial requirements, not proposed UI designs. The site has not been inspected and no particular layout, component or wording beyond illustrative examples is prescribed.

| Improvement | Rationale |
| --- | --- |
| Keep concise and explicit inferential labels, such as the existing `Religion (name guess)` and `Gender (name guess)`. | A reader should recognise that the data records a classification rather than a verified personal fact. |
| Retain the existing AI warning for biography-based estimates, and ensure its meaning is readily apparent wherever the value is used. | The distinction between sourced fact and model output should not disappear in a different presentation context. |
| Preserve the status of a variable in generated and shared visualisations. | A chart shared outside the original page should not inadvertently turn an estimated distribution into a claim about verified religious beliefs. A concise legend, note or equivalent can achieve this. |
| Make the evidential chain clear, including method, source and relevant version or date where practicable. | A Wikipedia page used as model input is not necessarily evidence confirming its output. Name guesses should be traceable to the input and actual classification, not represented as statements sourced from an external biography. |
| Keep the existing unknown/missing categories. | Avoid false precision, distinguish unavailable information from a positive classification and account for missing observations in reported results. |
| Introduce an accessible correction and challenge mechanism. | Enable people to dispute facts or estimates, correct errors and record the outcome, distinguishing a correction to an input record from a challenge to an inference. |
| Document and evaluate research methodology. | Describe validation, error rates or uncertainty where evidence permits, differential bias across groups and limitations of religion-related and gender-related proxies. Do not invent precision or claim that a proxy establishes actual beliefs. |
| Maintain appropriate technical and organisational security and minimise unrelated personal data. | Protect non-public research records, user accounts and internal systems; the public purpose does not justify collecting or retaining unrelated personal details. |
| Set clear terms against harassment, discriminatory targeting and other misuse, and provide a way to report it. | Address foreseeable harmful uses while preserving legitimate exploration. Terms are supplementary safeguards, not a guarantee against misuse. |

Illustrative short explanatory text, if useful in the existing interface:

- Name-based religion: “Estimated from the name alone; may reflect naming traditions rather than actual religious beliefs.”
- Biography-based AI religion: “AI-generated estimate using Wikipedia as context. Not independently verified; may be incorrect.”

The ICO distinguishes the status of an AI inference from factual accuracy and expects its limitations to be communicated. Statistical accuracy remains a separate research question. [14]

The project already has no bulk-download functionality, which is relevant to its design and reduces one route to mass redistribution. It does not prevent scraping or misuse, nor does it establish lawfulness by itself. This paper does not propose eliminating ordinary drill-down, chart generation or chart sharing, adding mandatory researcher registration, or converting the portal into an aggregate-only product. It does not establish that every existing sensitive display can lawfully remain unchanged: that depends on the actual evidence and impact of the individual disclosure.

## 9. Compliance work outside the interface

The following work supports the proposed legal position without itself requiring a redesign of the portal:

1. **Record the purposes and legal grounds.** Maintain a processing register mapping ordinary records, research inference, academic replication, interactive publication and user-account processing to their applicable grounds. Record the legitimate interests balancing exercise, the Article 9(2)(j) assessment and the paragraph 26 reasonable-belief reasoning for particular requirements. The exemption should not be used by default for unrelated administrative activities.
2. **Complete a DPIA under Article 35.** The combination of systematic inference, sensitive information, potential large-scale processing and public disclosure makes a high-risk assessment particularly important. Article 35 is not listed among the paragraph 26 exemptions. Consider the different populations and variables, risks of misidentification, harassment, stigma or outing, and residual risk after safeguards. A DPIA is an internal assessment, not a requirement to seek routine pre-approval from the regulator. Article 36 normally governs consultation where residual high risk remains; paragraph 26 lists Article 36 as potentially exempt only where the specific tests are met. [11][15]
3. **Maintain a privacy notice and rights process.** Article 14 normally requires information where data is collected or generated indirectly, including public-source information. A disproportionate-effort exception may be available on its conditions, with suitable safeguards and public notice; a website privacy notice alone is not automatically sufficient. Paragraph 26 may also exempt some transparency or rights obligations where justified. Retain a meaningful correction route regardless of whether a particular statutory right is exempt. [16]
4. **Check controller and provider arrangements.** Establish whether the project and academic collaborators are separate or joint controllers (Article 26), and assess the terms, security, processor status and any applicable transfer requirements for the AI service used to process biographies (Articles 28, 32 and Chapter V). Verify what actually happens to submitted data rather than assuming that use of publicly available biographies removes these obligations.
5. **Record research evidence and replication requirements.** Keep dated methodology documents, manuscript drafts, correspondence, data availability statements and relevant licensing permissions. The *Political Analysis* replication policy is useful supporting evidence, but permits exceptions and does not override privacy law. [17]
6. **Apply an editorial process and review.** Keep a dated record of the public-interest objectives, alternatives considered, relevant harms and decisions for each class of sensitive disclosure, and review when the methodology, population, display or use changes. Apply relevant editorial accuracy and privacy standards. [12][18]

The project should retain accountability, appropriate security and other GDPR duties not covered by a specific exemption. GDPR compliance also does not settle any independent questions involving misuse of private information, defamation, confidentiality, source licences or other applicable law.

## 10. Proposed statement of justification (for adoption if factually accurate)

> Parliament Pulse is an independent political science research and data journalism initiative. Its purpose is to improve understanding of British political institutions, political participation, political funding and political behaviour, with a particular interest in studying how different demographic groups are represented in political life.
>
> The project conducts and supports original academic research, develops research datasets, disseminates findings and facilitates independent replication. Its public portal allows readers to explore political data and generate and share visualisations of that data.
>
> A fundamental principle of Parliament Pulse is the traceability of published information. Across the site, users can examine the individual observations contributing to aggregate results and follow the evidential chain to the relevant underlying sources. This principle applies equally to ordinary political records and to research variables derived through computational methods. It is intended to allow users to verify findings independently, rather than requiring them to trust the publisher's conclusions.
>
> This is especially important for research involving inferred classifications. An aggregate result cannot on its own establish that the classifications producing it are reasonable, consistently applied or free from methodological bias. The ability to examine the underlying observations therefore contributes to the scientific and journalistic value of publication and enables meaningful public scrutiny.
>
> The project distinguishes inferred classifications from verified information. Name-based classifications are estimates derived from names, not statements establishing actual beliefs or identities. AI-generated classifications based on biographical context are identified as estimates and may be incorrect. Unknown values are permitted. The project seeks to make sources, methods and limitations clear and to facilitate challenges and corrections.
>
> The project considers that its research and publication activities advance legitimate interests in democratic transparency, independent research, public understanding, equality of representation and freedom of expression and information. It relies on Article 6(1)(f) for processing where the legitimate interests test is met, and Article 9(2)(j), together with Schedule 1 paragraph 4 of the Data Protection Act 2018, for qualifying special category research subject to the statutory safeguards.
>
> The project also processes personal data with a view to publishing academic and journalistic material. Where it reasonably believes that publication is in the public interest and that application of a particular listed GDPR provision would be incompatible with those special purposes, it relies on Schedule 2 paragraph 26 of the Data Protection Act 2018 only to the extent that its requirements are satisfied. The project gives particular weight to freedom of expression and information, the evidential value of individual-level provenance, and the public interest in research on demographic representation in British politics.
>
> In applying these grounds the project considers the relevance, accuracy, necessity and impact of particular processing and disclosures, including the different privacy interests of parliamentarians, candidates, donors and other individuals. It maintains appropriate safeguards and documents the reasons for its decisions.

## 11. References

All references below are public online sources. Statutory references are to UK law, including amendments made by the Data (Use and Access) Act 2025. The ICO guidance is regulatory interpretation rather than legislation.

[1] [UK GDPR, Article 4 — Definitions](https://www.legislation.gov.uk/eur/2016/679/article/4).

[2] [UK GDPR, Article 9 — Processing of special categories of personal data](https://www.legislation.gov.uk/eur/2016/679/article/9); [ICO — What are the conditions for processing?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-conditions-for-processing/).

[3] [ICO — What is special category data? (including inferences)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/).

[4] [UK GDPR, Article 6 — Lawfulness of processing](https://www.legislation.gov.uk/eur/2016/679/article/6); [ICO — Legitimate interests](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/legitimate-interests/).

[5] [ICO — Recognised legitimate interest](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/recognised-legitimate-interest/).

[6] [DPA 2018, section 10](https://www.legislation.gov.uk/ukpga/2018/12/section/10); [DPA 2018, Schedule 1, paragraph 4](https://www.legislation.gov.uk/ukpga/2018/12/schedule/1/paragraph/4).

[7] [Data (Use and Access) Act 2025, Part 5](https://www.legislation.gov.uk/ukpga/2025/18/part/5); [Section 86 — Research safeguards](https://www.legislation.gov.uk/ukpga/2025/18/section/86); [UK GDPR, Chapter 8A — Research, archives and statistics](https://www.legislation.gov.uk/eur/2016/679/chapter/8A).

[8] [ICO — What requirements and safeguards must we have in place?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/what-requirements-and-safeguards-must-we-have-in-place/); [ICO — How do the RAS provisions affect the principles and grounds for processing?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/how-do-the-ras-provisions-affect-the-principles-and-grounds-for-processing/).

[9] [ICO — Research, archiving and statistics provisions (updated November 2026)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/); [ICO — What is processing for RAS purposes?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/what-is-processing-for-ras-purposes/).

[10] [DPA 2018, Schedule 2, paragraph 27](https://www.legislation.gov.uk/ukpga/2018/12/schedule/2/paragraph/27); [ICO — What are the exemptions for research?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/what-are-the-exemptions-for-research/).

[11] [DPA 2018, Schedule 2, paragraph 26 — Special purposes exemption](https://www.legislation.gov.uk/ukpga/2018/12/schedule/2/paragraph/26); [UK GDPR, Article 85 — Freedom of expression and information](https://www.legislation.gov.uk/eur/2016/679/article/85).

[12] [ICO — Guide to data protection exemptions (journalism, academia, art and literature)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/exemptions/a-guide-to-the-data-protection-exemptions/); [ICO — Data protection and journalism code of practice, particularly its discussion of the exemption](https://ico.org.uk/media/for-organisations/documents/4025760/data-protection-and-journalism-code-202307.pdf).

[13] [DPA 2018, Schedule 1, paragraph 8](https://www.legislation.gov.uk/ukpga/2018/12/schedule/1/paragraph/8); [ICO — Substantial public interest conditions](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-substantial-public-interest-conditions/).

[14] [ICO — Accuracy and statistical accuracy in AI](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/what-do-we-need-to-know-about-accuracy-and-statistical-accuracy/).

[15] [UK GDPR, Article 35 — Data protection impact assessment](https://www.legislation.gov.uk/eur/2016/679/article/35); [Article 36 — Prior consultation](https://www.legislation.gov.uk/eur/2016/679/article/36).

[16] [UK GDPR, Article 14 — Information where personal data has not been obtained from the data subject](https://www.legislation.gov.uk/eur/2016/679/article/14); [Article 16 — Rectification](https://www.legislation.gov.uk/eur/2016/679/article/16); [Article 21 — Objection](https://www.legislation.gov.uk/eur/2016/679/article/21).

[17] [Political Analysis — Preparing your materials](https://www.cambridge.org/core/journals/political-analysis/information/author-instructions/preparing-your-materials); [Research transparency policy](https://www.cambridge.org/core/journals/political-analysis/information/journal-policies/research-transparency).

[18] [IPSO — Editors' Code of Practice](https://www.ipso.co.uk/editors-code-of-practice/), particularly clauses 1 (accuracy), 2 (privacy) and 12 (discrimination), where relevant.

### Evidence and limitations

The description of Parliament Pulse is based on the operator's account. The website, individual classification records, underlying methodology, scale of disclosures, provider arrangements and actual user access have not been audited. Earlier review of correspondence with the academic collaborator corroborated the manuscript and replication work, but did not independently establish a requirement to release every sensitive variable in identifiable form. This paper therefore provides a proposed legal rationale and practical compliance framework, not a finding that the statutory conditions are met or a completed DPIA. The remaining issue is the reasonableness and proportionality of the actual processing and disclosure, particularly biography-based sensitive guesses. A review of that evidence by a UK data protection specialist or the academic collaborator's data protection team would help establish the final documented position.
