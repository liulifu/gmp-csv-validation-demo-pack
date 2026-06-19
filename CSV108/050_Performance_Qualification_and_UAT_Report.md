---
document_number: QCL-2026-PQ-001
title: "Performance Qualification and User Acceptance Test Report"
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

# Performance Qualification and User Acceptance Test Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-PQ-001 |
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

## 1. Objective and users

PQ/UAT demonstrated fitness for intended use through representative end-to-end GMP scenarios. Twenty-four trained users participated: 12 analysts, 5 reviewers, 3 supervisors, 2 QA reviewers, 1 master-data steward and 1 system administrator.

## 2. Executed scenarios

| Test ID | Process | End-to-end scope | Result |
|---|---|---|---|
| PQ-001 | Raw material workflow | SAP request → receive → direct balance capture → calculation → review/approve → SAP status | Pass |
| PQ-002 | Finished-product assay | LES + CDS approved result/link + calculation + signatures | Pass |
| PQ-003 | Microbiology EM workflow | Location schedule → incubation/count → alert handling → approval | Pass |
| PQ-004 | Stability workflow | Pull schedule, overdue dashboard, test completion and report | Pass after DEF-005 |
| PQ-005 | OOS/OOT workflow | Limit excursion → eQMS case/link → hold → disposition | Pass |
| PQ-006 | Rejected/cancelled sample | Condition exception, reason, re-sample and retained history | Pass |
| PQ-007 | Interface outage contingency | Controlled paper/manual entry, verification and reconciliation | Pass |
| PQ-008 | Audit-trail review | Reviewer filters relevant events, documents review and approves | Pass |
| PQ-009 | Report/SAP completion | Controlled report and acknowledged SAP status/result | Pass |
| PQ-010 | Role-based scenario | Analyst/reviewer/supervisor/QA activities and negative permissions | Pass |
| PQ-011 | Legacy retrieval | Search and retrieve migrated/archive record, attachment and audit trail | Pass |
| PQ-012 | Controlled administration | Approved role/configuration change, evidence and rollback | Pass |

## 3. Business acceptance observations

Users confirmed the workflow was understandable, source records were accessible, exceptions were visible and reports supported review. DEF-005 was a low dashboard sort issue and was corrected/retested without impact on record correctness.

## 4. Conclusion

All 12 PQ/UAT scenarios passed. Business Process Owner accepts the system for the approved intended use, subject to completion of release prerequisites and VSR approval.

PQ/UAT acceptance is based on representative users performing representative business processes with approved procedures and realistic controlled data. Acceptance does not authorise production use until migration, training, support readiness, VSR and go-live approval are complete. Usability observations shall be dispositioned when they could affect data entry, review effectiveness or exception handling.

| PQ acceptance focus | Evidence expectation |
|---|---|
| Representative role | Qualified analyst/reviewer/supervisor/QA user executes assigned scenario |
| End-to-end process | Sample, execution, review, approval, interface and report flow are covered |
| Procedure fit | User can follow draft/final SOP without undocumented workaround |
| Exception visibility | OOS/OOT, retest, manual entry or interface issue is visible and controlled |
| Business acceptance | BPO records acceptance and any residual open item |

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Input | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Input | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Input | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Input | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Input | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Input | QCL-2026-EST-001 | [Electronic Signature Test Report](055_Electronic_Signature_Test_Report.md) |
| Input | QCL-2026-RPT-001 | [Report, Print and Export Verification Report](059_Report_Print_and_Export_Verification_Report.md) |
| Input | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |
| Input | QCL-2026-TRN-001 | [Training Plan, Materials and Training Record](071_Training_Plan_Materials_and_Training_Record.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | QCL-2026-PRC-001 | [Production Readiness Checklist](074_Production_Readiness_Checklist.md) |
| Output | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |

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
