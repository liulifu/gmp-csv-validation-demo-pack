---
document_number: QCL-2026-OQ-001
title: "Operational Qualification Protocol and Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Verification"
version: "1.0"
effective_or_record_date: "2027-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "Business Process Owner"
approved_by: "QA Validation Manager"
---

# Operational Qualification Protocol and Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-OQ-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Verification |
| Version | 1.0 |
| Effective/record date | 2027-04-30 |
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

## 1. Objective

OQ challenged configured functional behaviour, including negative and boundary conditions, against approved URS, specifications and FRA controls.

## 2. Executed OQ cases

| Test ID | Test | Type | Result |
|---|---|---|---|
| OQ-SMP-001 | Create SAP-origin sample request; generate sample ID and barcode | OQ | Pass |
| OQ-SMP-002 | Record receipt, reject, transfer, aliquot and disposal with custody history | OQ | Pass |
| OQ-SMP-003 | Assign tests from effective specification and block closure with open work | OQ | Pass |
| OQ-SMP-004 | Calculate stability pull date and overdue alert | OQ | Pass |
| OQ-SPEC-001 | Create, approve, effective-date and obsolete a specification | OQ | Pass |
| OQ-SPEC-002 | Confirm historical record retains original specification/method version | OQ | Pass |
| OQ-SPEC-003 | Verify numeric, qualitative, text and enumerated result types | OQ | Pass |
| OQ-LES-001 | Execute approved LES steps and enforce prerequisites/mandatory fields | OQ | Pass |
| OQ-LES-002 | Capture reagent, standard, instrument and lot references | OQ | Pass |
| OQ-LES-003 | Direct capture from balance, pH meter and TOC analyzer | OQ | Pass |
| OQ-LES-004 | Manual entry reason and independent verification | OQ | Pass |
| OQ-LES-005 | Pause, abort, repeat-test and exception dashboard | OQ | Pass |
| OQ-LES-006 | Prevent analyst self-approval | OQ | Pass |
| OQ-CALC-001 | Verify assay and dilution formula calculations | OQ | Pass |
| OQ-CALC-002 | Verify significant figures, rounding and boundary limits | OQ | Pass |
| OQ-CALC-003 | Verify formula history and controlled change | OQ | Pass |
| OQ-SEC-001 | Verify SSO, unique account and disabled local login | OQ | Pass |
| OQ-SEC-002 | Verify positive/negative permissions for each business role | OQ | Pass |
| OQ-SEC-003 | Verify session lock and account disablement | OQ | Pass |
| OQ-SEC-004 | Verify vendor remote access approval, timeout and logging | OQ | Pass |
| OQ-DI-001 | Verify system time synchronization and timezone control | OQ | Pass |
| OQ-DI-002 | Verify record retention and routine deletion restrictions | OQ | Pass |
| OQ-OPS-001 | Generate access, audit trail, backup and operational reports | OQ | Pass |
| OQ-GEN-001 | Verify application/environment/version display | OQ | Pass |
| OQ-GEN-002 | Verify unique identifier non-reuse and production baseline control | OQ | Pass |

## 3. Representative actual results

- Duplicate sample ID and self-approval attempts were rejected.
- Historical specifications remained unchanged after a new version became effective.
- Formula outputs matched independent references, including rounding and limit boundaries.
- Manual critical result required reason and independent verification.
- Local interactive login was disabled; session lock occurred at 15 minutes.
- Routine users could not delete GxP records.
- Required operational reports were generated.

## 4. Exceptions

Audit trail-specific configuration failure was managed under DEV-001 and retested in Document 054. No other unresolved OQ issue remained.

## 5. Conclusion

All planned OQ cases passed after controlled correction/retest. Configured functions are suitable to proceed to PQ/UAT.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-RCS-001 | [Report and Calculation Specification](029_Report_and_Calculation_Specification.md) |
| Input | QCL-2026-MDS-001 | [Master Data Specification](030_Master_Data_Specification.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Input | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-PQ-001 | [Performance Qualification and User Acceptance Test Report](050_Performance_Qualification_and_UAT_Report.md) |
| Output | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-04-30 | Initial approved fictional case version. |
