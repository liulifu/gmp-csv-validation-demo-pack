---
document_number: QCL-2027-INC-014
title: "Incident Record and Impact Assessment"
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

# Incident Record and Impact Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-INC-014 |
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

## 1. Incident summary

**Incident:** INC-2027-014  
**Start:** 2027-10-18 07:42 CST  
**End:** 2027-10-18 10:00 CST  
**Priority:** P1 technical / Medium GxP impact after assessment  
**Affected service:** QCLabOne → SAP outbound inspection-status interface

## 2. Timeline

| Time | Event/action | Owner |
|---|---|---|
| 2027-10-18 07:42 | SAP outbound interface alerts on TLS handshake failure | Monitoring |
| 07:48 | IT confirms client certificate expired at 00:00; inbound SAP requests still queued safely | IT |
| 07:55 | P1 incident declared; System Owner, QC and QA notified | Incident Commander |
| 08:05 | Outbound status messages paused; QC instructed not to assume SAP update | QC BPO |
| 08:20 | Emergency certificate renewal approved; no manual result re-entry required | QA/System Owner |
| 09:18 | New certificate installed and connection test successful | IT |
| 09:32 | 92 queued messages replayed by original message ID | Interface Support |
| 09:48 | SAP/QCLabOne reconciliation shows 92/92 accepted; no duplicate/loss | QC/IT |
| 10:00 | Service declared restored; problem record opened | Incident Commander |

## 3. Impact assessment

Ninety-two outbound status messages were delayed. QCLabOne results, signatures and audit trails remained available and correct. No message was lost or duplicated. SAP did not receive status until replay, so affected inspection lots remained in the prior/hold state; no batch was incorrectly released. No manual duplicate entry occurred.

## 4. Containment and recovery

The failed route was isolated, users were informed, queued messages were preserved and an emergency certificate was installed under approved emergency change. Reconciliation was 100%.

## 5. Disposition

No product-quality or record-integrity impact. A problem record was opened because certificate monitoring failed to provide advance warning.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2026-HOV-001 | [System Handover and Support Model](076_System_Handover_and_Support_Model.md) |
| Output | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
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
| 1.0 | 2027-12-20 | Initial approved fictional case version. |
