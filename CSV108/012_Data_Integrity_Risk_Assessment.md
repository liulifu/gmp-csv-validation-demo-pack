---
document_number: QCL-2026-DIRA-001
title: "Data Integrity Risk Assessment"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Risk and Compliance"
version: "1.0"
effective_or_record_date: "2026-03-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV/Quality Risk Lead"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# Data Integrity Risk Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-DIRA-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Risk and Compliance |
| Version | 1.0 |
| Effective/record date | 2026-03-20 |
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

## 1. Objective and method

This assessment evaluates the complete data lifecycle using ALCOA+ principles: attributable, legible, contemporaneous, original, accurate, complete, consistent, enduring and available. “C” means completeness, “A” attributable, “Cont” contemporaneous, “O” original, “Acu” accurate, “Cns” consistent, “E” enduring and “Av” available.

## 2. Data lifecycle inventory and risks

| ID | Data | Lifecycle stage | Failure mode | ALCOA+ | Controls | Residual risk |
|---|---|---|---|---|---|---|
| DIRA-01 | SAP sample request | Creation/transmission | Incorrect source data or duplicate message | C | A,C | Unique message ID, validation, exception queue, reconciliation | Medium |
| DIRA-02 | Sample ID/barcode | Creation/printing | Duplicate or mis-associated identity | A,C,O | Unique sequence, barcode verification, chain-of-custody | Low |
| DIRA-03 | Sample receipt record | Creation/modification | Backdating or incomplete receipt information | A,C,Cont | Mandatory fields, timestamp, audit trail, reason for change | Low |
| DIRA-04 | Specification/method version | Master data lifecycle | Obsolete version used or history overwritten | O,A,C,E | Approval/effective date, immutable history, change control | Medium |
| DIRA-05 | LES observations | Creation/review | Data entered late, omitted, or attributed incorrectly | A,Cont,C | Unique user, step timestamp, required fields, review | Medium |
| DIRA-06 | Balance/pH/TOC result | Capture/transmission | Manual transcription or unit conversion error | O,A,C | Direct interface, source metadata, unit validation | Low |
| DIRA-07 | CDS numeric result/link | Approval/transmission | LIMS result differs from CDS source or link breaks | O,A,C,E | Approved-result interface, stable ID/link, reconciliation | Medium |
| DIRA-08 | Manual result entry | Creation/verification | Critical result entered incorrectly | A,Acu,C | Reason, independent verification, audit trail | Medium |
| DIRA-09 | Calculation inputs/formula | Processing | Wrong formula, rounding or input version | Acu,C,O | Controlled formula version, independent test, change control | Medium |
| DIRA-10 | Pass/fail decision | Processing/approval | Incorrect status drives batch disposition | Acu,C | Boundary testing, review, locked approved state | Medium |
| DIRA-11 | OOS/OOT case linkage | Transmission | Duplicate or missing investigation | C,A | Idempotent interface, case ID return, exception queue | Low |
| DIRA-12 | Electronic signature | Approval | Signature shared, detached or meaning unclear | A,O,C | Unique credentials, re-authentication, record binding, manifestation | Low |
| DIRA-13 | Audit trail | Generation/review | Critical change not recorded or reviewed | C,Cns,E,A | Always-on configuration, challenge test, periodic review | Medium |
| DIRA-14 | Role and access data | Administration | Unauthorized privilege or shared account | A,C | Approved access requests, SoD, periodic review | Medium |
| DIRA-15 | Report/PDF output | Reporting | Truncation or mismatch to source record | Acu,C | Template/version control and report verification | Low |
| DIRA-16 | Backup copy | Backup/retention | Backup incomplete, unreadable or not monitored | C,E,A | Automated backup, monitoring, restore test | Medium |
| DIRA-17 | Migrated record | Migration | Field, attachment or relationship lost | C,Acu,O,E | Mapping, counts, field sampling, hash and relationship checks | Medium |
| DIRA-18 | Archived legacy record | Archive/retrieval | Record or audit trail cannot be retrieved | A,E,C | Read-only archive qualification and sample retrieval | Medium |
| DIRA-19 | System time | Infrastructure | Timestamp drift obscures sequence of events | Cont,C | Authoritative time sync and monitoring | Low |
| DIRA-20 | Contingency paper record | Outage/reconciliation | Late or duplicate transcription after recovery | Cont,O,C | Controlled forms, log, independent reconciliation | Medium |

## 3. Data ownership decisions

- QCLabOne is the official source for sample, LES, calculation, review, signature and audit records.
- CDS/SDMS is the official source for chromatographic raw/processed data.
- eQMS is the official source for OOS/OOT investigation content.
- SAP is the official source for material/batch master and final release status.
- ArchiveVault becomes the official source for accepted retired Legacy LIMS records.
- Manual contingency records remain controlled originals and are linked to reconciled electronic records.

## 4. Review frequency decisions

Critical result/specification/formula/role/signature audit trails are reviewed as part of record approval or defined periodic review. Privileged access and role changes are reviewed monthly; system-wide audit-trail trend review is quarterly.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Input | QCL-2026-PRA-001 | [Preliminary Risk Assessment](011_Preliminary_Risk_Assessment.md) |
| Output | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Output | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Output | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Output | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Output | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Output | SOP-QA-ATR-001 | [QCLabOne 2.0 Audit Trail Review SOP](068_Audit_Trail_Review_SOP.md) |
| Output | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV/Quality Risk Lead | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-20 | Initial approved fictional case version. |
