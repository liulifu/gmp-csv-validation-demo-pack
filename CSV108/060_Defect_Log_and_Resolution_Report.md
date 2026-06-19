---
document_number: QCL-2026-DEF-001
title: "Defect Log and Resolution Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Test Management"
version: "1.0"
effective_or_record_date: "2027-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# Defect Log and Resolution Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-DEF-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Test Management |
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

## 1. Purpose

This log records validation defects, resolution, retest and closure.

## 2. Defect register

| ID | Phase | Severity | Description | Cause area | Resolution | Final status |
|---|---|---|---|---|---|---|
| DEF-001 | OQ | Medium | Audit trail reason not mandatory when changing sample comment classified as critical metadata | Configuration | Changed event classification and mandatory reason rule | Closed; retest ATC-002/003 pass |
| DEF-002 | Migration | Medium | Attachment names containing `:` and `*` failed target import | Migration transform | Normalize storage filename and retain original in metadata | Closed; DMT-003 pass |
| DEF-003 | Interface | Medium | eQMS retry after timeout could create a duplicate case | Custom code | Add idempotency key and response lookup before retry | Closed; UT/IFT-EQM-002 pass |
| DEF-004 | Report | Low | Long method name wrapped over signature footer on one PDF page | Template | Adjusted layout and regression set | Closed; RPT-003 pass |
| DEF-005 | PQ | Low | Overdue stability dashboard sorted text dates incorrectly in Chinese locale | Configuration | Use ISO date sort field | Closed; PQ-004 retest pass |
| DEF-006 | SAT | Low | One barcode printer used outdated driver | Installation | Installed approved driver and reverified | Closed |

## 3. Trend conclusion

Six defects were identified: zero Critical/High, three Medium and three Low. All were corrected and retested before release. No repeated systemic failure remained.

Defect closure requires root cause, affected requirement/test, correction, regression or no-regression rationale, retest evidence and QA disposition where GxP impact is possible. A defect is release blocking when it prevents intended use, compromises data integrity, prevents inspection retrieval, creates an incorrect quality decision or invalidates a required control.

| Defect decision point | Required disposition |
|---|---|
| Critical/High defect | Release blocked until corrected or formally risk accepted by QA leadership |
| Medium defect | Corrected or residual risk accepted with workaround and owner |
| Low defect | Corrected or accepted with no GxP/data-integrity impact |
| Repeated defect theme | Trend/root-cause review and CAPA consideration |
| Retest evidence | Original failure, correction and passing evidence remain linked |

## 4. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Input | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Input | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Input | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Input | QCL-2026-PQ-001 | [Performance Qualification and User Acceptance Test Report](050_Performance_Qualification_and_UAT_Report.md) |
| Input | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Input | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Input | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Input | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Input | QCL-2026-RPT-001 | [Report, Print and Export Verification Report](059_Report_Print_and_Export_Verification_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-04-30 | Initial approved fictional case version. |
