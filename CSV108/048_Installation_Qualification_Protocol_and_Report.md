---
document_number: QCL-2026-IQ-001
title: "Installation Qualification Protocol and Report"
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

# Installation Qualification Protocol and Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-IQ-001 |
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

IQ verified that the approved software, infrastructure, environment, connectivity, documents and controls were installed/configured as specified.

## 2. Preconditions

Approved build record, configuration-item register, architecture design, supplier qualification and SAT were available. The validation environment was stable and administrative access was controlled.

## 3. Executed IQ tests

| Test ID | Test | Type | Result |
|---|---|---|---|
| IQ-001 | Verify approved cloud tenant, production URL and environment identification | IQ | Pass |
| IQ-002 | Verify application version 8.4.2-HF1 and license modules | IQ | Pass |
| IQ-003 | Verify QCL-IGW-01 server OS, CPU, memory, disk and hardening | IQ | Pass |
| IQ-004 | Verify PostgreSQL managed database service and encryption settings | IQ | Pass |
| IQ-005 | Verify corporate identity federation and time synchronization | IQ | Pass |
| IQ-006 | Verify network routes, firewall rules and TLS certificates | IQ | Pass |
| IQ-007 | Verify backup jobs, retention and monitoring configuration | IQ | Pass |
| IQ-008 | Verify antivirus/EDR and vulnerability baseline on gateway | IQ | Pass |
| IQ-009 | Verify production, validation and training environment segregation | IQ | Pass |
| IQ-010 | Verify installed barcode printers, scanners and drivers | IQ | Pass |
| IQ-011 | Verify interface service accounts and secret storage | IQ | Pass |
| IQ-012 | Verify application log and audit log storage | IQ | Pass |
| IQ-013 | Verify approved configuration package checksum | IQ | Pass |
| IQ-014 | Verify document and supplier evidence availability | IQ | Pass |
| IQ-015 | Verify restore and DR procedures are available and approved | IQ | Pass |

## 4. Key actual evidence

- Application version displayed `8.4.2-HF1`.
- Gateway displayed Windows Server 2022 build 20348 and Gateway 3.6.1.
- Site configuration checksum matched `QCL-CONFIG-1.0`.
- Time synchronized to corporate NTP within 2 seconds.
- TLS certificates, firewall rules, SAML metadata, monitoring and backup jobs matched design.
- Production, validation and training environments were segregated.

## 5. Deviations and conclusion

No IQ deviation remained open. DEF-006 had already been corrected during SAT. All 15 IQ cases passed; installation is acceptable for OQ/PQ.

IQ acceptance is limited to installation, environment segregation, baseline verification and supporting infrastructure readiness. Functional suitability remains covered by OQ/PQ. The IQ evidence package shall allow a reviewer to identify the exact environment, installed version, checksum, configuration package, qualified infrastructure services and any dependency that was leveraged rather than retested.

| IQ evidence check | Acceptance expectation |
|---|---|
| Environment identity | Tenant/server/environment name is visible in evidence |
| Version/baseline | Installed version and checksum match approved build/configuration records |
| Infrastructure dependency | Backup, monitoring, time sync, logging and security controls are active |
| Segregation | Validation/training/production environments are separated |
| Exception closure | Build or installation exceptions are closed or impact-assessed |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Input | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Input | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |

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
