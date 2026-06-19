---
document_number: QCL-2026-VTP-001
title: "Validation Test Plan and Strategy"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Verification"
version: "1.0"
effective_or_record_date: "2027-02-28"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "Business Process Owner"
approved_by: "QA Validation Manager"
---

# Validation Test Plan and Strategy

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-VTP-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Verification |
| Version | 1.0 |
| Effective/record date | 2027-02-28 |
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

## 1. Test strategy

Testing is risk-based and combines supplier evidence, scripted company tests and representative UAT. High-risk controls receive explicit normal, boundary, negative and failure testing.

## 2. Test levels

| Level | Purpose | Primary evidence |
|---|---|---|
| IQ | Confirm approved components, versions, environment, infrastructure and documents | IQ-001–015 |
| OQ | Challenge configured functional and control behaviour | OQ-GEN/SMP/SPEC/LES/CALC/SEC/DI/OPS |
| Specialised verification | Interface, migration, access, audit trail, e-signature, backup, performance, DR and reports | IFT/SEC/ATC/EST/DMT/BRT/PLC/DRT/RPT |
| PQ/UAT | Demonstrate representative GMP processes with trained business roles | PQ-001–012 |

## 3. Test environment and data

Formal OQ/PQ uses validation environment `QCL-VAL-CN-E01`, matching the approved production release/configuration. Synthetic data set `TD-QCL-1.2` includes normal, boundary, invalid, OOS/OOT, multilingual, large-volume and migration scenarios.

## 4. Evidence rules

Each step records tester, date/time, actual result and evidence reference. Screenshots alone are insufficient where logs, database-independent reports, source/target comparisons or exported audit trails provide better evidence. Corrections to test records follow good documentation practice.

## 5. Defect/deviation classification

Critical—credible patient/product/data loss risk and no workaround; High—major GxP function fails; Medium—control gap with contained impact; Low—minor usability/documentation issue. Failed expected results require a defect and, where protocol execution deviates, a validation deviation.

## 6. Entry/exit criteria

Entry: approved URS/design/FRA/scripts, stable build, trained testers and controlled data. Exit: all required tests executed, no open Critical/High item, Medium items resolved or accepted, traceability complete and test summary approved.

## 7. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |
| Input | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-RTM-001 | [Initial Requirements Traceability Matrix](039_Initial_Requirements_Traceability_Matrix.md) |
| Input | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Input | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-PQ-001 | [Performance Qualification and User Acceptance Test Report](050_Performance_Qualification_and_UAT_Report.md) |
| Output | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Output | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Output | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Output | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Output | QCL-2026-EST-001 | [Electronic Signature Test Report](055_Electronic_Signature_Test_Report.md) |
| Output | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Output | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Output | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Output | QCL-2026-RPT-001 | [Report, Print and Export Verification Report](059_Report_Print_and_Export_Verification_Report.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-CAPA-001 | [CAPA Record and Effectiveness Check](062_CAPA_Record_and_Effectiveness_Check.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-02-28 | Initial approved fictional case version. |
