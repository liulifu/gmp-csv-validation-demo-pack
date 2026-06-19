---
document_number: QCL-2026-CHA-001
title: "QCLabOne 2.0 Project Charter"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Project Initiation"
version: "1.0"
effective_or_record_date: "2026-01-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV Project Manager"
reviewed_by: "QC Business Process Owner"
approved_by: "Project Sponsor"
---

# QCLabOne 2.0 Project Charter

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CHA-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Project Initiation |
| Version | 1.0 |
| Effective/record date | 2026-01-30 |
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

## 1. Business need

The site currently uses Legacy LIMS 6.2, controlled spreadsheets and paper worksheets. Manual transcription, fragmented review evidence, inconsistent audit-trail capability and slow historical retrieval create compliance and operational burden. The project will implement LabSphere LIMS/LES 8.4.2 and retire the legacy platform after archive acceptance.

## 2. Objectives and measurable success criteria

| Objective | Success criterion |
|---|---|
| Implement the in-scope LIMS/LES platform | Approved production baseline and VSR by 2027-06-05 |
| Improve data integrity | 100% of critical result changes audit-trailed; no uncontrolled spreadsheet calculation for final results |
| Reduce transcription | Direct capture for all 6 balances, 4 pH meters, 2 TOC analyzers and approved CDS result transfer |
| Assure migration | 100% record-count reconciliation; 100% critical-field checks for active records; attachment hash reconciliation |
| Release trained users | 100% of production users complete role training before access |
| Control risk at go-live | No open critical/high validation deviation; all medium residual risks formally accepted |
| Retire legacy system | Archive retrieval acceptance and decommissioning completed by 2028-03-31 |

## 3. High-level scope

In scope: chemistry, microbiology, stability and environmental-monitoring sample management; LES; specifications; calculations; reporting; interfaces to SAP, eQMS, CDS/SDMS and selected instruments; migration/archive; training; go-live; first-year operation; Legacy LIMS retirement.

Out of scope: analytical-method validation, core validation of SAP/eQMS/CDS, replacement of instrument firmware, global rollout and mobile offline execution.

## 4. Budget and resources

| Item | Approved case value |
|---|---|
| Capital and implementation budget | CNY 12.8 million |
| Internal project effort | 18 core FTE equivalents across 24 months |
| Supplier services | Configuration, integrations, migration tooling, validation evidence and hypercare |
| Contingency | 10% of approved implementation budget |

The approved business case assumes measurable reduction in manual transcription, faster QC record retrieval, retirement of uncontrolled spreadsheet calculations, and lower inspection-response effort. Benefits shall be baselined before UAT and rechecked after six months of routine use. Compliance benefits are measured through audit-trail review effectiveness, deviation trends, record-retrieval performance and closure of legacy spreadsheet remediation actions.

## 5. Milestones

| Milestone | Target date |
|---|---|
| Project charter approved | 2026-01-30 |
| Supplier contract and qualification complete | 2026-04-30 |
| URS approved | 2026-06-30 |
| Design/configuration baseline approved | 2026-10-31 |
| FAT complete | 2027-01-25 |
| IQ/OQ/PQ complete | 2027-04-30 |
| Validation summary approved | 2027-06-05 |
| Production go-live | 2027-06-15 |
| Legacy LIMS retired | 2028-03-31 |

## 6. Principal risks

| Risk | Initial response |
|---|---|
| Legacy data mapping complexity | Profile early; execute two trial migrations and maintain an exception log |
| Instrument integration delay | Prioritise direct-capture instruments; retain controlled contingency process |
| Audit-trail configuration gap | Approve dedicated specification and execute challenge tests |
| Supplier cloud change | Quality agreement requires notice and impact assessment |
| User readiness | Role-based training, UAT and floor support during hypercare |

Critical dependencies include timely supplier audit closure, availability of QC subject-matter experts for design workshops and PQ, stable SAP/eQMS/CDS interface specifications, qualified production infrastructure, approved data-migration rules and completion of role-based SOP training. Any dependency that threatens validation release is escalated through the Steering Committee and recorded in the project risk log.

## 7. Governance and authority

The Project Sponsor authorises funding. The Steering Committee resolves schedule or scope conflicts. The BPO accepts business process suitability. QA independently accepts validation conclusions. The charter does not authorise production use.

Scope, budget or timeline changes that affect intended use, GxP controls, official record boundaries, migration population, interface commitments or go-live readiness require documented impact assessment before approval. Production use may be authorised only by the Go-Live and Production Release Approval after VSR approval and readiness checks.

## 8. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | VMP-SZ-001 | [Site Validation Master Plan](002_Validation_Master_Plan.md) |
| Input | CSI-SZ-001 | [Site Computerised System Inventory](003_Computerised_System_Inventory.md) |
| Input | QCL-2026-RACI-001 | [QCLabOne 2.0 CSV RACI and Responsibilities Matrix](004_CSV_RACI_and_Responsibilities_Matrix.md) |
| Output | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Output | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Output | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Output | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Output | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV Project Manager | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | Project Sponsor | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-01-30 | Initial approved fictional case version. |
