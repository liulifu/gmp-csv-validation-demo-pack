# GMP CSV Validation Demo Pack

A realistic, end-to-end **Computerized System Validation (CSV)** demo package for a GMP laboratory system.

This repository provides 108 example lifecycle documents for a fictional QC laboratory digital platform replacement project, including both editable Markdown sources and polished Word `.docx` files. It is designed for learning, benchmarking, and drafting reference material for regulated GxP software validation work.

> This is a fictional training/demo package. It is not approved GMP evidence, legal advice, regulatory advice, or a substitute for your company's SOPs, templates, quality approval, supplier evidence, or validation execution.

## What This Is

In pharmaceutical and biotech companies, this type of package is often described as a:

- CSV lifecycle document pack
- GxP computerized system validation package
- validation deliverables pack
- validation evidence starter kit
- LIMS/LES validation demo package

The demo scenario is **QCLabOne 2.0**, a fictional QC laboratory LIMS/LES replacement project covering project initiation, GxP assessment, supplier oversight, URS/design, IQ/OQ/PQ, traceability, go-live, operation, periodic review, and legacy system retirement.

## Why It Exists

CSV documentation is usually hard to learn from public examples because real packages are confidential. This repository gives students, QA/CSV engineers, validation consultants, product teams, and regulated-software builders a concrete reference set that shows how lifecycle deliverables can connect across one coherent system story.

Use it to:

- understand what a full CSV lifecycle can look like
- study traceability between requirements, risks, verification records, deviations, SOPs, and retirement records
- bootstrap internal discussions about validation deliverables
- compare your own templates against a complete fictional example
- review both Markdown and Word versions of the same example package

## Included Documents

The package contains 108 lifecycle documents, including:

- CSV lifecycle procedure and validation master plan
- computerized system inventory
- project charter, scope, intended use, and business process description
- GxP impact, system classification, preliminary risk, data integrity, Part 11 / Annex 11, cybersecurity and privacy assessments
- supplier qualification, audit, agreement, and documentation leveraging records
- URS, functional/design/configuration/interface/data/report/master-data specifications
- role/access, audit trail, electronic signature, backup/restore, BCP/DR, data migration, and functional risk documents
- IQ/OQ/PQ, interface, migration, security, audit trail, e-signature, backup, performance, DR, and report verification records
- defect, deviation, CAPA, test summary, RTM, and VSR records
- SOPs, training, cutover, go-live, handover, production baseline, access reviews, audit trail reviews, incidents, changes, periodic review, supplier review, archive records
- legacy LIMS retirement and final validation dossier index

## Repository Layout

```text
CSV108/
  001_...md through 108_...md
  Markdown source files with front matter and linked lifecycle content.

CSV108_docx/
  001_...docx through 108_...docx
  Polished Word versions of the same documents.
```

## Quick Start

Clone the repository:

```bash
git clone https://github.com/liulifu/gmp-csv-validation-demo-pack.git
cd gmp-csv-validation-demo-pack
```

Open the ready-made Word files:

```text
CSV108_docx/
```

Or read/edit the Markdown sources:

```text
CSV108/
```

## Privacy And Fictional Data

The documents are written as a fictional training case. A local scan of the Markdown sources found no real emails, phone numbers, ID numbers, passport numbers, IP addresses, bank/card numbers, employee IDs, real user IDs, or natural-person names.

Some documents discuss privacy-related concepts such as employee name, corporate ID, user/signature metadata, named accounts, service accounts, and user activity. These are data-category descriptions, not real personal data values.

## Important Compliance Boundary

Do not use these documents as-is for production GMP validation.

Before adapting any content, replace fictional company, system, supplier, date, role, evidence, test, and approval details. Align every document with your approved quality system, applicable regulations, supplier evidence, risk decisions, data integrity expectations, and document-control process.

Typical adaptation work includes:

- replacing fictional project details with your own system and site context
- mapping document owners and approvers to actual job roles
- aligning terminology with company SOPs
- updating regulatory references for your market
- replacing demo evidence IDs with real objective evidence
- reviewing every risk rating, control, test, deviation, and conclusion
- obtaining formal QA and business approval before use

## Who May Find This Useful

- CSV engineers and validation specialists
- QA validation managers
- LIMS/LES product teams
- pharmaceutical IT and quality teams
- consultants building starter examples
- students learning GAMP 5-style lifecycle thinking
- founders building regulated life-science software

## License

MIT. See [LICENSE](LICENSE).

## Star The Project

If this saves you time or helps you explain CSV work to someone else, a star helps other validation and regulated-software people find it.
