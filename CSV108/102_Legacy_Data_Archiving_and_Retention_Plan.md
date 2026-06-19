---
document_number: QCL-2028-LAR-001
title: "Legacy Data Archiving and Retention Plan"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Retirement"
version: "1.0"
effective_or_record_date: "2028-03-31"
case_status: "Approved/Closed in fictional retirement record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Legacy System Owner"
reviewed_by: "Records Management Owner"
approved_by: "Site Quality Head"
---

# Legacy Data Archiving and Retention Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-LAR-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Retirement |
| Version | 1.0 |
| Effective/record date | 2028-03-31 |
| Case status | Approved/Closed in fictional retirement record |

## Governing references

- China GMP (2010 Revision), Appendix: Computerised Systems (effective 1 December 2015)
- China GMP (2010 Revision), Appendix: Qualification and Validation (effective 1 December 2015)
- EU GMP Annex 11: Computerised Systems (2011)
- EU GMP Annex 15: Qualification and Validation (2015)
- 21 CFR Part 11: Electronic Records; Electronic Signatures
- FDA Guidance: Part 11, Electronic Records; Electronic Signatures — Scope and Application
- PIC/S PI 041-1: Good Practices for Data Management and Integrity in Regulated GMP/GDP Environments (2021)
- ISPE GAMP 5, Second Edition (2022), used as non-binding industry guidance

## 1. Purpose

Define how Legacy LIMS records are retained, indexed, protected and disposed after retirement.

## 2. Retention mapping

| Record class | Retention decision | Repository/form |
|---|---|---|
| QC sample/test/result records | Mapped by product/batch retention category; minimum per approved GMP schedule | ArchiveVault package |
| Legacy audit trails | Same as associated record | Included in package and searchable |
| Attachments/scanned worksheets | Same as associated record | Binary + checksum + metadata |
| User/role history | System life + applicable investigation/record retention | Archive metadata/export |
| Legacy configuration/specification versions | System life + related record retention | Configuration export/eDMS |
| Interface logs/reconciliation | 2 years minimum; longer if linked to record/investigation | Archive log package |
| Validation/operation/retirement evidence | Per validation record schedule; dossier index permanent | eDMS |
| Final sealed system image | 90-day post-shutdown contingency, then secure destruction if approved | Offline encrypted vault |

## 3. Archive format

Each legacy package contains human-readable PDF/A or viewer-independent rendering, structured XML/JSON metadata, original attachments, audit-trail export, user/signature metadata and SHA-256 manifest. Proprietary database dependence is not required for routine retrieval.

## 4. Index and ownership

Search keys: Legacy Sample ID, QCLabOne migrated ID where applicable, batch, material/product, test, status, date range and archive package ID. Records Management owns archive administration; QC/QA owns content interpretation.

## 5. Legal hold and disposition

Before any archive purge or final system-image destruction, Records Management checks legal/regulatory/investigation holds. Destruction requires a separately approved record and does not occur solely because the application is retired.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | SOP-QA-ARC-001 | [Data Retention, Archiving and Record Retrieval SOP](070_Data_Retention_Archiving_and_Record_Retrieval_SOP.md) |
| Input | QCL-2028-ARC-001 | [System and Data Archive Record](097_System_and_Data_Archive_Record.md) |
| Input | QCL-2028-RRA-001 | [Legacy LIMS Retirement Risk Assessment](100_Legacy_LIMS_Retirement_Risk_Assessment.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Output | QCL-2028-DCL-001 | [Legacy System Decommissioning Checklist](105_Legacy_System_Decommissioning_Checklist.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Legacy System Owner | Completed |
| Reviewed by | Records Management Owner | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2028-03-31 | Initial approved fictional case version. |
