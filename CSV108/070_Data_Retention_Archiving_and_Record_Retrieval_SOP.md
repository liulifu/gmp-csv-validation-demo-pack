---
document_number: SOP-QA-ARC-001
title: "Data Retention, Archiving and Record Retrieval SOP"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "SOP and Training"
version: "1.0"
effective_or_record_date: "2027-05-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Training/Procedure Owner"
reviewed_by: "System Owner"
approved_by: "QA Department Head"
---

# Data Retention, Archiving and Record Retrieval SOP

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | SOP-QA-ARC-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | SOP and Training |
| Version | 1.0 |
| Effective/record date | 2027-05-31 |
| Case status | Approved in fictional case |

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

This SOP controls retention, archive transfer, integrity verification, authorised retrieval and final disposition of QCLabOne and Legacy LIMS records.

## 2. Retention schedule

| Record class | Retention rule | Repository | Owner |
|---|---|---|---|
| Approved QC sample/test/result record | Product/batch retention requirement; at least 1 year after expiry unless longer rule applies | QCLabOne then ArchiveVault | QC Records Owner |
| Audit trail and electronic signature | Same as associated record | With record package | QA Data Integrity |
| Specification/method/calculation version | Effective life plus related record retention | QCLabOne/eDMS archive | QC Master Data Owner |
| OOS/OOT link and local summary | Same as related test/investigation | QCLabOne + eQMS | QA |
| Interface messages/reconciliation | 2 years online; longer when linked to record/incident | Log/archive repository | System Owner |
| Access/change/incident/backup evidence | System life + 2 years or longer if related to GMP investigation | eQMS/eDMS | System Owner/QA |
| Legacy LIMS archive | Original required retention by record class | ArchiveVault read-only | Records Management |
| Validation/retirement dossier index | Permanent index; evidence per applicable schedule | eDMS | QA Validation |

## 3. Archive package

A package contains PDF/A rendering where applicable, structured metadata/data, attachments, audit trail, signature manifestation, version references and SHA-256 manifest. Transfer is reconciled and the archive is read-only.

## 4. Retrieval

Authorised users search by sample ID, batch, material, date, test and legacy reference. Retrieval records requester, purpose and date. Inspection requests receive complete readable copies without altering originals.

## 5. Archive verification

Before source deletion or retirement, verify package counts/checksums, metadata relationships, sample retrieval, audit trail, attachments and signature context. Failures require incident/deviation and prevent decommissioning.

## 6. Disposition

No routine user can purge records. Final deletion after retention requires Records Management and Quality approval, legal-hold check, documented list, secure deletion evidence and inventory update.

## 7. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Input | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | QCL-2028-ARC-001 | [System and Data Archive Record](097_System_and_Data_Archive_Record.md) |
| Output | QCL-2028-IRD-001 | [Inspection Readiness Dossier and Audit Response Record](098_Inspection_Readiness_Dossier_and_Audit_Response_Record.md) |
| Output | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Training/Procedure Owner | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Department Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-05-31 | Initial approved fictional case version. |
