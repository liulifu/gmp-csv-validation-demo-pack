---
document_number: QCL-2027-REG-003
title: "Regression Test Plan and Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Operation"
version: "1.0"
effective_or_record_date: "2027-12-20"
case_status: "Completed/Closed in fictional operating record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "QA System Oversight"
---

# Regression Test Plan and Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-REG-003 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Operation |
| Version | 1.0 |
| Effective/record date | 2027-12-20 |
| Case status | Completed/Closed in fictional operating record |

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

Focused regression for LabSphere 8.4.3 and CHG-2027-021 certificate monitoring. Validation environment matched production configuration.

## 2. Results

| Test | Area | Actual result | Outcome |
|---|---|---|---|
| REG-001 | Version/install and baseline | 8.4.3 installed; configuration checksum unchanged | Pass |
| REG-002 | Corporate SSO/session/role access | Login, lock, positive/negative permission | Pass |
| REG-003 | Electronic signatures | Submit/review/approve manifestation and binding | Pass |
| REG-004 | Audit trail view/filter/export | Events complete; export performance improved | Pass |
| REG-005 | Controlled reports/PDF | Test report, CoA extract, pagination and signatures | Pass |
| REG-006 | SAP/eQMS/CDS/instrument smoke | Normal/error message paths | Pass |
| REG-007 | Calculation boundary set | Assay, RSD, rounding and limits unchanged | Pass |
| REG-008 | PQ critical workflow | Finished product assay and OOS link | Pass |
| REG-009 | Backup/restore compatibility | Backup job and test restore of selected record | Pass |
| REG-010 | Certificate monitoring change | All certificates discovered; 60/30/7 alerts simulated | Pass |

## 3. Deviations

No regression deviation or defect was identified. Supplier evidence covered unchanged standard functions; site testing covered high-risk/site-specific controls.

## 4. Conclusion

Release 8.4.3 and certificate monitoring are suitable for controlled production implementation.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Input | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |
| Input | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Input | QCL-2027-PAT-003 | [Patch and Upgrade Impact Assessment](089_Patch_and_Upgrade_Impact_Assessment.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA System Oversight | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-12-20 | Initial approved fictional case version. |
