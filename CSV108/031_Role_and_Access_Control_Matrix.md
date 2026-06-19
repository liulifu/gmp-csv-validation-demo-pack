---
document_number: QCL-2026-RAC-001
title: "Role and Access Control Matrix"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Design"
version: "1.0"
effective_or_record_date: "2026-10-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "Vendor Solution Architect"
approved_by: "QA CSV Lead"
---

# Role and Access Control Matrix

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-RAC-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Design |
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

## 1. Access-control principles

Access follows unique identity, least privilege, need-to-know, segregation of duties, approved joiner/mover/leaver workflow and periodic recertification.

## 2. Role matrix

| Role | Allowed activities | Prohibited/conflicting activities |
|---|---|---|
| Analyst | Create/receive assigned sample; execute LES; enter/capture data; submit | No spec/config/role administration; no final approval |
| Reviewer | Read source records/audit trail; verify calculation; review/reject | Cannot modify submitted data or administer system |
| QC Supervisor | Assign work; resolve authorised exceptions; approve defined results | Cannot administer security or audit trail |
| QA Reviewer | Review critical audit trails, OOS/OOT links and quality exceptions; approve defined QA decisions | No routine data entry or technical administration |
| Master Data Steward | Create/revise controlled master data | Cannot make own item effective or approve final results |
| System Administrator | Configure approved settings, roles and interfaces; run monitoring | Cannot create/modify QC result content or approve results |
| IT Support | Infrastructure, logs, backup/restore and incident support | No application-content editing; no QC approval |
| Vendor Support | Time-limited diagnostic/support access | No standing production access; no unapproved change |
| Auditor/Inspector Read-Only | Read/search/export approved records and audit trails | No create/change/approve |
| Service Account | Execute one defined interface or scheduled job | No interactive login; least privilege |

## 3. Permission matrix

| Function | Analyst | Reviewer | Supervisor | QA | Master Data | Sys Admin | IT | Vendor |
|---|---|---|---|---|---|---|---|---|
| Execute assigned test | R/W | Read | Read | Read | Read | Read metadata | No | No |
| Submit result | Yes | No | No | No | No | No | No | No |
| Review result/audit trail | Own read | Yes | Yes | Yes | Read | No approval | No | No |
| Final approve defined result | No | No | Yes | Where required | No | No | No | No |
| Create/revise specification | No | No | Read | Read | Yes | Technical support only | No | No |
| Make specification effective | No | No | No | Approval/oversight | No self-approval | Promote approved package | No | No |
| Manage roles | No | No | Request | Review | No | Execute approved request | Technical support | No standing access |
| View audit trail | Own/assigned | Yes | Yes | Yes | Relevant | Technical | Security logs | Ticketed |
| Change configuration | No | No | No | Approve oversight | No | Approved only | Infrastructure only | Ticketed approved |
| Delete GxP record/audit trail | No | No | No | No | No | No | No | No |

## 4. Account controls

Shared accounts are prohibited. Service accounts are non-interactive and owned. Two break-glass accounts are sealed, monitored and quarterly tested. Vendor accounts are disabled except during approved support windows.

## 5. Review frequency

All active accounts and roles quarterly; privileged accounts monthly; service accounts semi-annually; immediate disablement upon termination and within one business day for role transfer unless risk requires faster action.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-MDS-001 | [Master Data Specification](030_Master_Data_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Output | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Output | QCL-2027-UAR-001 | [User Access Request and Approval Records](078_User_Access_Request_and_Approval_Records.md) |
| Output | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Output | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | Vendor Solution Architect | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-31 | Initial approved fictional case version. |
