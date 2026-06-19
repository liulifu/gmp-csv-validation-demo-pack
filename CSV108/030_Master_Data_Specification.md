---
document_number: QCL-2026-MDS-001
title: "Master Data Specification"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Design"
version: "1.0"
effective_or_record_date: "2026-10-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "Vendor Solution Architect"
approved_by: "QA CSV Lead"
---

# Master Data Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-MDS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Design |
| Version | 1.0 |
| Effective/record date | 2026-10-31 |
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

This document defines ownership, attributes, lifecycle and approval of master data that drives GxP processing.

## 2. Master-data register

| Master data | Critical attributes | Source/system | Owner | Control |
|---|---|---|---|---|
| Material/product | Code, name, dosage form, site, status | SAP interface; read-only in QCLabOne | ERP Master Data Owner | Per approved ERP change |
| Specification | Tests, methods, limits, effective dates | Controlled in QCLabOne | QC Specification Owner | Creator/reviewer/approver segregation |
| Test method reference | Method number/version, result type, units | Controlled in QCLabOne; scientific method in eDMS | QC Method Owner | Effective version only |
| Calculation formula | Formula, variables, units, rounding | Controlled in QCLabOne | QC Calculation Owner | Independent verification |
| Reagent/standard | Item, lot, expiry, potency, storage | QCLabOne | QC Reagent Steward | Status/expiry prevents use |
| Instrument/device | Asset ID, type, location, qualification status | Asset system feed/manual approved sync | QC Instrument Owner | Unqualified/expired device blocked |
| User role mapping | Corporate group to application role | Identity + QCLabOne | System Owner | Approved access request |
| Location | Lab, room, storage, EM location and grade | QCLabOne | QC/Facilities Owner | Version/effective date |
| Controlled reason list | Reason code, description, applicable object | QCLabOne | QA Data Integrity Owner | QA approval |
| Report template | Template ID/version/effective state | QCLabOne/eDMS | Report Owner | Verification before effective |

## 3. Lifecycle

Draft → review → approved/effective → superseded/obsolete. Historical versions are never overwritten. Bulk load uses approved template, validation rules, independent review and reconciliation.

## 4. Periodic review

Specifications, methods and calculations are reviewed through their scientific document lifecycle. Reagent/standard and instrument status is monitored daily. Roles and controlled reasons are reviewed quarterly/annually as defined in SOPs.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Output | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Output | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |
| Output | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | Vendor Solution Architect | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-31 | Initial approved fictional case version. |
