---
document_number: QCL-2026-DMT-001
title: "Data Migration Test and Reconciliation Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Verification"
version: "1.0"
effective_or_record_date: "2027-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "Business Process Owner"
approved_by: "QA Validation Manager"
---

# Data Migration Test and Reconciliation Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-DMT-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Verification |
| Version | 1.0 |
| Effective/record date | 2027-04-30 |
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

## 1. Objective

Demonstrate that the approved mapping and migration tooling preserve completeness, accuracy, relationships, metadata, attachments and retrievability.

## 2. Trial migration results

| Test | Scope | Population | Actual result | Outcome |
|---|---|---|---|---|
| DMT-001 | Trial extraction counts/checksums | 10,000 samples / 38,000 results / 2,000 attachments | Counts and source checksums captured | Pass |
| DMT-002 | Critical field mapping | 100% of 12 defined critical fields | No unexplained mismatch | Pass |
| DMT-003 | Attachments/special characters | 2,000 files incl. 24 special-character names | All binary hashes match after rule update | Pass after DEV-002 |
| DMT-004 | Relationships/audit trail | 10,000 sample-test-result relationships; 5,000 audit events | 100% referential integrity | Pass |
| DMT-005 | Archive-only retrieval | 200 stratified records, 50 attachments, 50 audit histories | All readable/retrievable and matched source | Pass |
| DMT-006 | Exception and rerun | 42 intentional exceptions | All dispositioned; rerun produced no duplicates | Pass |

## 3. Statistical and field verification

Critical fields were checked 100% for the trial population. A stratified sample of 1,200 noncritical fields had 1,200 matches after correction, exceeding the ≥99.5% criterion. Attachment hashes matched 100%.

## 4. Exception summary

DEV-002 covered unsupported filename characters. Storage names were normalized while original names remained in metadata; all binary hashes matched. No systemic mapping defect remained.

## 5. Conclusion

Migration tooling and mappings are acceptable for production execution using the approved plan and version `MAP-2.3`.

Migration test acceptance confirms that the tool, mapping and reconciliation method are suitable for final migration; it does not itself approve production cutover. The final migration shall repeat required count, critical-field, attachment, relationship and retrieval checks using the frozen source population and shall disposition every exception before go-live.

| Migration evidence focus | Acceptance expectation |
|---|---|
| Population control | Source extract count and selection criteria are approved |
| Critical field check | 100% match or approved exception for active critical records |
| Sampling | Sample design covers record type, age, status and source variation |
| Attachment integrity | Count and hash reconciliation confirm binary content unchanged |
| Exception disposition | Business/QA disposition exists for every unresolved mismatch |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Input | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Input | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | QCL-2026-PDM-001 | [Production Data Migration Execution and Reconciliation Record](073_Production_Data_Migration_Execution_and_Reconciliation_Record.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-04-30 | Initial approved fictional case version. |
