---
document_number: QCL-2026-RFP-001
title: "RFI, RFP and Product Selection Record"
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

# RFI, RFP and Product Selection Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-RFP-001 |
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

## 1. Procurement objective

The project sought a configurable LIMS/LES capable of supporting regulated QC workflows, electronic records/signatures, data integrity, integrations, migration and vendor-hosted operation.

## 2. RFP mandatory requirements

| Area | Mandatory condition |
|---|---|
| GxP/CSV | Documented SDLC, configurable controls, audit trail, electronic signature and exportable evidence |
| Business | Chemistry, microbiology, stability, LES, specifications, calculations and reporting |
| Integration | REST/SFTP/message-queue support for SAP, eQMS, CDS and instruments |
| Data | Customer ownership, complete export, migration tools, archive compatibility |
| Security | Dedicated tenant, encryption, SSO/MFA, vulnerability and incident management |
| Service | 24×7 critical support, formal change notice, RTO/RPO and termination assistance |

## 3. Product evaluation

| Criterion | Weight | LabSphere | QualityLab Systems | OmniLIMS Cloud |
|---|---|---|---|---|
| Functional fit | 30% | 28 | 24 | 22 |
| Data integrity/Part 11 controls | 20% | 19 | 17 | 16 |
| Integration and migration | 15% | 14 | 12 | 11 |
| Supplier quality/validation evidence | 15% | 14 | 11 | 12 |
| Security/service resilience | 10% | 9 | 8 | 8 |
| Commercial/implementation risk | 10% | 8 | 9 | 7 |
| Weighted total | 100% | 92/100 | 81/100 | 76/100 |

## 4. Proof-of-concept results

LabSphere demonstrated SAP sample intake, LES sequence enforcement, CDS approved-result transfer, audit trail export, e-signature re-authentication, historical specification retention and a sample migration. Two gaps were identified: standard eQMS connector required custom idempotency logic, and the standard archive export required a site-specific metadata manifest. Both were accepted as controlled custom deliverables.

## 5. Selection decision

LabSphere Technologies Ltd. was selected on 2026-04-15, subject to supplier audit closure and execution of the quality/technical agreement. No product was selected solely on commercial score.

The selection score was not based on feature count alone. Mandatory compliance requirements were pass/fail; weighted scoring was applied only after mandatory items were met. Demonstrated audit-trail usability, supplier SDLC maturity, data-export capability, interface robustness and local support model were treated as critical differentiators.

| Evaluation dimension | Weighting approach |
|---|---|
| Mandatory GxP controls | Pass/fail; failure excludes product from award |
| Functional fit | Weighted against QC chemistry, microbiology, stability and LES workflows |
| Technical fit | Weighted against interfaces, cloud model, security and data export |
| Supplier maturity | Weighted using audit evidence, references, SDLC and support history |
| Lifecycle cost/risk | Weighted using implementation effort, customisation burden and retirement complexity |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CHA-001 | [QCLabOne 2.0 Project Charter](005_Project_Charter.md) |
| Input | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Input | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Output | QCL-2026-SQA-001 | [Supplier Qualification Assessment](018_Supplier_Qualification_Assessment.md) |
| Output | QCL-2026-SAR-001 | [Supplier Audit Report and CAPA](019_Supplier_Audit_Report_and_CAPA.md) |
| Output | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Output | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Output | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Output | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |

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
