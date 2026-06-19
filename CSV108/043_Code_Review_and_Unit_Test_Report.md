---
document_number: QCL-2026-CRU-001
title: "Code Review and Unit Test Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Development"
version: "1.0"
effective_or_record_date: "2026-12-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Integration Development Lead"
reviewed_by: "IT System Owner"
approved_by: "QA CSV Lead"
---

# Code Review and Unit Test Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CRU-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Development |
| Version | 1.0 |
| Effective/record date | 2026-12-20 |
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

## 1. Review scope

Code review covered the signed release tags for the five custom integration components and archive utility.

## 2. Code-review summary

| Component | Files/changes reviewed | Review conclusion |
|---|---|---|
| SAP connector 2.1.0 | Message validation, idempotency, mapping, acknowledgement | Accepted |
| eQMS connector 1.4.1 | Case creation, retry, idempotency and status polling | Accepted after DEF-003 correction |
| CDS connector 2.3.0 | Approved status, value/unit/context mapping and source link | Accepted |
| Instrument adapters 3.6.1 | Device parsers, unit/range validation and queue | Accepted |
| Archive utility 1.0.0 | Manifest, checksum and filename normalization | Accepted |

## 3. Unit-test results

| Test ID | Test | Expected result | Outcome |
|---|---|---|---|
| UT-SAP-001 | Valid sample request mapping | Expected target object created | Pass |
| UT-SAP-002 | Duplicate idempotency key | No duplicate object; duplicate status returned | Pass |
| UT-SAP-003 | Invalid mandatory field | Rejected with field error | Pass |
| UT-EQM-001 | Create OOS case | One request and stored returned case ID | Pass |
| UT-EQM-002 | Retry same request | No duplicate case | Pass after code fix |
| UT-CDS-001 | Approved result mapping | Value/unit/context/link preserved | Pass |
| UT-CDS-002 | Unapproved CDS status | Rejected | Pass |
| UT-INS-001 | Device parser and unit mapping | Correct normalized message | Pass |
| UT-INS-002 | Out-of-range/unknown device | Quarantined | Pass |
| UT-ARC-001 | Archive manifest generation | All files and hashes listed | Pass |
| UT-ARC-002 | Special-character filename | Normalized target name; original metadata retained | Pass |
| UT-COM-001 | Logging masks secrets | No password/token in log | Pass |
| UT-COM-002 | Retry backoff and dead-letter queue | 1/5/15 min then queue | Pass |
| UT-COM-003 | Timestamp/time-zone conversion | UTC retained; CST displayed | Pass |

## 4. Static and dependency checks

No critical/high static-analysis issue or known critical vulnerability remained in the approved build. Secrets scanning passed. Third-party component list and licences were accepted by IT Security.

## 5. Conclusion

Custom code is acceptable for FAT/SAT and formal interface verification. All identified issues are traceable in the defect log.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Input | QCL-2026-SDP-001 | [Software Development and Source Control Plan](042_Software_Development_and_Source_Control_Plan.md) |
| Output | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Integration Development Lead | Completed |
| Reviewed by | IT System Owner | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-12-20 | Initial approved fictional case version. |
