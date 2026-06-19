---
document_number: QCL-2026-PBL-001
title: "Production Baseline and Approved Configuration Record"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Release"
version: "1.0"
effective_or_record_date: "2027-06-15"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "Site Quality Head"
---

# Production Baseline and Approved Configuration Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-PBL-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Release |
| Version | 1.0 |
| Effective/record date | 2027-06-15 |
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

This record is the authoritative approved production baseline at go-live.

## 2. Baseline manifest

| Item | Approved version/identifier | Verification |
|---|---|---|
| Application | LabSphere LIMS/LES 8.4.2-HF1 | Supplier release signature verified |
| Tenant | QCL-PROD-CN-E01 | Production banner/URL verified |
| Site configuration | QCL-CONFIG-1.0-R1 | SHA-256 9d8a...c4f2 |
| Role/access package | QCL-RBAC-1.0 | Role export checksum recorded |
| Calculation package | QCL-CALC-1.0 | Independent reference set passed |
| Report package | QCL-RPT-1.0-R1 | RPT regression passed |
| SAP connector | 2.1.0 | Signed tag/build |
| eQMS connector | 1.4.1 | Signed tag/build |
| CDS connector | 2.3.0 | Signed tag/build |
| Instrument gateway/adapters | Gateway 3.6.1 / INST-24-1.0 | 24 endpoints verified |
| Gateway OS | Windows Server 2022 build 20348 | Hardening baseline 2026.11 |
| Database | PostgreSQL 15.5 managed | Encryption/PITR verified |
| Archive schema | RecordPackage v1 | Archive transfer/retrieval passed |
| Monitoring/backup | Dashboard set MON-QCL-1.0 / backup policy BAK-QCL-1.0 | Alerts and first backup passed |

## 3. Baseline checksum and export

The combined baseline manifest is `QCL-PROD-BL-1.0`, SHA-256 `b5ea8d7c...51ad`. Configuration, role, calculation and report exports are stored in the controlled release repository and eDMS.

## 4. Change control

Any difference from this baseline is an operational change and must be recorded in the CI register and change record. Monitoring-only data changes do not alter the baseline unless configuration is changed.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Input | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Input | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Input | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Input | QCL-2026-PDM-001 | [Production Data Migration Execution and Reconciliation Record](073_Production_Data_Migration_Execution_and_Reconciliation_Record.md) |
| Input | QCL-2026-PRC-001 | [Production Readiness Checklist](074_Production_Readiness_Checklist.md) |
| Output | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Output | QCL-2027-PAT-003 | [Patch and Upgrade Impact Assessment](089_Patch_and_Upgrade_Impact_Assessment.md) |
| Output | QCL-2027-REG-003 | [Regression Test Plan and Report](090_Regression_Test_Plan_and_Report.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-06-15 | Initial approved fictional case version. |
