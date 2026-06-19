---
document_number: QCL-2026-CLA-001
title: "System Classification and Criticality Assessment"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Risk and Compliance"
version: "1.0"
effective_or_record_date: "2026-03-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV/Quality Risk Lead"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# System Classification and Criticality Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CLA-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Risk and Compliance |
| Version | 1.0 |
| Effective/record date | 2026-03-20 |
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

## 1. Classification method

Components are classified by their role and complexity. Industry categories are used as a planning aid, not as a substitute for GxP risk assessment.

Classification considers whether the component is standard infrastructure, configured commercial software, custom software, configured content, peripheral hardware or user-developed application. Criticality considers the worst credible impact on product quality, patient safety, data integrity, record availability and business continuity if the component fails or is misused.

## 2. Classification results

| Component | Classification | Configuration/customisation | Criticality | Validation implication |
|---|---|---|---|---|
| LabSphere LIMS/LES 8.4.2 | Configurable commercial application | Extensive workflow, master data, reports and security configuration | High | URS, configuration specification, risk-based OQ/PQ and traceability |
| QCL-IGW-01 OS/runtime | Infrastructure software | Standard hardened configuration | High supporting | Installation qualification and operational monitoring |
| SAP/eQMS/CDS connectors | Custom software/integration | Custom mappings, transformations and retry logic | High | Development plan, code review, unit and interface testing |
| Report templates/calculation rules | Configured/custom content | Site-specific logic | High | Specification, independent verification and regression |
| Barcode printers/scanners | Hardware/peripheral | Standard drivers and device mapping | Medium | Installation and workflow test |
| ArchiveVault | Configurable archive service | Retention/index configuration | High | Supplier assessment, qualification and retrieval test |
| Controlled spreadsheets | User-developed applications | Formula/macro dependent by file | Medium/High | Individual assessment, migration or retirement evidence |

## 3. Criticality evaluation

The application is business-critical and data-integrity-critical. An incorrect result, limit, signature or interface transfer could support an incorrect disposition. Loss of availability beyond eight hours delays QC release. Loss of historical records impairs inspection and product-quality investigations.

## 4. Validation strategy decision

Use a full risk-based lifecycle. Supplier standard tests may be leveraged for non-site-specific product functions. All site configuration, interfaces, calculations, roles, audit trails, signatures, migration and representative business processes require company-controlled verification.

## 5. Validation depth matrix

| Component type | Minimum company-controlled evidence |
|---|---|
| Configurable commercial application | Intended use, URS, configuration specification, risk assessment, OQ/PQ, traceability and VSR |
| Custom interface or transformation | Design specification, source/change control, code review, unit evidence, interface challenge and reconciliation |
| Configured calculation/report | Approved logic, independent calculation check, boundary/negative testing and regression coverage |
| Qualified infrastructure | Installation/configuration baseline, security hardening, monitoring, backup/restore and DR evidence |
| Peripheral/device integration | Installation check, device mapping, data-capture challenge and exception handling |
| User-developed application replacement | Inventory assessment, migration/retirement decision and evidence that uncontrolled use has stopped |

## 6. Supplier evidence leveraging limits

Supplier evidence may reduce duplicate testing for standard product functions only when version, configuration relevance, test independence, defect status and traceability are acceptable. It shall not replace site verification of intended use, site configuration, role/access design, interfaces, migrations, regulated reports, electronic signatures, audit trails or SOP-based business processes.

## 7. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Output | QCL-2026-PRA-001 | [Preliminary Risk Assessment](011_Preliminary_Risk_Assessment.md) |
| Output | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |
| Output | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV/Quality Risk Lead | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-20 | Initial approved fictional case version. |
