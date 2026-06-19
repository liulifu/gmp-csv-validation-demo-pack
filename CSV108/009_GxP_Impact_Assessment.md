---
document_number: QCL-2026-GXP-001
title: "QCLabOne 2.0 GxP Impact Assessment"
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

# QCLabOne 2.0 GxP Impact Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-GXP-001 |
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

## 1. Assessment question and conclusion

**Question:** Does failure or misuse of QCLabOne 2.0 affect patient safety, product quality, GMP decisions or the integrity/availability of regulated records?

**Conclusion:** Yes. The system has **High GxP impact** because it creates and approves QC records, performs calculations and limit evaluation, supports material/batch disposition, applies electronic signatures and retains data required for inspection.

## 2. GxP impact screening

| Assessment criterion | Answer | Rationale |
|---|---|---|
| Creates or modifies GMP records | Yes | Sample, test, result, calculation, review, signature and audit records |
| Performs calculation or acceptance decision | Yes | Formula, rounding and specification evaluation |
| Supports material or batch disposition | Yes | Approved QC status/result is returned to SAP |
| Controls regulated workflow | Yes | Assignment, execution, OOS hold, review and approval |
| Stores required electronic records | Yes | Active records and audit trails; archive export |
| Uses electronic signatures | Yes | Submission, review and approval signatures |
| Exchanges GxP data | Yes | SAP, eQMS, CDS/SDMS and instruments |
| Failure could delay operations only | No | Certain failures could also produce an incorrect quality decision or unavailable evidence |

## 3. Component impact

| Component | Impact | Decision |
|---|---|---|
| LIMS/LES application | Direct | Full lifecycle validation |
| Interface gateway/custom interfaces | Direct | Specification, code control and verification |
| Cloud infrastructure/database | Indirect but critical | Supplier qualification and infrastructure qualification evidence |
| Identity service | Indirect but critical | Qualified service plus access/security verification |
| Backup and archive | Indirect but critical | Qualification, restore and retrievability testing |
| Barcode peripherals | Supporting | Installation and functional verification |

## 4. Required controls

URS, risk assessment, supplier qualification, design/configuration, traceability, IQ/OQ/PQ, interface/migration/security/audit/e-signature/backup tests, VSR, SOP/training, operational review and controlled retirement are required.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | CSI-SZ-001 | [Site Computerised System Inventory](003_Computerised_System_Inventory.md) |
| Input | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Output | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Output | QCL-2026-PRA-001 | [Preliminary Risk Assessment](011_Preliminary_Risk_Assessment.md) |
| Output | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Output | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Output | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |
| Output | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |

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
