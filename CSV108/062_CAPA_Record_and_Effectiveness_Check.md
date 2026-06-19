---
document_number: QCL-2026-CAPA-001
title: "CAPA Record and Effectiveness Check"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Test Management"
version: "1.0"
effective_or_record_date: "2027-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# CAPA Record and Effectiveness Check

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CAPA-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Test Management |
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

## 1. CAPA record

**CAPA ID:** CAPA-QCL-2027-001  
**Source:** DEV-001 / audit-trail reason configuration  
**Problem statement:** The site configuration review did not explicitly classify sample comments as critical metadata, allowing a change without mandatory reason.

## 2. Root cause

The design specification listed critical objects at a high level, while the configuration workbook used a supplier default field classification. The design-to-configuration review checklist did not require field-by-field confirmation for audit-reason rules.

## 3. Actions

| Action | Owner | Due | Completion/evidence |
|---|---|---|---|
| Update audit-trail specification with field-level criticality appendix | QA Data Integrity Owner | 2027-04-05 | ATS revision 1.1 approved |
| Update configuration workbook and promote controlled package | System Owner | 2027-04-06 | QCL-CONFIG-1.0-R1 |
| Repeat ATC-002/003 and affected regression | Test Lead | 2027-04-08 | All pass |
| Add field-level audit configuration review to CSV checklist | CSV Program Lead | 2027-04-30 | SOP attachment revised |
| Train configuration reviewers | QA Training Owner | 2027-05-10 | 12/12 completed |

## 4. Effectiveness check

On 2027-09-15, QA sampled 25 configured critical fields and five production change events. All required reason capture; no missing reason was found. CAPA is effective and closed.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Input | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Input | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Output | SOP-QA-ATR-001 | [QCLabOne 2.0 Audit Trail Review SOP](068_Audit_Trail_Review_SOP.md) |
| Output | QCL-2027-ATR-001 | [Periodic Audit Trail Review Record](081_Periodic_Audit_Trail_Review_Record.md) |
| Output | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-04-30 | Initial approved fictional case version. |
