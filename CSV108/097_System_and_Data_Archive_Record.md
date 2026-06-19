---
document_number: QCL-2028-ARC-001
title: "System and Data Archive Record"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Operation"
version: "1.0"
effective_or_record_date: "2028-03-15"
case_status: "Completed/Closed in fictional operating record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "QA System Oversight"
---

# System and Data Archive Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-ARC-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Operation |
| Version | 1.0 |
| Effective/record date | 2028-03-15 |
| Case status | Completed/Closed in fictional operating record |

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

This record documents controlled archive transfers completed before Legacy LIMS retirement and the first QCLabOne archive pilot.

## 2. Archive batches

| Batch | Content | Population | Transfer date | Integrity result | Status |
|---|---|---|---|---|---|
| ARC-BATCH-001 | Legacy LIMS 2010–2014 | 38,420 packages | 2028-01-12 | 100% manifest/checksum | Accepted |
| ARC-BATCH-002 | Legacy LIMS 2015–2017 | 41,962 packages | 2028-01-26 | 100% manifest/checksum | Accepted |
| ARC-BATCH-003 | Legacy LIMS 2018–cutover archive copy | 32,222 packages | 2028-02-09 | 100% manifest/checksum | Accepted |
| ARC-BATCH-004 | Controlled Excel/paper index archive | 22 files / 9,420 images | 2028-02-16 | 100% count/checksum | Accepted |
| ARC-BATCH-005 | QCLabOne first closed-record archive pilot | 1,000 packages | 2028-02-23 | 100% manifest/retrieval | Accepted |

## 3. Storage and protection

ArchiveVault stores read-only packages with replicated encrypted copies and quarterly integrity scans. Search indexes include legacy sample ID, batch, material, test and date. Access is limited to Records Management, authorised QC/QA and inspection read-only roles.

## 4. Retrieval sampling

A stratified set of 600 legacy records and 100 attachments/audit histories was retrieved successfully; detailed evidence is in Document 103. QCLabOne pilot retrieval was also successful.

## 5. Conclusion

Archive transfers are complete and accepted for retirement planning.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Input | SOP-QA-ARC-001 | [Data Retention, Archiving and Record Retrieval SOP](070_Data_Retention_Archiving_and_Record_Retrieval_SOP.md) |
| Input | QCL-2026-PDM-001 | [Production Data Migration Execution and Reconciliation Record](073_Production_Data_Migration_Execution_and_Reconciliation_Record.md) |
| Output | QCL-2028-IRD-001 | [Inspection Readiness Dossier and Audit Response Record](098_Inspection_Readiness_Dossier_and_Audit_Response_Record.md) |
| Output | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA System Oversight | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2028-03-15 | Initial approved fictional case version. |
