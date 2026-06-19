---
document_number: QCL-2026-SDP-001
title: "Software Development and Source Control Plan"
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

# Software Development and Source Control Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-SDP-001 |
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

## 1. Scope

This plan applies to the custom SAP, eQMS, CDS/SDMS, instrument and archive integrations plus site-specific report utility code. It does not govern the supplier’s standard product source code, which is covered by supplier qualification.

## 2. Development lifecycle

| Stage | Required output | Control |
|---|---|---|
| Plan | Approved scope, architecture, standards and repository | No coding before approved work item |
| Requirements/design | Interface specification, mapping and error handling | Peer review and traceability |
| Implementation | Source code and automated tests | Protected branch and named developer |
| Code review | Independent review checklist | No self-approval of merge |
| Unit test | Normal, boundary, negative and failure cases | Automated result retained |
| Build | Reproducible signed artifact and software bill of materials | CI/CD service account |
| Promotion | DEV → TEST → VAL → PROD | Separate approver and checksum verification |
| Maintenance | Versioned change, regression and rollback | Change control |

## 3. Repository and branching

Repository: `git/qclabone-integrations`. Protected `main` branch; feature branches reference approved work item. Pull request requires one independent technical reviewer and successful automated tests. Tags are immutable and signed.

## 4. Coding and security standards

Input validation, idempotency, explicit error handling, least-privilege credentials, secret masking, structured logging, dependency scanning, no hard-coded credentials and UTC timestamps are mandatory. Third-party dependencies require approved licence and vulnerability review.

## 5. Release versions

SAP 2.1.0; eQMS 1.4.1; CDS 2.3.0; instrument adapters 3.6.1; archive utility 1.0.0.

Custom code cannot be promoted to validation or production unless the linked requirement/design item, code review, unit evidence, dependency/security scan and release tag are complete. Emergency fixes follow the same retrospective documentation and regression requirements as configuration emergency changes.

| Development control | Minimum evidence |
|---|---|
| Work item linkage | Approved requirement, defect or change record |
| Code review | Independent reviewer, comments resolved and approval retained |
| Automated checks | Unit tests, static analysis, dependency and secrets scan |
| Release package | Signed/immutable tag, build artifact checksum and deployment notes |
| Rollback | Prior version and rollback decision criteria documented |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Input | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Output | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Output | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |

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
