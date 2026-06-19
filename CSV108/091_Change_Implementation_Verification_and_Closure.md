---
document_number: QCL-2027-CHG-021-C
title: "Change Implementation Verification and Closure"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Operation"
version: "1.0"
effective_or_record_date: "2027-12-20"
case_status: "Completed/Closed in fictional operating record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "QA System Oversight"
---

# Change Implementation Verification and Closure

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-CHG-021-C |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Operation |
| Version | 1.0 |
| Effective/record date | 2027-12-20 |
| Case status | Completed/Closed in fictional operating record |

## Governing references

- China GMP (2010 Revision), Appendix: Computerised Systems (effective 1 December 2015)
- China GMP (2010 Revision), Appendix: Qualification and Validation (effective 1 December 2015)
- EU GMP Annex 11: Computerised Systems (2011)
- EU GMP Annex 15: Qualification and Validation (2015)
- 21 CFR Part 11: Electronic Records; Electronic Signatures
- FDA Guidance: Part 11, Electronic Records; Electronic Signatures — Scope and Application
- PIC/S PI 041-1: Good Practices for Data Management and Integrity in Regulated GMP/GDP Environments (2021)
- ISPE GAMP 5, Second Edition (2022), used as non-binding industry guidance

## 1. Implementation record

CHG-2027-021 certificate monitoring was implemented 2027-11-18. LabSphere 8.4.3 was implemented during the approved maintenance window 2027-12-09 22:00–22:48 CST.

## 2. Post-implementation verification

| Check | Actual result |
|---|---|
| Application/version | 8.4.3 displayed in production |
| Configuration checksum | Site configuration unchanged and matches approved baseline revision |
| Certificate inventory | 14/14 production certificates discovered with owner/expiry |
| Alert simulation | 60/30/7-day alerts received by IT/System Owner |
| Critical smoke tests | SSO, sample, result, signature, audit, report and interfaces pass |
| Monitoring/backup | Healthy; first post-change backup pass |
| Open incidents | None |

## 3. Baseline updates

CI-001 updated to 8.4.3; production baseline revision is `QCL-PROD-BL-1.1`. Release and regression evidence were archived.

## 4. Closure decision

Change objectives achieved; no adverse impact; rollback not required. Change closed 2027-12-20.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Input | QCL-2027-PAT-003 | [Patch and Upgrade Impact Assessment](089_Patch_and_Upgrade_Impact_Assessment.md) |
| Input | QCL-2027-REG-003 | [Regression Test Plan and Report](090_Regression_Test_Plan_and_Report.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |
| Output | QCL-2028-SPR-001 | [Supplier Periodic Performance and SLA Review](096_Supplier_Periodic_Performance_and_SLA_Review.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA System Oversight | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-12-20 | Initial approved fictional case version. |
