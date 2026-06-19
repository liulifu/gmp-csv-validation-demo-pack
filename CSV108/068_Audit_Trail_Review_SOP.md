---
document_number: SOP-QA-ATR-001
title: "QCLabOne 2.0 Audit Trail Review SOP"
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

# QCLabOne 2.0 Audit Trail Review SOP

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | SOP-QA-ATR-001 |
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

This SOP defines risk-based review of audit trails to detect unauthorised, unexplained or inappropriate changes to GxP records and configuration.

## 2. Review frequencies

| Review | Frequency/trigger | Owner |
|---|---|---|
| Record-level result/test audit trail | Before final approval for defined critical records | Reviewer |
| Specification/formula/master-data change trail | As part of change/effective approval | Master Data Reviewer/QA |
| Privileged access, role changes and vendor sessions | Monthly | System Owner + QA |
| System-wide critical-event trend | Quarterly | QA Data Integrity + System Owner |
| Event-based review | Incident, OOS/OOT, complaint, suspected DI issue or inspection | Assigned investigator |

## 3. Review procedure

1. Confirm review scope, period, objects, users and filters.
2. Verify the report/export criteria and completeness.
3. Examine critical changes, deletion attempts, repeated corrections, manual entries, result invalidation, unusual time patterns, role/configuration changes and vendor activity.
4. Compare reason with source record, procedure, ticket/change/OOS and business context.
5. Document reviewed population, exceptions, conclusion and reviewer signature.
6. Escalate unexplained or potentially unauthorised events immediately.

## 4. Exception classification

- **Critical:** suspected falsification, audit trail disabled/altered, unauthorised deletion or data loss.
- **Major:** unexplained critical result/spec/formula/role change or repeated control bypass.
- **Minor:** isolated documentation weakness with no record-integrity effect.
- **No issue:** event is justified, authorised and consistent with source evidence.

## 5. Escalation

Potential product impact triggers hold and QA investigation. Security concerns also notify IT Security. An isolated event may require deviation; systemic/repeated issues require problem/CAPA and risk reassessment.

## 6. Evidence retention

Retain report/export, filter criteria, reviewer annotation, linked investigation and approval. Review records follow the related GMP-record retention period.

## 7. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Input | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Input | QCL-2026-CAPA-001 | [CAPA Record and Effectiveness Check](062_CAPA_Record_and_Effectiveness_Check.md) |
| Input | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |
| Output | QCL-2027-ATR-001 | [Periodic Audit Trail Review Record](081_Periodic_Audit_Trail_Review_Record.md) |
| Output | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |
| Output | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |

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
