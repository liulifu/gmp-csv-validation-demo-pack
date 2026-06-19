---
document_number: QCL-2026-IUS-001
title: "QCLabOne 2.0 Intended Use Statement"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Project Initiation"
version: "1.0"
effective_or_record_date: "2026-02-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV Project Manager"
reviewed_by: "QC Business Process Owner"
approved_by: "Project Sponsor"
---

# QCLabOne 2.0 Intended Use Statement

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-IUS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Project Initiation |
| Version | 1.0 |
| Effective/record date | 2026-02-20 |
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

## 1. Formal intended-use statement

QCLabOne 2.0 LIMS/LES is intended to be the controlled GMP computerised system for managing QC laboratory sample lifecycle, approved electronic laboratory execution, result calculation, review, approval, reporting, audit trails, electronic signatures and operational retrieval at Suzhou Sterile Products Manufacturing Site.

It supports quality-control evidence used for material disposition, batch-release support, stability evaluation, environmental-monitoring review and regulatory inspection. It is a high GxP-impact system.

## 2. Official record boundaries

| Record/data | Official source | QCLabOne responsibility |
|---|---|---|
| Sample identity, custody, assignments and status | QCLabOne | Create, control, retain and report |
| LES observations, manual entries and calculations | QCLabOne | Official electronic test record |
| Chromatographic raw/processed data | ChromLink CDS/SDMS | Store approved numeric result and stable source link; do not replace CDS raw data |
| OOS/OOT investigation record | QualiTrack eQMS | Create/link case and display case status; eQMS remains official investigation record |
| Material/batch master and final ERP release status | SAP | Receive source data and return QC disposition support; QCLabOne is not ERP batch-release system |
| Retired Legacy LIMS records | ArchiveVault after acceptance | Provide searchable index/link and inspection retrieval |

## 3. Users and approved activities

| Role | Approved intended activities |
|---|---|
| Analyst | Receive/execute assigned work, capture data, review own entry and electronically submit |
| Reviewer | Review source data, calculation, deviations and audit trail; electronically review |
| QC Supervisor | Assign work, resolve workflow exceptions and approve results where authorised |
| QA Reviewer | Review critical audit trails/OOS links and approve defined quality decisions |
| System Administrator | Maintain approved configuration, roles and controlled lists under change control; no routine final-result approval |
| IT Support | Support infrastructure, monitoring, backup/restore, security and incidents; no routine content editing |
| Vendor Support | Time-limited approved support only; no autonomous production configuration change |

## 4. Not intended uses

- It does not validate analytical methods or replace method-transfer evidence.
- It does not serve as the official source for chromatographic raw data.
- It does not perform final ERP batch release.
- It does not allow uncontrolled spreadsheet calculations to determine final GMP results.
- It does not store patient or clinical-subject data.
- It does not authorise retirement of legacy records before archive acceptance.

## 5. Fitness-for-use criteria

The system is fit for intended use when the 72 approved URS are traced to risk controls and passing verification; migration and archive criteria are met; procedures/training are effective; production configuration is baselined; and the VSR confirms no unacceptable residual risk.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CHA-001 | [QCLabOne 2.0 Project Charter](005_Project_Charter.md) |
| Input | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Output | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Output | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Output | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Output | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Output | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Output | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV Project Manager | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | Project Sponsor | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-20 | Initial approved fictional case version. |
