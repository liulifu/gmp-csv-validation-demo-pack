---
document_number: QCL-2026-CUT-001
title: "Cutover, Rollback and Contingency Plan"
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

# Cutover, Rollback and Contingency Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CUT-001 |
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

## 1. Purpose

This plan controls production cutover from Legacy LIMS/hybrid processes to QCLabOne, including contingency and rollback.

## 2. Cutover schedule

| Timing | Activity | Owner | Case outcome |
|---|---|---|---|
| T-14 days | Confirm change freeze, final migration list, users/training, support roster and rollback environment | All owners | Complete |
| T-7 days | Legacy LIMS configuration/data-entry freeze except approved business transactions | Legacy Owner/QC | Complete |
| T-3 days | Final production backup, certificate check, configuration checksum and cutover rehearsal | IT/Supplier | Complete |
| T-1 day 18:00 | Stop routine Legacy LIMS entry; begin controlled contingency log | QC BPO | Complete |
| T0 18:30 | Final extraction of legacy/Excel active data | Migration Lead | Complete |
| T0 20:00 | Load and automated reconciliation | Migration/Supplier | Complete |
| T+1 02:00 | Business critical-field and sample verification | QC/QA | Complete |
| T+1 06:00 | Interface smoke test, backup check and production baseline verification | IT/System Owner | Complete |
| T+1 08:00 | Go/no-go meeting | Sponsor/BPO/System Owner/QA | Go |
| T+1 09:00 | Enable users and interfaces; start hypercare | System Owner | Complete |

## 3. Go/no-go criteria

Production migration accepted; no Critical/High discrepancy; baseline/version correct; SAP/eQMS/CDS/instrument smoke tests pass; backup succeeds; support available; procedures/training effective; no unresolved product/data-integrity concern.

## 4. Rollback criteria

Rollback is considered for corrupted/incomplete migration that cannot be corrected within window, unavailable critical workflow/interface beyond agreed cutover window, signature/audit failure, security compromise or inability to reconcile transactions. QA and BPO decide with System Owner.

## 5. Rollback method

Disable new entries/interfaces, preserve QCLabOne evidence, restore Legacy LIMS controlled write access from approved state if safe, reconcile all contingency/new-system transactions and issue communication. Rollback does not delete QCLabOne evidence.

## 6. Hypercare

Four weeks of 07:00–22:00 on-site/remote coverage plus 24×7 P1 support. Daily review covers incidents, queues, audit/signature anomalies, backup and user issues.

## 7. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Input | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Input | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Input | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |
| Input | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2026-TRN-001 | [Training Plan, Materials and Training Record](071_Training_Plan_Materials_and_Training_Record.md) |
| Output | QCL-2026-PDM-001 | [Production Data Migration Execution and Reconciliation Record](073_Production_Data_Migration_Execution_and_Reconciliation_Record.md) |
| Output | QCL-2026-PRC-001 | [Production Readiness Checklist](074_Production_Readiness_Checklist.md) |
| Output | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |
| Output | QCL-2026-HOV-001 | [System Handover and Support Model](076_System_Handover_and_Support_Model.md) |

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
