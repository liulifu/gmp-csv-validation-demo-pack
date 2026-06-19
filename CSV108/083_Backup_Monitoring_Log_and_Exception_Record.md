---
document_number: QCL-2027-BML-001
title: "Backup Monitoring Log and Exception Record"
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

# Backup Monitoring Log and Exception Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-BML-001 |
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

## 1. Monitoring period

2027-06-15 through 2027-12-31.

## 2. Backup monitoring log

| Month | Required jobs | Exceptions | Disposition | Status |
|---|---|---|---|---|
| 2027-06 | 30/30 nightly; PITR continuous | 0 | Initial backup and monitoring stable | Pass |
| 2027-07 | 31/31 nightly; PITR continuous | 0 | No exception | Pass |
| 2027-08 | 31/31 after rerun | 1 | 2027-08-12 attachment backup failed at 82% storage threshold; capacity increased and rerun completed 10:42 | Closed INC-2027-009 |
| 2027-09 | 30/30 nightly; PITR continuous | 0 | No exception | Pass |
| 2027-10 | 31/31 nightly; PITR continuous | 0 | No exception | Pass |
| 2027-11 | 30/30 nightly; PITR continuous | 0 | No exception | Pass |
| 2027-12 | 31/31 nightly; PITR continuous | 0 | Annual restore test completed | Pass |

## 3. Exception INC-2027-009

The 2027-08-12 attachment backup stopped because the backup repository reached an 82% threshold and a quota action failed. No recovery point was lost because database PITR and the prior attachment backup remained valid. Capacity was increased; the job reran successfully the same day. Alert thresholds were revised to 70% warning/80% critical.

## 4. Review conclusion

All required backup periods were available. No exception exceeded the approved RPO or required QA product-impact action.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |
| Output | QCL-2027-RST-001 | [Periodic Restore Test Report](084_Periodic_Restore_Test_Report.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-DRE-001 | [Business Continuity and Disaster Recovery Exercise Report](095_Business_Continuity_and_DR_Exercise_Report.md) |

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
