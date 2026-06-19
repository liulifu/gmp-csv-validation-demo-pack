---
document_number: QCL-2026-SEC-001
title: "Security, Access and Segregation of Duties Test Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Verification"
version: "1.0"
effective_or_record_date: "2027-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "Business Process Owner"
approved_by: "QA Validation Manager"
---

# Security, Access and Segregation of Duties Test Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-SEC-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Verification |
| Version | 1.0 |
| Effective/record date | 2027-04-30 |
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

## 1. Objective

Verify authentication, least privilege, account lifecycle, segregation of duties, privileged/vendor access and security-event evidence.

## 2. Results

| Test | Control | Scope | Result |
|---|---|---|---|
| SEC-001 | Role matrix positive/negative tests | 180 permission checks | 180 passed |
| SEC-002 | SoD conflicts | Admin + QC approval; analyst + reviewer; creator + master-data approval | All prohibited combinations blocked or detected |
| SEC-003 | Account lifecycle | Create/change/disable and evidence | Pass |
| SEC-004 | Failed login/security reports | Lockout and event details | Pass |
| SEC-005 | Service accounts | Non-interactive and least privilege | Pass |
| OQ-SEC-003 | Session lock | 15 minutes | Pass at 15:00 ±5 sec |
| OQ-SEC-004 | Vendor remote access | Ticket, MFA, 8-hour window, session log | Pass |

## 3. Notable evidence

No shared interactive account was enabled. Two break-glass accounts were sealed, monitored and excluded from routine role groups. Production administrators had no QC result-approval permission. Vendor access automatically disabled at the approved end time.

## 4. Conclusion

The approved access model satisfies the security and SoD requirements. Routine operation requires the access-request and review processes in Documents 078–080.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Output | QCL-2027-UAR-001 | [User Access Request and Approval Records](078_User_Access_Request_and_Approval_Records.md) |
| Output | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Output | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-04-30 | Initial approved fictional case version. |
