---
document_number: SOP-IT-LIMS-001
title: "QCLabOne 2.0 System Administration SOP"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "SOP and Training"
version: "1.0"
effective_or_record_date: "2027-05-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Training/Procedure Owner"
reviewed_by: "System Owner"
approved_by: "QA Department Head"
---

# QCLabOne 2.0 System Administration SOP

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | SOP-IT-LIMS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | SOP and Training |
| Version | 1.0 |
| Effective/record date | 2027-05-31 |
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

This SOP controls QCLabOne administration, access execution, approved configuration promotion, master-data support, interface operations and technical troubleshooting.

## 2. Administrative principles

- Administrators execute approved requests; they do not approve their own privileged access or configuration.
- Production administration uses named privileged accounts separate from ordinary user accounts.
- Administrators shall not create, alter or approve QC results.
- Direct database modification is prohibited except under an approved emergency recovery plan with QA oversight and documented reconciliation.
- Vendor access is disabled by default and tied to a ticket/window.

## 3. User access administration

1. Verify approved request, training status, manager/BPO approval and any QA approval.
2. Assign only approved role groups.
3. Perform a second-person check for privileged or high-risk roles.
4. Record actual execution date/time and administrator.
5. Disable access immediately for termination and promptly for transfer/suspension.
6. Retain evidence and include accounts in periodic review.

## 4. Configuration and master-data promotion

Approved package must identify change record, source environment, version, checksum, affected URS/risk/test and rollback. A separate administrator promotes to production. Post-promotion verification confirms package/version, key controls and monitoring.

## 5. Interface administration

Monitor queues and reconciliation. Do not edit message payloads in place. Reprocessing requires approved role, documented cause and audit trail. A systematic or unexplained error requires incident/problem management.

## 6. Audit, logs and time

Do not disable audit trails, security logging or time synchronization. Any outage/change to these services is a potential GxP incident. Export logs through approved functions; protect copies from alteration.

## 7. Backup/restore and recovery

Follow the approved operations SOP. Restore requires an authorised ticket, defined recovery point, isolated target and post-restore business/QA verification.

## 8. Break-glass accounts

Two sealed accounts are held by IT Security. Use requires Incident Commander and QA approval where practicable, immediate notification, full session review and password reset/reseal. Quarterly non-production functionality check is documented.

## 9. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Input | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Input | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Input | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Output | QCL-2026-HOV-001 | [System Handover and Support Model](076_System_Handover_and_Support_Model.md) |
| Output | QCL-2027-UAR-001 | [User Access Request and Approval Records](078_User_Access_Request_and_Approval_Records.md) |
| Output | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Output | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Output | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Output | QCL-2027-RST-001 | [Periodic Restore Test Report](084_Periodic_Restore_Test_Report.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Training/Procedure Owner | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Department Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-05-31 | Initial approved fictional case version. |
