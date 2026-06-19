---
document_number: QCL-2026-DMP-001
title: "Data Migration Strategy and Plan"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Data Migration"
version: "1.0"
effective_or_record_date: "2026-10-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Data Migration Lead"
reviewed_by: "QC Data Owner"
approved_by: "QA CSV Lead"
---

# Data Migration Strategy and Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-DMP-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Data Migration |
| Version | 1.0 |
| Effective/record date | 2026-10-31 |
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

## 1. Migration objectives

Move active/required legacy data into QCLabOne and retain remaining historical records in ArchiveVault without loss of meaning, relationships, metadata, audit trail or retrievability.

## 2. Scope and disposition

| Source | Volume | Disposition |
|---|---|---|
| Legacy LIMS samples | 86,742 | 2018–cutover active/required records migrated; all records archived |
| Legacy LIMS results | 326,115 | Associated active records migrated; all results archived |
| Attachments | 24,806 | Migrated or archived with SHA-256 checksum |
| Active stability pulls | 1,984 | Migrated with schedules and history |
| Stability/reagent/EM spreadsheets | 12 controlled workbooks | Active data migrated after profiling; source preserved |
| Selected paper indexes | 3 indexes / 9,420 images | Index and approved image set archived; paper remains per retention |

## 3. Migration phases

1. Source freeze/profile.
2. Mapping and transformation approval.
3. Trial migration 1—technical completeness.
4. Cleansing and rule refinement.
5. Trial migration 2—business/UAT and performance.
6. Production extraction and freeze.
7. Load, reconciliation and exception disposition.
8. Business/QA acceptance.
9. Legacy read-only period and final archive verification.

## 4. Acceptance criteria

- Source/target counts reconcile 100% or have approved explained exclusions.
- Critical fields for migrated active records are checked 100%.
- A statistically justified sample of noncritical fields meets ≥99.5% accuracy, with no systemic defect.
- Attachments reconcile by count and checksum.
- Parent/child relationships and audit histories pass defined checks.
- No critical/high migration exception remains before go-live.

## 5. Security and source protection

Extraction uses read-only accounts and encrypted transfer. Source backups are retained. Production source is frozen during final migration except approved emergency transactions, which are separately reconciled.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Output | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-PDM-001 | [Production Data Migration Execution and Reconciliation Record](073_Production_Data_Migration_Execution_and_Reconciliation_Record.md) |
| Output | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Data Migration Lead | Completed |
| Reviewed by | QC Data Owner | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-31 | Initial approved fictional case version. |
