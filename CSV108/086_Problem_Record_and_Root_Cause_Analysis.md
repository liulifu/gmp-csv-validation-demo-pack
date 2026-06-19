---
document_number: QCL-2027-PRB-006
title: "Problem Record and Root Cause Analysis"
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

# Problem Record and Root Cause Analysis

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-PRB-006 |
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

## 1. Problem statement

The SAP outbound client certificate expired without the required 60/30/7-day warnings, causing a 2 h 18 min interface interruption.

## 2. Root-cause analysis

| Why | Finding |
|---|---|
| Why did the interface fail? | The TLS client certificate expired. |
| Why was it not renewed? | The certificate was absent from the central expiry dashboard. |
| Why was it absent? | A 2027 gateway configuration change renamed the certificate alias; the discovery rule matched the old alias. |
| Why was the monitoring change not detected? | Change verification checked connectivity but not monitoring inventory/alert simulation. |
| Why did the process allow this gap? | The change checklist did not require certificate-monitoring registration and owner/due-date confirmation. |

**Root cause:** Incomplete change-verification design for certificate inventory and alerting after alias/configuration changes.  
**Contributing factor:** Certificate renewal ownership was split between infrastructure and application support without a single accountable register owner.

## 3. Corrective and preventive actions

| Action | Owner | Due | Status |
|---|---|---|---|
| Create authoritative certificate/secret register with owner, use and expiry | IT Security Owner | 2027-10-25 | Complete |
| Implement automated discovery independent of certificate alias | IT Monitoring Lead | 2027-11-10 | Complete |
| Add 60/30/7-day alerts and escalation to System Owner | IT Monitoring Lead | 2027-11-10 | Complete |
| Update change checklist to verify monitoring/renewal after certificate change | Change Manager | 2027-11-15 | Complete |
| Quarterly certificate register review | System Owner | Ongoing | First review complete 2028-01-05 |

## 4. Effectiveness

No unmonitored production certificate was found in two subsequent monthly scans. Test certificate alerts fired at 60/30/7 days. Action is effective.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
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
