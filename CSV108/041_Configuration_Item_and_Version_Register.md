---
document_number: QCL-2026-CIR-001
title: "Configuration Item and Version Register"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Build and Installation"
version: "1.0"
effective_or_record_date: "2026-12-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "IT System Owner"
reviewed_by: "Vendor Technical Lead"
approved_by: "QA CSV Lead"
---

# Configuration Item and Version Register

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CIR-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Build and Installation |
| Version | 1.0 |
| Effective/record date | 2026-12-20 |
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

This register identifies controlled software, configuration, code, templates and schemas that form the validated production baseline.

## 2. Configuration-item register

| CI ID | Item | Approved version | Location | Identifier/checksum | Owner | Change control |
|---|---|---|---|---|---|---|
| CI-001 | LabSphere LIMS/LES | 8.4.2-HF1 | Production/Validation | Supplier release package | System Owner | QCL-2026 |
| CI-002 | PostgreSQL managed database | 15.5 | Production | Supplier platform | Supplier Cloud Owner | QCL-2026 |
| CI-003 | Interface Gateway | 3.6.1 | QCL-IGW-01 | MSI SHA-256 73bc...11af | IT System Owner | QCL-2026 |
| CI-004 | Windows Server | 2022 build 20348 | QCL-IGW-01 | Corporate golden image 2026.11 | IT Infrastructure | QCL-2026 |
| CI-005 | SAP connector | 2.1.0 | Gateway | Git tag qcl-sap-v2.1.0 | Integration Lead | QCL-2026 |
| CI-006 | eQMS connector | 1.4.1 | Gateway | Git tag qcl-eqm-v1.4.1 | Integration Lead | QCL-2026 |
| CI-007 | CDS connector | 2.3.0 | Gateway | Git tag qcl-cds-v2.3.0 | Integration Lead | QCL-2026 |
| CI-008 | Instrument adapters | 3.6.1 | Gateway | Config set INST-24-1.0 | IT/QC Instrument Owner | QCL-2026 |
| CI-009 | Site configuration package | 1.0 | Production | QCL-CONFIG-1.0 checksum 51aa...b2e7 | System Owner | QCL-2026 |
| CI-010 | Report template package | 1.0 | Production | QCL-RPT-1.0 | Report Owner | QCL-2026 |
| CI-011 | Calculation package | 1.0 | Production | QCL-CALC-1.0 | QC Calculation Owner | QCL-2026 |
| CI-012 | Role/access package | 1.0 | Production | QCL-RBAC-1.0 | System Owner | QCL-2026 |
| CI-013 | Archive package schema | 1.0 | Production/Archive | RecordPackage v1 | Records Management | QCL-2026 |
| CI-014 | Production baseline manifest | 1.0 | eDMS | QCL-PROD-BL-1.0 | System Owner | QCL-2026 |

## 3. Baseline rule

Any change to a listed item requires approved change control, version update, impact assessment and verification. Emergency security changes may use the emergency procedure but must be retrospectively documented within one business day.

Configuration items are grouped by validation impact. Critical items influence regulated records, calculations, audit trails, signatures, access, interfaces, migration, backup/recovery or retention. Supporting items influence operation or monitoring. Informational items document context but do not alter GxP behavior. The impact group drives approval and regression expectations.

| Item impact group | Change expectation |
|---|---|
| Critical GxP | QA-reviewed impact assessment and targeted regression before release |
| Supporting validated state | System Owner approval and operational verification |
| Infrastructure dependency | IT owner approval and qualification/monitoring evidence |
| Informational | Version/update record with no regression unless linked impact is identified |

## 4. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-RCS-001 | [Report and Calculation Specification](029_Report_and_Calculation_Specification.md) |
| Input | QCL-2026-MDS-001 | [Master Data Specification](030_Master_Data_Specification.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Output | QCL-2027-PAT-003 | [Patch and Upgrade Impact Assessment](089_Patch_and_Upgrade_Impact_Assessment.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | IT System Owner | Completed |
| Reviewed by | Vendor Technical Lead | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-12-20 | Initial approved fictional case version. |
