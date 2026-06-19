---
document_number: QCL-2026-PRA-001
title: "Preliminary Risk Assessment"
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

# Preliminary Risk Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-PRA-001 |
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

## 1. Method

Severity (S), probability (P) and detectability (D) are scored 1–5. RPN = S × P × D. High ≥40; Medium 16–39; Low ≤15. Any credible risk to an incorrect batch-quality decision is treated as High until controls are verified.

## 2. Preliminary risk register

| ID | Hazard | Potential impact | S | P | D | Initial rating | Planned control |
|---|---|---|---|---|---|---|---|
| PRA-01 | Incorrect or incomplete sample request from SAP | Wrong tests or material disposition | 4 | 3 | 3 | 36 Medium | Interface validation, message reconciliation, exception queue |
| PRA-02 | Use of obsolete specification or method | Incorrect test or limit applied | 5 | 2 | 3 | 30 Medium | Effective-date/version controls, approval workflow, OQ |
| PRA-03 | Calculation or rounding defect | Incorrect pass/fail decision | 5 | 2 | 4 | 40 High | Independent formula verification, boundary testing, controlled change |
| PRA-04 | Unauthorized access or excessive privilege | Uncontrolled data/configuration change | 5 | 3 | 3 | 45 High | RBAC, SoD, access approval, periodic review |
| PRA-05 | Audit trail not enabled or incomplete | Changes cannot be reconstructed | 5 | 2 | 4 | 40 High | Audit trail specification and challenge testing |
| PRA-06 | Electronic signature not linked to record | Approval authenticity compromised | 5 | 2 | 4 | 40 High | Part 11 assessment and signature challenge test |
| PRA-07 | Instrument/CDS data transfer error | Incorrect or missing result | 5 | 3 | 3 | 45 High | Mapping, checksum/message ID, exception handling, reconciliation |
| PRA-08 | Migration omits or corrupts legacy records | Historical evidence unavailable | 5 | 3 | 4 | 60 High | Profiling, trial migration, count/field reconciliation, archive verification |
| PRA-09 | Cloud service outage | QC operations delayed | 4 | 3 | 2 | 24 Medium | BCP, redundancy, RTO/RPO, manual fallback |
| PRA-10 | Backup or restore failure | Permanent loss of GxP data | 5 | 2 | 4 | 40 High | Backup monitoring, periodic restore tests, DR exercise |
| PRA-11 | Supplier change without impact assessment | Validated state unintentionally affected | 4 | 3 | 3 | 36 Medium | Quality agreement, change notice, patch assessment |
| PRA-12 | Insufficient user training | Incorrect workflow execution | 4 | 3 | 2 | 24 Medium | Role-based training and authorization |
| PRA-13 | Vendor remote support changes production | Unapproved GxP configuration change | 5 | 2 | 4 | 40 High | Time-limited access, session monitoring, change control |
| PRA-14 | Old LIMS retired before archive acceptance | Regulatory records become unavailable | 5 | 2 | 4 | 40 High | Retirement gate and archive retrievability testing |
| PRA-15 | Hybrid/manual contingency data not reconciled | Duplicate or inconsistent records | 4 | 3 | 3 | 36 Medium | Controlled forms, independent verification, post-outage reconciliation |

## 3. Risk response

High risks require explicit URS and verification coverage. Medium risks require documented controls and testing where the control is automated or critical. Low risks may be managed by standard procedures and supplier/infrastructure evidence. Residual risk will be reassessed in the FRA and VSR.

## 4. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Input | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Input | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Output | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Output | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |
| Output | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |

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
