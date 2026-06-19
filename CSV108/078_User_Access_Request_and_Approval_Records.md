---
document_number: QCL-2027-UAR-001
title: "User Access Request and Approval Records"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Operation"
version: "1.0"
effective_or_record_date: "2027-09-30"
case_status: "Completed/Closed in fictional operating record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "QA System Oversight"
---

# User Access Request and Approval Records

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-UAR-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Operation |
| Version | 1.0 |
| Effective/record date | 2027-09-30 |
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

## 1. Purpose

This record demonstrates the approved user-access process used at go-live and during the first operating quarter. User IDs are fictional training identifiers.

## 2. Access records

| Request ID | User ID | Role | Department | Request/activation date | Approval | Execution/check | Current status |
|---|---|---|---|---|---|---|---|
| UAR-0001 | QC-ANL-001 | Analyst | Chemistry | 2027-06-10 | BPO + manager | IT Admin A / checker B | Active |
| UAR-0002 | QC-ANL-002 | Analyst | Microbiology | 2027-06-10 | BPO + manager | IT Admin A / checker B | Active |
| UAR-0003 | QC-REV-001 | Reviewer | Chemistry | 2027-06-10 | BPO + manager | IT Admin B / checker A | Active |
| UAR-0004 | QC-SUP-001 | QC Supervisor | QC | 2027-06-10 | BPO + QA | IT Admin A / checker B | Active |
| UAR-0005 | QA-REV-001 | QA Reviewer | QA | 2027-06-10 | QA Head | IT Admin B / checker A | Active |
| UAR-0006 | MD-STW-001 | Master Data Steward | QC | 2027-06-10 | BPO + QA | IT Admin A / checker B | Active |
| UAR-0007 | SYS-ADM-001 | System Administrator | IT | 2027-06-09 | System Owner + QA | Privileged Admin / checker | Active |
| UAR-0008 | IT-SUP-001 | IT Support | IT | 2027-06-09 | IT Manager + System Owner | Privileged Admin / checker | Active |
| UAR-0009 | VND-SUP-001 | Vendor Support | Supplier | 2027-06-14 | System Owner + QA; disabled by default | Just-in-time group | Disabled |
| UAR-0010 | AUD-RO-001 | Auditor Read-Only | QA | 2027-09-04 | QA Head | IT Admin A / checker B | Disabled after mock audit |
| UAR-0011 | QC-ANL-017 | Analyst | Chemistry | 2027-08-01 | BPO + manager | IT Admin B / checker A | Active |
| UAR-0012 | QC-REV-004 | Reviewer | Stability | 2027-08-15 | BPO + manager | IT Admin A / checker B | Active |

## 3. Population summary

At go-live, 97 trained users were enabled: 42 Analysts, 16 Reviewers, 8 QC Supervisors, 6 QA Reviewers, 5 Master Data Stewards, 4 System Administrators and 16 supporting/read-only roles. Additional users followed the same request process.

## 4. Control checks

Each request included business need, exact role, manager/BPO approval, training completion and expiry/temporary dates where applicable. Privileged roles had QA/System Owner approval and second-person provisioning verification. Vendor accounts remained disabled except during approved sessions.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Input | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |
| Input | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Input | QCL-2026-TRN-001 | [Training Plan, Materials and Training Record](071_Training_Plan_Materials_and_Training_Record.md) |
| Input | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |
| Output | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Output | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA System Oversight | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-09-30 | Initial approved fictional case version. |
