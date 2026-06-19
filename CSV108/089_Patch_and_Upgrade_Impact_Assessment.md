---
document_number: QCL-2027-PAT-003
title: "Patch and Upgrade Impact Assessment"
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

# Patch and Upgrade Impact Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2027-PAT-003 |
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

## 1. Assessment

**Patch:** LabSphere LIMS/LES 8.4.3  
**Assessment date:** 2027-11-15  
**Supplier release date:** 2027-11-08

## 2. Release impact

| Area | Supplier information | Project decision |
|---|---|---|
| Release | LabSphere 8.4.3 | Cumulative security/maintenance release |
| Security fixes | Two high vendor-rated dependency vulnerabilities; no known exploitation | Patch required within 30 days |
| Functional changes | Updated PDF engine, SAML library, audit export performance; no schema change | Regression required for reports, SSO and audit export |
| Database migration | None | Low implementation complexity |
| Configuration impact | No intended site configuration change | Baseline version update only |
| Downtime | 60-minute maintenance window | BCP notification only; no manual process expected |
| Rollback | Supplier snapshot and application rollback to 8.4.2-HF1 | Tested in validation environment |

## 3. Risk decision

The high-rated dependency vulnerabilities create a greater risk if the release is deferred. No data model or calculation change is present. Proceed under change control with focused regression on installation/version, SSO, role access, audit export, e-signature, controlled reports, interfaces and critical PQ smoke scenarios.

## 4. Evidence leveraged

Supplier release qualification summary, software bill of materials, vulnerability remediation statement, automated regression summary and rollback procedure were assessed and accepted.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Input | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Input | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Input | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Input | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |
| Input | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |
| Output | QCL-2027-REG-003 | [Regression Test Plan and Report](090_Regression_Test_Plan_and_Report.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-SPR-001 | [Supplier Periodic Performance and SLA Review](096_Supplier_Periodic_Performance_and_SLA_Review.md) |

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
