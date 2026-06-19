---
document_number: SOP-CSV-001
title: "Site Computerised System Lifecycle Management Procedure"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "CSV Governance"
version: "1.0"
effective_or_record_date: "2025-12-15"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV Program Lead"
reviewed_by: "QA Validation Manager"
approved_by: "Site Quality Head"
---

# Site Computerised System Lifecycle Management Procedure

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | SOP-CSV-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | CSV Governance |
| Version | 1.0 |
| Effective/record date | 2025-12-15 |
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

This procedure defines the site lifecycle controls for GxP computerised systems. It ensures that applications are selected, specified, configured, verified, released, operated, changed and retired using documented quality risk management. The procedure applies to both applications and the qualified infrastructure on which they depend.

## 2. Scope

The procedure applies to systems that create, modify, calculate, transmit, approve, report, archive or retrieve GMP data at Suzhou Sterile Products Manufacturing Site. It includes vendor-hosted services, configurable commercial applications, custom integrations, laboratory instruments, spreadsheets used for GxP decisions, archive repositories and legacy systems.

The procedure does not replace analytical method validation, process validation, equipment qualification or information-security procedures; it defines how those controls interface with CSV.

## 3. Definitions

| Term | Definition |
|---|---|
| Computerised system | The application, hardware, infrastructure, procedures, people and data that together perform a regulated function. |
| Process Owner | The manager accountable for the regulated business process and fitness for intended use. |
| System Owner | The manager accountable for the system lifecycle and maintenance of the validated state. |
| Validation | Documented evidence that the system consistently fulfils approved requirements for its intended use. |
| Critical data | Data used to make or support decisions affecting patient safety, product quality or data integrity. |
| Electronic record | A regulated record created, modified, maintained, archived, retrieved or transmitted electronically. |
| Validated state | The condition in which approved requirements, configuration, procedures, training and evidence remain current and effective. |

## 4. Responsibilities

| Role | Minimum responsibility |
|---|---|
| Site Quality Head | Approves the site CSV framework and accepts release or retirement quality conclusions. |
| QA Validation Manager | Provides independent quality oversight, approves risk-based validation strategy and verifies closure of critical issues. |
| Process Owner | Defines intended use and requirements, supplies qualified users and accepts business-process performance. |
| System Owner | Maintains inventory, access, configuration, incidents, changes, periodic review and retirement. |
| IT Owner | Qualifies infrastructure and controls security, backup, restore, monitoring and disaster recovery. |
| Supplier | Provides controlled product, services, documentation, defect resolution and change/security notifications under agreement. |
| CSV Lead | Coordinates deliverables, traceability, test governance and validation reporting. |

## 5. Procedure

### 5.1 Inventory and GxP assessment

Every system shall be entered in the site inventory before regulated use. The owner shall document intended use, data handled, interfaces, hosting model, GxP impact, validation status, supplier and review date. A system is GxP-relevant when failure could affect product quality, patient safety, regulated decisions or the integrity/availability of required records.

### 5.2 Classification and risk-based lifecycle

Software and components shall be classified by complexity and degree of configuration/customisation. Validation depth shall be determined from intended use, GxP impact, data criticality, system complexity, supplier capability and failure risk. Low-risk functions may use concise scripted or unscripted assurance evidence; high-risk functions require pre-approved acceptance criteria and objective records.

### 5.3 Supplier controls

Supplier competence and reliability shall be assessed before selection. Formal agreements shall define responsibility for hosting, configuration, support, security, backup, incident notification, change notification, audit access, data return and service termination. Supplier evidence may be leveraged only after a documented assessment of relevance, independence, traceability and execution quality.

### 5.4 Requirements, design and configuration

Requirements shall be uniquely identified, testable and linked to intended use and risk. Design and configuration records shall describe architecture, data flows, interfaces, roles, audit trails, electronic signatures, calculations, reports, backup, continuity and migration. Production configuration shall be established as an approved baseline.

### 5.5 Verification

Verification shall cover installation, functional operation and representative end-to-end use. Testing shall include normal, boundary, negative and failure-recovery scenarios according to risk. Deviations and defects shall be recorded, investigated and closed or formally accepted before release. Requirements, risks, design and tests shall remain traceable.

### 5.6 Release

Release requires an approved validation summary, completed training, effective procedures, accepted migration, verified production baseline, support readiness and an assessment of open items. No critical defect or unresolved high data-integrity risk may remain.

### 5.7 Operation and maintenance

The System Owner shall maintain the validated state through controlled access, audit-trail review, backup monitoring, incident/problem management, change control, patch assessment, supplier oversight, security monitoring and periodic review. Significant changes shall trigger risk assessment and proportionate regression or revalidation.

### 5.8 Retirement

Retirement shall be planned before disabling the system. Required records, metadata, audit trails, attachments and signatures shall remain readable, retrievable and protected for the retention period. Access and interfaces may be removed only after archive acceptance and business/quality approval.

## 6. Lifecycle gates

| Gate | Minimum entry criteria | Exit decision |
|---|---|---|
| G0 — Initiate | Approved business need and named owner | Project authorised and inventory entry created |
| G1 — Define | Approved scope, intended use and process description | GxP/classification/risk baseline accepted |
| G2 — Design | Approved URS and supplier strategy | Design/configuration baseline accepted |
| G3 — Verify | Installed build and approved test plan | Required tests complete; deviations dispositioned |
| G4 — Release | VSR, training, SOPs, migration and support ready | Quality release to production |
| G5 — Operate | Approved baseline and operational controls | Validated state confirmed by periodic review |
| G6 — Retire | Approved archive and retirement plan | System decommissioned; records remain available |

## 7. Records generated

| Record | Owner | Retention rule |
|---|---|---|
| System inventory and assessments | System Owner | System life plus applicable record-retention period |
| Requirements, design, risk and test evidence | CSV Lead | System life plus applicable record-retention period |
| Access, audit, backup, incident and change records | System Owner | Per GMP record schedule; not less than the related regulated record |
| Validation and retirement dossier index | QA Validation | Permanent index; underlying records per retention schedule |

## 8. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Output | VMP-SZ-001 | [Site Validation Master Plan](002_Validation_Master_Plan.md) |
| Output | CSI-SZ-001 | [Site Computerised System Inventory](003_Computerised_System_Inventory.md) |
| Output | QCL-2026-RACI-001 | [QCLabOne 2.0 CSV RACI and Responsibilities Matrix](004_CSV_RACI_and_Responsibilities_Matrix.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV Program Lead | Completed |
| Reviewed by | QA Validation Manager | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2025-12-15 | Initial approved fictional case version. |
