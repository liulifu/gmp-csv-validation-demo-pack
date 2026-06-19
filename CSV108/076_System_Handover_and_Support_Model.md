---
document_number: QCL-2026-HOV-001
title: "System Handover and Support Model"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Release"
version: "1.0"
effective_or_record_date: "2027-06-15"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "Site Quality Head"
---

# System Handover and Support Model

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-HOV-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Release |
| Version | 1.0 |
| Effective/record date | 2027-06-15 |
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

## 1. Handover scope

The project transfers the approved production service, documents, configuration, monitoring, support knowledge and outstanding lifecycle obligations to operations.

## 2. Support model

| Level | Function | Scope | Owner | Coverage |
|---|---|---|---|---|
| L0 | User job aids/local super-user | Navigation and known procedural questions | QC Super Users | Business hours |
| L1 | Service desk | Ticket logging, triage, password/known issue routing | IT Service Desk | 24×7 P1; business hours others |
| L2 | Application/Interface support | Application, queue, configuration, logs, restore coordination | System Owner/IT App Team | On-call P1 |
| L3 | Supplier support | Product defect, cloud platform, code and advanced recovery | LabSphere | Per SLA |
| QA | Quality oversight | GxP impact, deviation/change/CAPA and release decisions | QA | On-call escalation |

## 3. Handover items

Production/admin URLs; configuration baseline; CI register; interface/monitoring dashboards; backup/DR runbooks; supplier contacts; certificates/secrets inventory; access groups; known-error list; SOPs; training records; validation dossier; migration/archive status; periodic review schedule.

## 4. Escalation

P1 or potential GxP/data-integrity/security events contact IT Duty Manager, System Owner, QC BPO, QA and Supplier Incident Commander immediately. Service desk must not close a ticket solely because a workaround exists without GxP assessment.

## 5. Hypercare exit

Hypercare ended 2027-07-14 after four weeks with no Critical/High incident, queues reconciled daily, backups successful, response time within target and user support volume reduced to steady state.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Input | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Input | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2026-CUT-001 | [Cutover, Rollback and Contingency Plan](072_Cutover_Rollback_and_Contingency_Plan.md) |
| Input | QCL-2026-PRC-001 | [Production Readiness Checklist](074_Production_Readiness_Checklist.md) |
| Input | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |
| Input | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |
| Output | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Output | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-SPR-001 | [Supplier Periodic Performance and SLA Review](096_Supplier_Periodic_Performance_and_SLA_Review.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-06-15 | Initial approved fictional case version. |
