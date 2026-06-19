---
document_number: QCL-2026-ATS-001
title: "Audit Trail Specification"
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

# Audit Trail Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-ATS-001 |
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

This specification defines which events are audit-trailed, the minimum event content, protection, review and retention.

## 2. Audited events

| Object | Events | Minimum captured content |
|---|---|---|
| Sample | Create, receive, transfer, aliquot, reject, cancel, dispose, status change | User/service, timestamp, old/new status, reason where applicable, source |
| Test/LES | Assignment, start, entry, direct capture, manual entry, pause, abort, repeat, submit | Old/new value, unit, source device, verifier, reason |
| Result/calculation | Input change, recalculation, limit evaluation, override attempt | Old/new value, formula version, limit version, outcome, reason |
| Specification/method | Create, revise, approve, effective, obsolete | Version, old/new field, approver, effective date, reason |
| Master data | Create/change/disable reagent, standard, instrument, location, list value | Old/new value, user, approval, change reference |
| Security | Account/role create/change/disable, failed login, privileged session | Actor, target, old/new role, source, ticket |
| Electronic signature | Submit/review/approve/reject/cancel and invalidation | Signer, meaning, time, record ID, authentication result |
| Interface | Receive/send/retry/reprocess/error | Message ID, source/destination, status, error, actor |
| System/configuration | Configuration change, promotion, release, time-zone change | Old/new value, package/checksum, change record |

## 3. Technical requirements

Audit trails are computer-generated, append-only, synchronized to authoritative time and inseparable from the regulated record context. They retain old/new values in human-readable form. Routine application/database administrators cannot modify or delete entries.

## 4. Reason-for-change rules

A reason is mandatory for changes to results, specification/method/limit, formula, critical master data, role, workflow status, signature-impacting data and authorised interface reprocessing. Controlled reason plus comment is used where context is needed.

## 5. Review model

- Record-level review: reviewer examines relevant critical changes before approval.
- Monthly review: privileged access, role changes and vendor sessions.
- Quarterly review: system-wide critical event trends, repeated reasons, deletions/attempts, time changes and failed interface reprocessing.
- Event-based review: incident, OOS/OOT, complaint, data-integrity concern or inspection request.

## 6. Retention/export

Audit data is retained at least as long as the associated record. Exports show filters, execution time and requester and are verified against on-screen source.

## 7. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Output | SOP-QA-ATR-001 | [QCLabOne 2.0 Audit Trail Review SOP](068_Audit_Trail_Review_SOP.md) |
| Output | QCL-2027-ATR-001 | [Periodic Audit Trail Review Record](081_Periodic_Audit_Trail_Review_Record.md) |
| Output | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |

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
