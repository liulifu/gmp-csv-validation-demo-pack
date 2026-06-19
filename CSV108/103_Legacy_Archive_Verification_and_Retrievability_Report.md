---
document_number: QCL-2028-AVR-001
title: "Legacy Archive Verification and Retrievability Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Retirement"
version: "1.0"
effective_or_record_date: "2028-03-31"
case_status: "Approved/Closed in fictional retirement record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Legacy System Owner"
reviewed_by: "Records Management Owner"
approved_by: "Site Quality Head"
---

# Legacy Archive Verification and Retrievability Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-AVR-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Retirement |
| Version | 1.0 |
| Effective/record date | 2028-03-31 |
| Case status | Approved/Closed in fictional retirement record |

## Governing references

- China GMP (2010 Revision), Appendix: Computerised Systems (effective 1 December 2015)
- China GMP (2010 Revision), Appendix: Qualification and Validation (effective 1 December 2015)
- EU GMP Annex 11: Computerised Systems (2011)
- EU GMP Annex 15: Qualification and Validation (2015)
- 21 CFR Part 11: Electronic Records; Electronic Signatures
- FDA Guidance: Part 11, Electronic Records; Electronic Signatures — Scope and Application
- PIC/S PI 041-1: Good Practices for Data Management and Integrity in Regulated GMP/GDP Environments (2021)
- ISPE GAMP 5, Second Edition (2022), used as non-binding industry guidance

## 1. Objective

Demonstrate completeness, integrity, readability, searchability and long-term retrievability of Legacy LIMS records before shutdown.

## 2. Verification results

| Test area | Scope | Actual result | Outcome |
|---|---|---|---|
| Population reconciliation | 112,604 archive packages; 1,482,610 audit events; 24,806 attachments | 100% count/manifest agreement | Pass |
| Checksum verification | All package files | 100% SHA-256 verification | Pass |
| Stratified sample records | 600 records across 2010–2027, modules/statuses/products | 600/600 readable and matched source | Pass |
| Attachments | 150 selected incl. large/multilingual/special-character files | 150/150 open and hash match | Pass |
| Audit histories | 150 selected records | 150/150 complete, chronological and linked | Pass |
| Electronic approval metadata | 100 approved records | Name/ID/time/meaning/history available | Pass |
| Search performance | Sample/batch/material/test/date queries | Median 4.8 min; maximum 14 min; target <30 min | Pass |
| Inspection copy | 20 complete record packages | Readable export produced without altering source | Pass |
| Secondary copy recovery | 50 packages from secondary archive copy | 50/50 pass | Pass |

## 3. Sampling rationale

Sampling was stratified by year, product/material, chemistry/microbiology/stability, approved/rejected/cancelled status, attachment presence, audit-event complexity and migrated/archive-only disposition. High-risk and unusual records were deliberately over-sampled.

## 4. Exceptions

Three index labels used an obsolete test-name synonym. The records and data were correct; index aliases were added and re-tested. No missing/corrupt record, attachment or audit trail was found.

## 5. Acceptance

QC Data Owner, QA and Records Management accept ArchiveVault as the official source for Legacy LIMS records after retirement.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2028-ARC-001 | [System and Data Archive Record](097_System_and_Data_Archive_Record.md) |
| Input | QCL-2028-IRD-001 | [Inspection Readiness Dossier and Audit Response Record](098_Inspection_Readiness_Dossier_and_Audit_Response_Record.md) |
| Input | QCL-2028-RRA-001 | [Legacy LIMS Retirement Risk Assessment](100_Legacy_LIMS_Retirement_Risk_Assessment.md) |
| Input | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Output | QCL-2028-AIS-001 | [Legacy Access Revocation and Interface Shutdown Record](104_Legacy_Access_Revocation_and_Interface_Shutdown_Record.md) |
| Output | QCL-2028-DCL-001 | [Legacy System Decommissioning Checklist](105_Legacy_System_Decommissioning_Checklist.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Legacy System Owner | Completed |
| Reviewed by | Records Management Owner | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2028-03-31 | Initial approved fictional case version. |
