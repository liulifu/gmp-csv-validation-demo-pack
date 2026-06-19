---
document_number: QCL-2027-ATR-001
title: "Periodic Audit Trail Review Record"
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

# Periodic Audit Trail Review Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-ATR-001 |
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

## 1. Review period and scope

Quarterly system-wide audit-trail review for 2027-07-01 to 2027-09-30, plus privileged activity from go-live. Filters and exported report IDs are retained with this record.

## 2. Population and outcome

| Event category | Population | Review outcome | Exceptions |
|---|---|---|---|
| Result changes requiring reason | 1,284 | 1,284 justified and linked to review/OOS/correction | 0 unexplained |
| Specification/method/formula changes | 46 | 46 linked to approved change/master-data approval | 0 |
| Role/access changes | 37 | 36 routine; 1 ODV-004 | 1 closed |
| Vendor privileged sessions | 9 | 9 ticketed, time-limited and session-reviewed | 0 |
| Delete/purge attempts | 3 | All denied; training/test-related support checks | 0 malicious |
| Time/configuration changes | 8 | 8 approved change records | 0 |
| Failed signature attempts | 22 | User credential errors; no pattern/lockout concern | 0 |
| Interface reprocess events | 63 | All linked to queue reason/incident or duplicate test | 0 unexplained |

## 3. Detailed review observations

- Result corrections were mostly documented transcription/unit corrections and authorised OOS/retest activities.
- No audit-trail gap, disabled trail, altered timestamp or unexplained deletion was found.
- Three denied purge attempts were generated during approved administrator support verification and were correctly logged.
- The single excessive-role event was ODV-004; no GxP data change occurred during the 47-minute window.
- Repeated interface reprocessing was concentrated around a laboratory network outage and reconciled.

## 4. Conclusion

Audit-trail controls operated effectively. No product or data-integrity impact was identified. Continue quarterly trend review and record-level review before approval.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Input | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Input | QCL-2026-CAPA-001 | [CAPA Record and Effectiveness Check](062_CAPA_Record_and_Effectiveness_Check.md) |
| Input | SOP-QA-ATR-001 | [QCLabOne 2.0 Audit Trail Review SOP](068_Audit_Trail_Review_SOP.md) |
| Input | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Input | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Output | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
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
