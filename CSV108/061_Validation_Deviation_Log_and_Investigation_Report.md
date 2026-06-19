---
document_number: QCL-2026-DEV-001
title: "Validation Deviation Log and Investigation Report"
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

# Validation Deviation Log and Investigation Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-DEV-001 |
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

This record documents protocol deviations and their GxP impact, corrective action, retest and closure.

## 2. Deviation register

| ID | Affected test | Description | Class | Impact assessment | Action/retest | Status |
|---|---|---|---|---|---|---|
| DEV-001 | ATC-002/003 | Audit-trail reason configuration failed expected result | Medium | No production data; validation environment only. Risk to detectability if unresolved. | Config corrected under controlled build; affected audit tests repeated plus regression | Closed 2027-04-08 |
| DEV-002 | DMT-003 | 24 attachment filenames failed due to unsupported characters | Medium | Binary content intact in source; potential migration incompleteness. | Mapping rule updated; all affected files reloaded and hash checked | Closed 2027-04-12 |
| DEV-003 | IFT-EQM-002 | Initial retry test generated duplicate sandbox case | Medium | No production data; could create duplicate investigation. | Connector fix 1.4.1, unit retest, interface retest and case cleanup | Closed 2027-04-15 |
| DEV-004 | PLC-001 | Response time exceeded target for stability dashboard at 200 users | Low | No correctness/data-integrity impact; usability delay only. | Added index/cache; repeated load test met target | Closed 2027-04-20 |

## 3. Closure criteria

Each deviation has defined scope, preserved original evidence, root-cause evaluation, impact on other tests/requirements, corrected evidence and independent QA closure. No retrospective alteration of original test results occurred.

## 4. Conclusion

Four validation deviations were closed. None involved production data or created unaddressed residual risk.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Input | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Input | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Input | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Input | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Input | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |
| Output | QCL-2026-CAPA-001 | [CAPA Record and Effectiveness Check](062_CAPA_Record_and_Effectiveness_Check.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
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
