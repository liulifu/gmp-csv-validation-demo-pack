---
document_number: QCL-2027-CHG-021
title: "Change Control Record"
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

# Change Control Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-CHG-021 |
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

## 1. Change request

**Change:** CHG-2027-021  
**Title:** Implement authoritative certificate inventory and automated expiry monitoring  
**Source:** INC-2027-014 / PRB-006  
**Type:** Planned corrective technical change

## 2. Scope

Add certificate discovery on QCL-IGW-01 and cloud endpoints; central register with owner/service/expiry; 60/30/7-day alerts; escalation; dashboard; change-checklist update. No business data model, calculation, workflow, audit trail or signature logic is changed.

## 3. Impact assessment

| Area | Impact |
|---|---|
| GxP function | Indirect availability improvement; no intended record-content change |
| Interfaces | Monitoring only; connection certificates remain unchanged except controlled test certificate |
| Security | Positive; improved expiry control |
| Validation | Focused installation/configuration verification and alert regression |
| SOP/training | Operations SOP/checklist updated; support team briefed |
| Rollback | Disable new monitoring job and restore prior dashboard configuration |

## 4. Implementation plan

Deploy to test, validate discovery/alerts, review false positives, promote configuration, verify all production certificates present, update register and execute 60/30/7-day simulated alert tests.

## 5. Approval and planned verification

Approved by System Owner with QA review on 2027-10-27. Verification is documented in Documents 090 and 091.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Input | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |
| Output | QCL-2027-REG-003 | [Regression Test Plan and Report](090_Regression_Test_Plan_and_Report.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
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
| 1.0 | 2027-12-20 | Initial approved fictional case version. |
