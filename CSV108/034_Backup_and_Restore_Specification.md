---
document_number: QCL-2026-BRS-001
title: "Backup and Restore Specification"
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

# Backup and Restore Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-BRS-001 |
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

## 1. Scope and objectives

Backup protects database, attachments, configuration, audit logs, gateway and archive records. Recovery objectives are RPO 15 minutes and RTO 8 hours for a declared production disaster.

## 2. Backup schedule

| Data/component | Backup method/frequency | Retention | Protection | Owner/platform |
|---|---|---|---|---|
| Production database | Continuous transaction log/PITR plus nightly full | 35 days online; monthly copy 1 year | AES-256 at rest/TLS | Supplier cloud backup |
| Attachments/object store | Nightly incremental, weekly full | 90 days online; monthly copy 1 year | AES-256/TLS | Supplier cloud backup |
| Configuration/export package | At each approved release plus nightly | System life + 2 years | Encrypted | eDMS + secure repository |
| Interface gateway VM/config | Nightly image + configuration export | 35 days; monthly 1 year | Encrypted | Veeam on-site/DR |
| Audit/log export | Daily immutable export | 2 years online; longer with related GMP record | WORM/encrypted | Security log repository |
| Legacy archive | Monthly integrity scan and quarterly secondary copy | Applicable GMP retention period | Encrypted/read-only | ArchiveVault + secondary copy |

## 3. Monitoring and exception handling

Automated jobs are monitored daily. Failed jobs alert IT and supplier support. A failed critical backup requires same-day rerun, incident record if the recovery window is at risk, and QA notification for potential GxP impact.

## 4. Restore process

1. Authorise restore ticket and define recovery point/scope.
2. Isolate target environment and preserve original evidence.
3. Restore database, attachments, configuration and required logs.
4. Execute consistency checks, sample record retrieval, audit-trail and signature checks.
5. Reconcile selected records and interface status.
6. Approve return to service and retain the restore report.

## 5. Test frequency

Technical restore at least annually and after major architecture change; application-level restore included in DR exercise. Archive secondary-copy retrieval is tested annually.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Output | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Output | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Output | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Output | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Output | QCL-2027-RST-001 | [Periodic Restore Test Report](084_Periodic_Restore_Test_Report.md) |

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
