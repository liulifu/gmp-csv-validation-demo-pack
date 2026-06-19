---
document_number: QCL-2028-DRE-001
title: "Business Continuity and Disaster Recovery Exercise Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Operation"
version: "1.0"
effective_or_record_date: "2028-03-15"
case_status: "Completed/Closed in fictional operating record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "QA System Oversight"
---

# Business Continuity and Disaster Recovery Exercise Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-DRE-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Operation |
| Version | 1.0 |
| Effective/record date | 2028-03-15 |
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

## 1. Exercise

Annual technical DR and business-continuity exercise executed 2028-02-24 using a simulated primary-region loss.

## 2. Results

| Area | Acceptance | Actual | Outcome |
|---|---|---|---|
| Detection/activation | Primary region declared unavailable; DR team notified | 18 minutes | Pass |
| Database recovery point | Recover within 15-minute RPO | 8 minutes behind last commit | Pass |
| Service restoration | RTO ≤8 hours | 5 h 58 min to technical service; 6 h 42 min incl. business/QA validation | Pass |
| Record integrity | 250 selected signed records, attachments, audit events and calculations | 100% match | Pass |
| Interface recovery | Queued SAP/eQMS/CDS messages replay/reconcile | 174/174 reconciled | Pass |
| Manual continuity | 50 pre-numbered forms issued/simulated and reconciled once | 50/50 | Pass |
| Backup/monitoring | Backup resumes; alerts healthy | Pass | Pass |
| Communication | Stakeholder cadence and decision log followed | One 12-minute late business update | Minor observation |

## 3. Observation and action

The 60-minute business-update cadence was missed once by 12 minutes while the team verified interface reconciliation. The call tree and alternate communications coordinator were updated. No recovery or data-integrity impact occurred.

## 4. Conclusion

RPO/RTO, application integrity, interface reconciliation and manual-continuity controls were demonstrated. Exercise passed.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Input | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Input | QCL-2027-RST-001 | [Periodic Restore Test Report](084_Periodic_Restore_Test_Report.md) |
| Input | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA System Oversight | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2028-03-15 | Initial approved fictional case version. |
