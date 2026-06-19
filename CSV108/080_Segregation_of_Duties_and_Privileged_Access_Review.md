---
document_number: QCL-2027-SOD-001
title: "Segregation of Duties and Privileged Access Review"
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

# Segregation of Duties and Privileged Access Review

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-SOD-001 |
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

## 1. Scope

Review of privileged roles, conflicting permission combinations, vendor accounts, service accounts and break-glass accounts as of 2027-09-30.

## 2. Review results

| Account/group | Role | Expected segregation | Finding | Disposition |
|---|---|---|---|---|
| SYS-ADM-001 | System Administrator | No QC approval | No conflict | Accept |
| SYS-ADM-002 | System Administrator | No QC approval | No conflict | Accept |
| IT-SUP-001 | IT Support | No application content edit/approval | No conflict | Accept |
| QA-REV-001 | QA Reviewer | No admin/config promotion | No conflict | Accept |
| MD-STW-001 | Master Data Steward | Cannot approve own item/effective promotion | No conflict | Accept |
| VND-SUP-001/2/3 | Vendor Support | Disabled by default; no QC approval | No standing conflict | Accept |
| QC-ANL-017 | Analyst | Erroneously received SuperUser for 47 min on 2027-08-22 | Conflict existed; no change activity; ODV-004/CAPA closed | Closed |

## 3. Privileged activity

Six privileged user accounts generated 214 administrative events during the period. A 100% review confirmed that each event linked to an approved access request, incident or change. Nine vendor sessions linked to approved tickets and were disabled at window end.

## 4. Conclusion

No open SoD conflict remains. ODV-004 resulted in a role-provisioning control enhancement and effectiveness check.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Input | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Input | QCL-2027-UAR-001 | [User Access Request and Approval Records](078_User_Access_Request_and_Approval_Records.md) |
| Input | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |

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
