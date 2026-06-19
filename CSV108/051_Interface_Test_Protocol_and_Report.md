---
document_number: QCL-2026-IFT-001
title: "Interface Test Protocol and Report"
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

# Interface Test Protocol and Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-IFT-001 |
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

Verify accurate, complete, secure and recoverable transfer of GxP data across SAP, eQMS, CDS/SDMS, instruments, identity and archive interfaces.

## 2. Interface test results

| Test ID | Test | Type | Result |
|---|---|---|---|
| IFT-SAP-001 | Inbound SAP sample request happy path | Interface | Pass |
| IFT-SAP-002 | Duplicate and malformed SAP message handling | Interface | Pass |
| IFT-SAP-003 | Outbound inspection status/result acknowledgement and reconciliation | Interface | Pass |
| IFT-EQM-001 | Create one OOS/OOT case and receive case ID/status | Interface | Pass |
| IFT-EQM-002 | Retry without duplicate eQMS case creation | Interface | Pass after DEF-003 |
| IFT-CDS-001 | Transfer approved result, unit, sequence ID, method version and link | Interface | Pass |
| IFT-CDS-002 | Reject unapproved or inconsistent CDS result | Interface | Pass |
| IFT-INS-001 | Instrument message source identity, unit and timestamp | Interface | Pass |
| IFT-INS-002 | Exception queue and authorized reprocessing | Interface | Pass |
| IFT-ALL-001 | Interface outage contingency entry and reconciliation | Interface | Pass |

## 3. Reconciliation results

| Interface | Messages sent | Accepted | Rejected/test exceptions | Unreconciled |
|---|---|---|---|---|
| SAP inbound/outbound | 2,540 | 2,510 | 30 intentional negative cases | 0 |
| eQMS | 118 | 112 | 6 intentional/timeout cases | 0 |
| CDS/SDMS | 1,024 | 1,010 | 14 intentional invalid/unapproved cases | 0 |
| Instruments | 3,600 | 3,540 | 60 intentional device/range/unit cases | 0 |
| Archive | 250 packages | 250 | 0 | 0 |

## 4. Deviations

DEV-003 addressed duplicate eQMS case creation during retry. Connector 1.4.1 introduced idempotency and lookup logic; repeat test passed. No production data was involved.

## 5. Conclusion

Interfaces preserve required values/context, detect failures and reconcile to zero unexplained messages. Interface controls are acceptable.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Input | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |

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
