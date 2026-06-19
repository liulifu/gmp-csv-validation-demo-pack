---
document_number: QCL-2027-RST-001
title: "Periodic Restore Test Report"
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

# Periodic Restore Test Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-RST-001 |
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

## 1. Test date and scope

Periodic restore test executed 2027-12-05 using the 2027-12-04 23:45 CST recovery point. Scope included database, attachments, configuration, audit trail, signatures and interface status in an isolated recovery environment.

## 2. Results

| Check | Acceptance | Actual result | Outcome |
|---|---|---|---|
| Recovery point | Within 15-minute RPO | Restored to requested 23:45 point | Pass |
| Database/attachments | Complete and consistent | 250 selected records and 76 attachments reconciled | Pass |
| Audit trail/signatures | Readable, linked and protected | All selected events/signatures present | Pass |
| Application usability | Login, search, report and calculation functional | All checks pass | Pass |
| Access isolation | Recovery environment restricted | Only approved recovery team had access | Pass |
| Elapsed time | Technical restore within 8-hour objective | 3 h 06 min technical; 4 h 02 min incl. validation | Pass |

## 3. Conclusion

The backup set can restore complete regulated records within the required objectives. Next periodic restore is due by 2028-12-05 or after material architecture change.

## 4. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
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
| 1.0 | 2027-12-20 | Initial approved fictional case version. |
