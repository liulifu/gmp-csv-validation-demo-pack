---
document_number: QCL-2027-UAR-002
title: "Periodic User Access Review Report"
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

# Periodic User Access Review Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-UAR-002 |
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

## 1. Review period

2027-06-15 through 2027-09-30. The review compared QCLabOne users/roles with HR status, department ownership, training, approved requests and privileged-access records.

## 2. Review summary

| Population | Count | Review result | Exception |
|---|---|---|---|
| Active named users | 102 | 102 matched HR/department/training | 0 |
| Disabled/terminated users | 7 | 7 disabled within required time | 0 |
| Privileged users | 6 | 6 justified and independently approved | 0 |
| Vendor accounts | 3 | All disabled except approved session windows | 0 |
| Service accounts | 8 | Owners current; non-interactive; secrets within rotation | 0 |
| Break-glass accounts | 2 | Sealed; no use; quarterly test documented | 0 |
| Role changes since go-live | 11 | 10 correct; 1 deviation ODV-004 addressed | 1 closed |

## 3. Actions

The ODV-004 role-assignment deviation was already contained and closed. Two users due to transfer on 2027-10-01 were scheduled for role change before effective transfer. No orphan, shared or unjustified standing vendor account was identified.

## 4. Conclusion

Access remains appropriate and current. Next all-user review is due 2027-12-31; privileged-account review remains monthly.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Input | QCL-2027-UAR-001 | [User Access Request and Approval Records](078_User_Access_Request_and_Approval_Records.md) |
| Output | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
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
| 1.0 | 2027-09-30 | Initial approved fictional case version. |
