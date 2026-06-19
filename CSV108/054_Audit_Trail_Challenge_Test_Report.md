---
document_number: QCL-2026-ATC-001
title: "Audit Trail Challenge Test Report"
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

# Audit Trail Challenge Test Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-ATC-001 |
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

Challenge audit-trail generation, completeness, protection, reason-for-change, review and export for critical GxP objects.

## 2. Results

| Test | Scenario | Actual result | Outcome |
|---|---|---|---|
| ATC-001 | Result creation/change/delete attempt | Create and change recorded with old/new value; delete denied and attempt logged | Pass |
| ATC-002 | Specification/formula/master-data changes | All critical fields recorded | Pass after DEV-001 |
| ATC-003 | Mandatory reason for critical change | Save blocked without reason | Pass after DEV-001 |
| ATC-004 | Protection/filter/export/review | No tested role could alter trail; export matched source/filter | Pass |
| ATC-005 | Role/signature/workflow events | Actor, target, old/new state, time and meaning captured | Pass |

## 3. Deviation DEV-001

Initial configuration did not require a reason when changing a sample comment classified by the site as critical metadata. Event classification and mandatory-reason configuration were corrected in package `QCL-CONFIG-1.0-R1`. ATC-002, ATC-003 and affected regression tests passed.

## 4. Review usability

Reviewers successfully filtered by record, user, date, event type and changed field; exported evidence identified filters and execution time. No ordinary or routine administrative role could edit/delete audit entries.

## 5. Conclusion

Audit-trail controls are acceptable for intended use and operational review.

Audit-trail test acceptance depends on review usability as well as event capture. For each critical event type, the reviewer must be able to see who did what, when, why where required, prior value, new value, affected record and whether a downstream review/signature was invalidated. Exported audit evidence shall remain complete enough for inspection use.

| Audit challenge focus | Acceptance expectation |
|---|---|
| Critical event capture | Creation/change/delete attempt/configuration/security/signature events recorded |
| Reason for change | Mandatory reason enforced for site-defined critical metadata |
| Review filters | Reviewer can locate event by record, user, field, event type and time |
| Protection | Routine/admin users cannot edit or delete audit entries |
| Export fidelity | Export shows filter, time, requester and complete event context |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Input | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-CAPA-001 | [CAPA Record and Effectiveness Check](062_CAPA_Record_and_Effectiveness_Check.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | SOP-QA-ATR-001 | [QCLabOne 2.0 Audit Trail Review SOP](068_Audit_Trail_Review_SOP.md) |
| Output | QCL-2027-ATR-001 | [Periodic Audit Trail Review Record](081_Periodic_Audit_Trail_Review_Record.md) |
| Output | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |

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
