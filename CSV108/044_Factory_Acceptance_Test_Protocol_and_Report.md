---
document_number: QCL-2026-FAT-001
title: "Factory Acceptance Test Protocol and Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Verification"
version: "1.0"
effective_or_record_date: "2027-01-25"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "Business Process Owner"
approved_by: "QA Validation Manager"
---

# Factory Acceptance Test Protocol and Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-FAT-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Verification |
| Version | 1.0 |
| Effective/record date | 2027-01-25 |
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

## 1. Objective and environment

FAT verified the configured solution and custom integrations in the supplier-controlled FAT environment before site deployment. Protocol version 1.0 was approved on 2027-01-10 and executed 2027-01-16 to 2027-01-22.

## 2. FAT cases and results

| Test | Area | Acceptance | Result |
|---|---|---|---|
| FAT-001 | Tenant/module installation and version | Correct modules/version displayed | Pass |
| FAT-002 | Sample lifecycle/configured workflow | Normal and exception states operate | Pass |
| FAT-003 | Specification and effective-version control | Historical version preserved | Pass |
| FAT-004 | LES mandatory sequence and resources | Bypass prevented | Pass |
| FAT-005 | Calculation/rounding reference set | Matches independent expected results | Pass |
| FAT-006 | Role and segregation model | Positive/negative access correct | Pass |
| FAT-007 | Audit trail and reason-for-change | Events captured; one configuration observation | Pass with item transferred to site ATC |
| FAT-008 | Electronic signatures | Manifestation and binding correct | Pass |
| FAT-009 | SAP/eQMS/CDS simulated interfaces | Messages and errors processed | Pass after eQMS code fix |
| FAT-010 | Migration trial subset | Counts/critical fields/attachments reconcile | Pass |
| FAT-011 | Backup/restore demonstration | Record restored and reconciled | Pass |
| FAT-012 | Report templates | Content/pagination/signatures correct | Pass with low template defect |

## 3. Findings

DEF-003 and DEF-004 were identified, corrected and retested. One audit-trail configuration observation was transferred to formal site challenge testing because the final site event classification was not yet imported.

## 4. Exit criteria and conclusion

All FAT cases passed or were closed through controlled retest. Signed build packages and the FAT evidence were released for site installation/SAT.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Input | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Output | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-01-25 | Initial approved fictional case version. |
