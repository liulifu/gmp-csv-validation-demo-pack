---
document_number: QCL-2026-SDL-001
title: "Supplier Documentation Leveraging Assessment"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Supplier Management"
version: "1.0"
effective_or_record_date: "2026-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Supplier Quality Lead"
reviewed_by: "IT System Owner"
approved_by: "QA Validation Manager"
---

# Supplier Documentation Leveraging Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-SDL-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Supplier Management |
| Version | 1.0 |
| Effective/record date | 2026-04-30 |
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

This assessment determines which supplier documents may be used as validation evidence and where company-controlled verification remains necessary.

## 2. Assessment criteria

Evidence is evaluated for relevance to intended use, approved status, version match, traceability, test independence, clear expected/actual results, deviation control and availability for inspection.

## 3. Leveraging decision

| Supplier evidence | Relevance | Decision | Limitation/required site evidence |
|---|---|---|---|
| Supplier quality manual and SDLC | Relevant to standard product controls | Accepted as background evidence | Supplier-managed; audit confirmed |
| Product requirements/design baseline | Covers standard features but not site intended use | Partially leveraged | Site URS/design remains controlling |
| Release 8.4.2 qualification summary | Covers core platform regression | Leveraged for unchanged standard functions | Site critical functions still challenged |
| Cloud platform IQ/qualification | Covers platform, database and monitoring | Leveraged with site IQ confirmation | Dedicated-tenant identifiers and settings verified |
| Standard security test/penetration summary | Supports baseline confidence | Leveraged | Site SSO/RBAC/vendor-access tests required |
| Standard audit-trail test | Core audit engine | Partially leveraged | Site configuration and reason-for-change challenge required |
| Custom interface unit tests | Project-specific | Accepted after code review | Company FAT/SAT/interface test required |
| Supplier training materials | Product navigation | Leveraged as source | Site role/SOP training remains required |

## 4. Overall conclusion

Supplier evidence reduces duplicate testing for unchanged standard platform functions. It does not replace the company’s responsibility to define intended use, approve requirements and risk, verify site configuration/interfaces/migration, demonstrate representative business processes or accept release.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-SQA-001 | [Supplier Qualification Assessment](018_Supplier_Qualification_Assessment.md) |
| Input | QCL-2026-SAR-001 | [Supplier Audit Report and CAPA](019_Supplier_Audit_Report_and_CAPA.md) |
| Input | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Input | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Input | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |
| Output | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Output | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Output | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Supplier Quality Lead | Completed |
| Reviewed by | IT System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-30 | Initial approved fictional case version. |
