---
document_number: QCL-2026-TSR-001
title: "Test Summary Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Test Management"
version: "1.0"
effective_or_record_date: "2027-06-05"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# Test Summary Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-TSR-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Test Management |
| Version | 1.0 |
| Effective/record date | 2027-06-05 |
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

## 1. Scope

This report summarises formal qualification/validation execution from FAT through PQ and specialised verification.

## 2. Test execution summary

| Type | Planned | Executed | Open failed | Conclusion |
|---|---|---|---|---|
| Audit trail | 5 | 5 | 0 | Pass |
| Backup/Restore | 4 | 4 | 0 | Pass |
| DR/Failover | 4 | 4 | 0 | Pass |
| E-signature | 4 | 4 | 0 | Pass |
| IQ | 15 | 15 | 0 | Pass |
| Interface | 10 | 10 | 0 | Pass |
| Migration | 6 | 6 | 0 | Pass |
| OQ | 25 | 25 | 0 | Pass |
| PQ/UAT | 12 | 12 | 0 | Pass |
| Performance | 4 | 4 | 0 | Pass |
| Report | 4 | 4 | 0 | Pass |
| Security | 5 | 5 | 0 | Pass |

## 3. Issue summary

- Defects: 6 total; 0 Critical/High; all closed.
- Validation deviations: 4 total; all closed.
- CAPA: 1 validation-process CAPA; implemented and later effectiveness-checked.
- No unexplained data mismatch, lost record, uncontrolled signature or open high risk remained.

## 4. Acceptance criteria

All 98 catalogue tests were executed and passed after controlled correction/retest where noted. All Must URS have passing evidence. Performance, restore and DR targets were achieved.

## 5. Conclusion

Testing is complete and supports approval of final traceability and the Validation Summary Report.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Input | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Input | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Input | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Input | QCL-2026-PQ-001 | [Performance Qualification and User Acceptance Test Report](050_Performance_Qualification_and_UAT_Report.md) |
| Input | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Input | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Input | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Input | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Input | QCL-2026-EST-001 | [Electronic Signature Test Report](055_Electronic_Signature_Test_Report.md) |
| Input | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Input | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Input | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Input | QCL-2026-RPT-001 | [Report, Print and Export Verification Report](059_Report_Print_and_Export_Verification_Report.md) |
| Input | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |
| Input | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Input | QCL-2026-CAPA-001 | [CAPA Record and Effectiveness Check](062_CAPA_Record_and_Effectiveness_Check.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-06-05 | Initial approved fictional case version. |
