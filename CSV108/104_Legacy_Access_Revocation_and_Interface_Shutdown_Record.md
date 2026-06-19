---
document_number: QCL-2028-AIS-001
title: "Legacy Access Revocation and Interface Shutdown Record"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Retirement"
version: "1.0"
effective_or_record_date: "2028-03-31"
case_status: "Approved/Closed in fictional retirement record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Legacy System Owner"
reviewed_by: "Records Management Owner"
approved_by: "Site Quality Head"
---

# Legacy Access Revocation and Interface Shutdown Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-AIS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Retirement |
| Version | 1.0 |
| Effective/record date | 2028-03-31 |
| Case status | Approved/Closed in fictional retirement record |

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

Record removal of Legacy LIMS access, service accounts, interfaces, scheduled jobs and network routes.

## 2. Revocation/shutdown record

| Area | Population/service | Action/evidence | Status |
|---|---|---|---|
| Human users | 214 Legacy LIMS named accounts | Disabled 2028-03-29; final export retained | Complete |
| Privileged accounts | 8 admin/database accounts | Disabled; credentials sealed for 90-day recovery team only | Complete |
| Vendor accounts | 3 | Disabled and remote route removed | Complete |
| Service accounts | 6 interface/scheduler accounts | Disabled after interface stop | Complete |
| SAP legacy interfaces | Inbound/outbound legacy endpoints | Stopped; SAP routing removed; QCLabOne unaffected | Complete |
| CDS/instrument legacy feeds | 12 endpoints | Stopped after source-owner confirmation | Complete |
| Email/report scheduler | Legacy scheduled reports | Disabled; recipients notified | Complete |
| Firewall/DNS | Legacy app/database routes and names | Blocked/retired; archive URL remains | Complete |
| Licences/support | Legacy application/Oracle support allocation | Termination initiated after shutdown | Complete |

## 3. Final activity review

Audit/security logs from 2028-03-22 to shutdown showed only authorised retirement-team access and automated archive checks. No data modification occurred; application/database remained read-only.

## 4. Post-shutdown interface verification

QCLabOne SAP/eQMS/CDS/instrument interfaces passed smoke tests. No enterprise route continued to reference Legacy LIMS. Archive access remained available.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | SOP-QA-ARC-001 | [Data Retention, Archiving and Record Retrieval SOP](070_Data_Retention_Archiving_and_Record_Retrieval_SOP.md) |
| Input | QCL-2028-RTP-001 | [Legacy LIMS Retirement Plan](101_Legacy_LIMS_Retirement_Plan.md) |
| Input | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Output | QCL-2028-DCL-001 | [Legacy System Decommissioning Checklist](105_Legacy_System_Decommissioning_Checklist.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | CSI-SZ-001-CHG-2028-03 | [Computerised System Inventory Update—Retired Status](107_Computerised_System_Inventory_Update_Retired_Status.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Legacy System Owner | Completed |
| Reviewed by | Records Management Owner | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2028-03-31 | Initial approved fictional case version. |
