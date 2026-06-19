---
document_number: SOP-IT-LIMS-002
title: "QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP"
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

# QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | SOP-IT-LIMS-002 |
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

This SOP defines integrated technical operation of QCLabOne: monitoring, maintenance, backup, incident/problem management, change/patch control and security.

## 2. Routine monitoring

| Control | Frequency | Action/record |
|---|---|---|
| Application/interface health | Continuous; daily review | Dashboard and exception-queue review |
| Backup status | Daily | Confirm required jobs; investigate failure |
| Certificates/secrets | Daily automated; monthly review | 60/30/7-day alerts and renewal change |
| Capacity/performance | Weekly/monthly trend | Act at 70% warning/85% critical |
| Security events/vulnerabilities | Continuous; daily triage | Escalate potential GxP/security impact |
| Time synchronization | Continuous | Incident if drift >60 seconds |
| Supplier service/changes | Monthly | Review notifications and SLA |

## 3. Incident management

Record detection time, reporter, affected service/data, users/batches, immediate containment, continuity action, GxP/data-integrity/security impact, communications, recovery, reconciliation and closure. Potential record loss, unauthorised access, signature/audit failure or incorrect result is High priority until assessed.

## 4. Problem and CAPA

Repeated or major incidents require root-cause analysis using evidence such as logs, configuration, timeline and supplier analysis. Corrective/preventive actions have owners, due dates and effectiveness checks.

## 5. Change control

Before implementation, document reason, scope, impacted configuration/records/URS/risk/interfaces/SOP/training, validation strategy, rollback and approvals. Emergency changes protect service/data but require retrospective change documentation within one business day.

## 6. Patch and release management

Review release notes, vulnerabilities, compatibility, data model, audit/signature effects, supplier test evidence and rollback. Test based on risk. No supplier release is promoted automatically to production.

## 7. Backup and restore

Review backup logs daily and rerun failures. Perform annual application-level restore and DR exercise. Restore to production requires QA/business verification when regulated data may be affected.

## 8. Security

Use least privilege, separate admin identity, just-in-time vendor access, approved secret vault, EDR, encryption and monitoring. Critical vulnerability or suspected compromise triggers the security incident process and possible system isolation.

## 9. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Input | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Input | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Input | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Output | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Output | QCL-2027-RST-001 | [Periodic Restore Test Report](084_Periodic_Restore_Test_Report.md) |
| Output | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Output | QCL-2027-PAT-003 | [Patch and Upgrade Impact Assessment](089_Patch_and_Upgrade_Impact_Assessment.md) |
| Output | QCL-2027-REG-003 | [Regression Test Plan and Report](090_Regression_Test_Plan_and_Report.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |
| Output | QCL-2028-DRE-001 | [Business Continuity and Disaster Recovery Exercise Report](095_Business_Continuity_and_DR_Exercise_Report.md) |

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
