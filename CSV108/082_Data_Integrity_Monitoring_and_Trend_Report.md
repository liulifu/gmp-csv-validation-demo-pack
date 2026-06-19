---
document_number: QCL-2027-DIM-001
title: "Data Integrity Monitoring and Trend Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Operation"
version: "1.0"
effective_or_record_date: "2027-09-30"
case_status: "Completed/Closed in fictional operating record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "QA System Oversight"
---

# Data Integrity Monitoring and Trend Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-DIM-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Operation |
| Version | 1.0 |
| Effective/record date | 2027-09-30 |
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

## 1. Reporting period

Go-live 2027-06-15 through 2027-09-30.

## 2. Data-integrity indicators

| Indicator | Observed | Assessment | Trend |
|---|---|---|---|
| Manual critical-result entries | 318 | 0.9% of critical results; all independently verified | Stable |
| Post-signature corrections | 27 | 100% invalidated/re-reviewed | No adverse trend |
| Records with missing reason for critical change | 0 | Target 0 | Meets |
| Unexplained audit-trail events | 0 | Target 0 | Meets |
| Interface unreconciled messages at month-end | 0 | Target 0 | Meets |
| Backup failures not recovered within same day | 0 | Target 0 | Meets |
| OOS/OOT cases without valid eQMS link | 0 | Target 0 | Meets |
| Use of break-glass account | 0 | Target 0 | Meets |
| Vendor sessions without approved ticket | 0 | Target 0 | Meets |
| Late data entry >24 h without documented reason | 2 | Both outage forms reconciled/approved | No systemic trend |

## 3. Qualitative review

No evidence of shared credentials, backdating, discarded data, uncontrolled calculation, hidden repeat testing, missing OOS linkage or audit-trail suppression was identified. Two delayed entries were associated with approved outage forms and reconciled within one day.

## 4. Actions

Maintain targeted training on meaningful correction reasons; retain monthly privileged-access review; add role-assignment automated conflict alert following ODV-004; continue certificate-expiry monitoring improvement after INC-2027-014.

## 5. Conclusion

The system and associated procedures support ALCOA+ principles. Residual data-integrity risk remains acceptable.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | SOP-QA-ATR-001 | [QCLabOne 2.0 Audit Trail Review SOP](068_Audit_Trail_Review_SOP.md) |
| Input | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Input | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Input | QCL-2027-ATR-001 | [Periodic Audit Trail Review Record](081_Periodic_Audit_Trail_Review_Record.md) |
| Input | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |
| Output | QCL-2028-IRD-001 | [Inspection Readiness Dossier and Audit Response Record](098_Inspection_Readiness_Dossier_and_Audit_Response_Record.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA System Oversight | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-09-30 | Initial approved fictional case version. |
