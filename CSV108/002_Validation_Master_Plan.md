---
document_number: VMP-SZ-001
title: "Site Validation Master Plan"
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

# Site Validation Master Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | VMP-SZ-001 |
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

## 1. Purpose and site validation policy

This Validation Master Plan describes how Suzhou Sterile Products Manufacturing Site governs qualification and validation. Computerised applications used in GMP operations shall be validated for intended use and supporting infrastructure shall be qualified. Scope and depth are based on documented risk, and retrospective validation is not accepted as a substitute for planned lifecycle evidence.

## 2. Site system portfolio

| Portfolio class | Examples | Site approach |
|---|---|---|
| High GxP applications | LIMS/LES, MES, eQMS, ERP quality modules, CDS/SDMS | System-specific validation plan, URS, risk, traceability, verification, VSR and annual review |
| GxP infrastructure | Identity, database, virtualisation, backup, network, archive | Qualification, configuration baseline, monitoring, restore/DR evidence |
| Configurable instruments | Chromatography, TOC, balances with electronic records | Instrument qualification plus software/data-integrity controls |
| User-developed applications | Critical spreadsheets, databases and scripts | Use-based risk assessment, specification, verification and controlled operation |
| Non-GxP tools | Administrative utilities with no regulated record/decision | Documented exclusion and basic IT controls |

## 3. Organisation

The Site Quality Head owns the validation governance model. Process Owners are accountable for intended use and business acceptance. System Owners maintain validated state. QA provides independent oversight. IT qualifies common infrastructure. Suppliers remain subject to formal agreements and oversight.

## 4. Planning principles

1. Every GxP system shall have an inventory record and named owner.
2. Validation deliverables may be combined where the rationale is documented and traceability remains clear.
3. Supplier documentation is leveraged only after assessment.
4. Critical functions receive explicit acceptance criteria and objective test evidence.
5. Data migration, electronic signatures, audit trails, interfaces and record retention receive dedicated controls where applicable.
6. Periodic review frequency is risk-based, normally annual for high GxP systems and every two years for medium-impact systems.
7. Significant change, repeated incident, supplier change or adverse trend may trigger revalidation.

Portfolio priority is assigned using GxP impact, patient/product risk, data criticality, regulatory commitment, business continuity tier, change complexity and inspection exposure. The CSV Program Lead maintains the ranked backlog and escalates any overdue high-impact system remediation to the Site Quality Council.

| Planning control | Minimum expectation |
|---|---|
| Validation strategy rationale | Documents why the selected lifecycle depth is adequate for intended use and risk |
| Supplier leveraging | Identifies which supplier records are reusable, which require site challenge and which are not accepted |
| Infrastructure dependency | Confirms qualified services, monitoring, backup, restore and security ownership before application release |
| Data integrity planning | Covers audit trail, e-signature, record retention, migration, archive and inspection retrieval where applicable |
| Deferred work | Requires QA-approved risk assessment, owner, due date and release impact statement |

## 5. 2026–2028 site validation programme

| Programme item | Owner | Target | Planned evidence |
|---|---|---|---|
| QCLabOne 2.0 implementation | QC System Owner | Go-live 2027-06-15 | Project validation plan, URS, design, IQ/OQ/PQ, migration, VSR |
| Legacy LIMS 6.2 retirement | Legacy System Owner | 2028-03-31 | Archive verification and retirement dossier |
| ChromLink CDS patch programme | QC Data Owner | 2027 Q3 | Patch assessment and regression |
| Critical spreadsheet remediation | QC Process Owners | 2027 Q4 | Inventory, risk, migration or controlled retirement |
| Annual site inventory review | CSV Program Lead | Each January | Approved inventory and overdue-action report |

## 6. Validation status reporting

Monthly status reports shall show planned/actual deliverables, overdue approvals, open high risks, test progress, defect/deviation ageing, training readiness and release risks. Quality escalation is required for any critical finding, unapproved production change, data loss or risk to record integrity.

The standard dashboard shall include green/amber/red status for deliverables, validation deviations, supplier actions, migration readiness, training, open change controls, environment readiness and release decision blockers. Amber items require a recovery owner and date. Red items require Steering Committee review and QA acknowledgement before the next lifecycle gate.

## 7. Acceptance metrics

| Metric | Site target |
|---|---|
| High-risk requirements with approved verification coverage | 100% |
| Critical/high validation deviations open at release | 0 |
| Production users trained and authorised before access | 100% |
| Annual periodic reviews completed by due date | ≥95%; no high GxP system >30 days overdue |
| Backup restore exercises completed for tier-1 systems | At least annually |

## 8. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | SOP-CSV-001 | [Site Computerised System Lifecycle Management Procedure](001_CSV_Lifecycle_Management_Procedure.md) |
| Output | CSI-SZ-001 | [Site Computerised System Inventory](003_Computerised_System_Inventory.md) |
| Output | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |
| Output | QCL-2026-MDL-001 | [Master Deliverable List and Schedule](016_Master_Deliverable_List_and_Schedule.md) |

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
