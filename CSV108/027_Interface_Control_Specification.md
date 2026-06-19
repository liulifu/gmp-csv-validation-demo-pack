---
document_number: QCL-2026-ICS-001
title: "Interface Control Specification"
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

# Interface Control Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-ICS-001 |
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

This specification defines interface ownership, protocol, data content, validation, error handling, reconciliation and security.

## 2. Interface register

| ID | Flow | Protocol | Message | Critical content | Error/reconciliation | Account |
|---|---|---|---|---|---|---|
| IF-01 | SAP → QCLabOne | HTTPS REST/JSON via gateway | SampleRequest v2 | Material, batch, plant, sample type, quantity, spec reference, request time | Immediate ACK; invalid/duplicate to exception queue | QCL-IGW service |
| IF-02 | QCLabOne → SAP | HTTPS REST/JSON | InspectionStatus v1 | Sample ID, inspection lot, completion status, disposition support, approved time | Retry 3 times; daily reconciliation | QCL-IGW service |
| IF-03 | QCLabOne ↔ QualiTrack eQMS | REST/JSON | QualityCase v1 | Event type OOS/OOT, sample/test/result IDs, summary; return case ID/status | Idempotency key prevents duplicate case | QCL-EQM service |
| IF-04 | ChromLink → QCLabOne | Message queue + HTTPS link | ApprovedResult v3 | Result, unit, sequence ID, method version, approval time, stable URL | Reject unapproved/mismatched context; exception queue | QCL-CDS service |
| IF-05 | Balance/pH/TOC → Gateway | Serial/TCP vendor protocol normalized to JSON | InstrumentResult v2 | Device ID, value, unit, timestamp, status, test context | Range/unit/device checks; no silent substitution | Device adapter accounts |
| IF-06 | Identity → QCLabOne | SAML 2.0 | Identity assertion | User ID, name, group/role claims, session | Deny on invalid/expired assertion | Corporate identity |
| IF-07 | QCLabOne → ArchiveVault | SFTP + manifest | RecordPackage v1 | PDF/A, XML/JSON metadata, attachments, audit trail, checksums | Manifest validation and transfer reconciliation | Archive service |

## 3. Common interface controls

- Every message has source system, destination, correlation ID, business key, created time, schema version and checksum.
- Duplicate messages are detected by idempotency key and do not create duplicate records.
- Mandatory-field, type, unit, range and context checks occur before business processing.
- Errors are retained in an exception queue; reprocessing requires authorised role and audit trail.
- Daily reconciliation compares sent, received, accepted, rejected and outstanding counts.
- No interface account is interactive; secrets are rotated through the approved vault.

## 4. Sample field mapping—CDS result

| CDS field | QCLabOne field | Rule |
|---|---|---|
| approvedResult | TestResult.NumericValue | Decimal; no rounding during transfer |
| unitCode | TestResult.Unit | Must match configured method unit |
| sequenceId | SourceRecord.SequenceID | Required and immutable |
| methodVersion | SourceRecord.MethodVersion | Required; mismatch blocks processing |
| approvalTimestamp | SourceRecord.ApprovedAt | ISO 8601 with offset |
| recordUrl | SourceRecord.Link | HTTPS stable link; authorised users only |
| status | SourceRecord.Status | Only APPROVED accepted |

Interface acceptance requires positive, negative and recovery scenarios. Each interface shall demonstrate normal processing, duplicate prevention, schema rejection, business-rule rejection, retry/reprocess behavior, reconciliation and auditability of manual intervention. Any manual correction to an interface message requires reason, owner and independent review.

| Interface control | Required verification |
|---|---|
| Idempotency | Duplicate business key/message ID does not create duplicate regulated record |
| Rejection handling | Invalid schema/unit/context is quarantined with actionable error |
| Reprocessing | Authorised user can reprocess only after documented disposition |
| Reconciliation | Source/target counts and outstanding messages are reviewed |
| Source traceability | Accepted record retains source ID, timestamp and source-system context |

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-SDP-001 | [Software Development and Source Control Plan](042_Software_Development_and_Source_Control_Plan.md) |
| Output | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Output | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Output | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |

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
