---
document_number: QCL-2026-DMS-001
title: "Data Mapping, Cleansing and Transformation Specification"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Data Migration"
version: "1.0"
effective_or_record_date: "2026-10-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Data Migration Lead"
reviewed_by: "QC Data Owner"
approved_by: "QA CSV Lead"
---

# Data Mapping, Cleansing and Transformation Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-DMS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Data Migration |
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

This document defines field-level source-to-target mapping, cleansing, transformation, validation and exception rules.

## 2. Mapping table

| Source | Target | Type | Transformation | Validation |
|---|---|---|---|---|
| Legacy SAMPLE.SAMPLE_NO | Sample.SampleID | String | Preserve legacy ID in LegacyReference; target generates new QCL ID | Required/unique |
| SAMPLE.MATERIAL_CODE | Sample.MaterialCode | String | Trim; uppercase; validate against SAP master | Reject unmatched |
| SAMPLE.BATCH_NO | Sample.BatchNumber | String | Preserve leading zeros | Required |
| SAMPLE.RECEIVED_DATE | Sample.ReceiptTimestamp | Timestamp | Convert local legacy time to ISO 8601 +08:00 | No future date |
| TEST.TEST_CODE | TestAssignment.TestCode | String | Lookup mapping table M-TEST-01 | Reject unmapped |
| TEST.SPEC_VER | TestAssignment.SpecificationVersion | String | Map to approved target effective version/reference | Historical reference retained |
| RESULT.RESULT_VALUE | Result.NumericValue/TextValue | Decimal/text | Locale decimal conversion; no rounding | Type validation |
| RESULT.UNIT | Result.Unit | Controlled code | Map legacy unit synonyms to target code | Reject unknown |
| RESULT.STATUS | Result.Status | Enum | A=Approved, R=Rejected, P=Pending; preserve source status | Controlled |
| RESULT.APPROVED_BY | Signature.LegacyApprover | String | Retain legacy user display and ID; do not create new signature | Historical metadata |
| AUDIT.* | LegacyAuditEvent | Structured | Preserve event, old/new value, user, timestamp and reason | Count/retrieval checks |
| ATTACH.FILE_NAME | Attachment.Name | String | Normalize unsupported characters; retain original name metadata | DEV-002 rule |
| ATTACH.CONTENT | Attachment.Binary | Binary | Transfer unchanged; SHA-256 compare | 100% checksum |
| STAB.PULL_DATE | Stability.PullDate | Date | Preserve approved date/window | Required |
| EXCEL_ACTIVE_ROWS | Target master/transaction entities | Various | Only approved rows; formulas not migrated as logic | Independent review |

## 3. Cleansing rules

Duplicate legacy IDs are not merged automatically. Invalid codes, orphan records, impossible dates and missing required relationships enter the exception log. Business owners decide correction in source, target mapping, archive-only disposition or justified exclusion.

## 4. Attachment special-character rule

Unsupported filename characters are replaced with `_` for the target storage name; the original filename is retained in metadata. Binary content is not modified. Source and target SHA-256 hashes must match.

## 5. Approval and versioning

Mapping version `MAP-2.3` is the production-approved baseline. Changes after trial migration 2 require migration change control and repeat of affected reconciliation tests.

Mapping rules shall preserve meaning, provenance and auditability. Any transformation that changes format, code, unit, identifier, relationship or status requires business-owner approval and test evidence. Data that cannot be transformed without changing regulated meaning shall be excluded from migration and retained in the approved archive with documented retrieval path.

| Mapping control | Required review |
|---|---|
| Code translation | Source/target code list, retired code handling and owner approval |
| Unit conversion | Scientific rationale, precision/rounding rule and independent check |
| Relationship mapping | Parent/child linkage and orphan handling verified |
| Exclusion rule | Business/QA approval and archive/retrieval reference |
| Mapping version change | Impacted fields, repeat-test scope and approval recorded |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Input | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Output | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Output | QCL-2026-PDM-001 | [Production Data Migration Execution and Reconciliation Record](073_Production_Data_Migration_Execution_and_Reconciliation_Record.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Data Migration Lead | Completed |
| Reviewed by | QC Data Owner | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-31 | Initial approved fictional case version. |
