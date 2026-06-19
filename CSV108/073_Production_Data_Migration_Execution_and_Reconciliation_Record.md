---
document_number: QCL-2026-PDM-001
title: "Production Data Migration Execution and Reconciliation Record"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Release"
version: "1.0"
effective_or_record_date: "2027-06-15"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "Site Quality Head"
---

# Production Data Migration Execution and Reconciliation Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-PDM-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Release |
| Version | 1.0 |
| Effective/record date | 2027-06-15 |
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

## 1. Execution window

Final extraction began 2027-06-14 18:32 CST. Load completed 2027-06-15 02:18. Reconciliation and business verification completed 06:25.

## 2. Production reconciliation

| Data set | Source count | Target/archive count | Difference/disposition | Result |
|---|---|---|---|---|
| Legacy sample records | 86,742 | 86,742 | 0 | 100% |
| Legacy result records | 326,115 | 326,115 | 0 | 100% |
| Attachments | 24,806 | 24,806 | 0; 312 names normalized with original metadata retained | 100% hashes match |
| Active stability pulls | 1,984 | 1,984 | 0 | 100% |
| Controlled spreadsheet active rows | 14,228 | 14,224 | 4 approved exclusions: cancelled duplicate rows | 100% explained |
| Legacy audit events in archive | 1,482,610 | 1,482,610 | 0 | 100% |
| Archive record packages | 112,604 | 112,604 | 0 | 100% manifest/checksum |

## 3. Critical-field verification

All migrated active records were automatically checked for Sample ID/legacy reference, material, batch, test, result, unit, status, specification/method version, source record, approval metadata and relationships. A business sample of 500 records was independently compared; no mismatch was found.

## 4. Exceptions

Four cancelled duplicate spreadsheet rows were excluded under approved EXC-MIG-017 and retained in the source archive. No critical/high exception remained. Filename normalization followed MAP-2.3 and preserved original names.

## 5. Acceptance

QC Data Owner, Migration Lead, Records Management and QA accepted the production migration at 07:05 CST. Legacy LIMS remained read-only for verification/retirement.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Input | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Input | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Input | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Input | QCL-2026-CUT-001 | [Cutover, Rollback and Contingency Plan](072_Cutover_Rollback_and_Contingency_Plan.md) |
| Output | QCL-2026-PRC-001 | [Production Readiness Checklist](074_Production_Readiness_Checklist.md) |
| Output | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |
| Output | QCL-2028-ARC-001 | [System and Data Archive Record](097_System_and_Data_Archive_Record.md) |
| Output | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-06-15 | Initial approved fictional case version. |
