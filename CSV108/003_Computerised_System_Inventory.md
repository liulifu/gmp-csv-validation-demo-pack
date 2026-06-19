---
document_number: CSI-SZ-001
title: "Site Computerised System Inventory"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "CSV Governance"
version: "1.0"
effective_or_record_date: "2026-01-15"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV Program Lead"
reviewed_by: "QA Validation Manager"
approved_by: "Site Quality Head"
---

# Site Computerised System Inventory

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | CSI-SZ-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | CSV Governance |
| Version | 1.0 |
| Effective/record date | 2026-01-15 |
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

This inventory is the controlled site register for systems supporting the QCLabOne 2.0 process. It records ownership, GxP impact, validation state and lifecycle status. The full site inventory is maintained in the eQMS; the table below is the approved project-relevant extract.

## 2. Inclusion criteria

A component is included when it creates, modifies, calculates, transmits, approves, reports, archives or retrieves GMP data; controls identity or access; provides qualified infrastructure; or must be retained/retired as part of the regulated process.

## 3. Inventory register

| ID | System/component | Version | Type | Hosting/location | GxP impact | Owner | Validation/lifecycle state |
|---|---|---|---|---|---|---|---|
| SYS-001 | QCLabOne 2.0 LIMS/LES | LabSphere LIMS/LES 8.4.2 | Configurable application | Vendor private cloud | High | QC System Owner | In validation / Production from 2027-06-15 |
| SYS-002 | QCL-IGW-01 Interface Gateway | Gateway 3.6.1 | Custom integration + infrastructure | On-site virtual server | High | IT System Owner | Qualified |
| SYS-003 | SAP S/4HANA QC Interface | SAP S/4HANA 2023 | Existing validated enterprise system | Corporate data centre | High | ERP Process Owner | Validated; interface impact assessed |
| SYS-004 | QualiTrack eQMS Interface | QualiTrack 5.6 | Existing validated quality system | Corporate private cloud | High | QA Process Owner | Validated; interface impact assessed |
| SYS-005 | ChromLink CDS/SDMS Result Interface | ChromLink 7.2 | Existing validated laboratory system | On-site data centre | High | QC Data Owner | Validated; interface tested |
| SYS-006 | Corporate Identity Service | AD FS 2022 | Qualified infrastructure | Corporate data centre | Medium | IT Security Owner | Qualified |
| SYS-007 | Legacy LIMS 6.2 | Legacy LIMS 6.2 / Oracle 12c | Legacy configurable application | On-site data centre | High | Legacy System Owner | Read-only; retirement planned |
| SYS-008 | Controlled QC Excel Registers | Office LTSC 2021 | User-developed applications | Controlled file share | Medium/High by use | QC Process Owners | Replacement/archival in progress |
| SYS-009 | Long-Term Archive Repository | ArchiveVault 4.1 | Configurable archive service | Vendor private cloud | High | Records Management Owner | Qualified |
| SYS-010 | Veeam Backup Platform | Veeam 12.1 | Qualified infrastructure | On-site DR centre | High support | IT Infrastructure Owner | Qualified |
| SYS-011 | Laboratory Balances/pH/TOC Interfaces | 24 devices, model list in ICS | Instrument interfaces | QC laboratories | High | QC Instrument Owner | Qualified/interface tested |
| SYS-012 | Barcode Printers and Scanners | 18 printers, 42 scanners | Peripheral devices | QC laboratories | Medium | QC Operations Owner | Verified |

## 4. Review and maintenance

The System Owner shall update the inventory after implementation, version change, hosting change, new interface, change of intended use, ownership transfer, periodic review or retirement. The next formal review for high-impact entries is due 2028-03-15 unless an earlier trigger occurs.

## 5. Key decisions

- QCLabOne is the official record system for sample metadata, LES execution, calculations, review/approval, audit trails and controlled reports.
- ChromLink CDS/SDMS remains the official source for chromatographic raw and processed source data. QCLabOne stores approved numerical results and a stable source link.
- ArchiveVault is the official long-term source for retired Legacy LIMS records and later archived closed records.
- Excel registers are assessed individually; no blanket “medium” classification is permitted.
- Identity and backup platforms are supporting infrastructure but are included because failure could compromise high-impact applications.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | SOP-CSV-001 | [Site Computerised System Lifecycle Management Procedure](001_CSV_Lifecycle_Management_Procedure.md) |
| Input | VMP-SZ-001 | [Site Validation Master Plan](002_Validation_Master_Plan.md) |
| Output | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Output | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | CSI-SZ-001-CHG-2028-03 | [Computerised System Inventory Update—Retired Status](107_Computerised_System_Inventory_Update_Retired_Status.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV Program Lead | Completed |
| Reviewed by | QA Validation Manager | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-01-15 | Initial approved fictional case version. |
