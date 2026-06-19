---
document_number: QCL-2028-PRR-001
title: "Annual Periodic Review Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Operation"
version: "1.0"
effective_or_record_date: "2028-03-15"
case_status: "Completed/Closed in fictional operating record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "QC Business Process Owner"
approved_by: "QA System Oversight"
---

# Annual Periodic Review Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-PRR-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Operation |
| Version | 1.0 |
| Effective/record date | 2028-03-15 |
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

## 1. Review period and objective

Review of the validated state from go-live 2027-06-15 through 2028-02-29.

## 2. Current configuration

Production runs LabSphere 8.4.3 with baseline `QCL-PROD-BL-1.1`. Intended use and business scope remain unchanged. Inventory, owners, interfaces and record boundaries remain current.

## 3. Operating metrics

| Area | Observed | Criterion/assessment | Status |
|---|---|---|---|
| System availability | 99.94% | Target ≥99.9% | Meets |
| P1 incidents | 1 (certificate expiry) | No data loss; RCA/CAPA effective | Acceptable |
| Other incidents | 17 P2/P3 | All closed; no adverse trend | Acceptable |
| Changes | 12 planned + 1 emergency | All approved/closed | Acceptable |
| Open CAPA/deviation | 0 overdue | Target 0 | Meets |
| Access review | Quarterly complete; monthly privileged complete | No open conflict | Meets |
| Audit-trail review | Quarterly and record-level complete | 0 unexplained event | Meets |
| Backup/restore | Daily monitored; annual restore pass | RPO/RTO met | Meets |
| Security | No confirmed compromise; vulnerabilities managed | 8.4.3 applied | Meets |
| Supplier SLA | All targets met except one planned notice at 82 vs 90 days | Low issue | Acceptable with action |
| Performance/capacity | Peak 61%; response within target | No capacity concern | Meets |
| Training/SOP | Current; role changes linked to training | No overdue critical training | Meets |

## 4. Significant events

INC-2027-014 delayed 92 SAP messages with no loss/duplicate or incorrect release. ODV-004 granted an analyst excessive privilege for 47 minutes with no activity; provisioning CAPA was effective. Both are closed.

## 5. Requirements/risk review

No new intended use or high risk emerged. Certificate monitoring and access-provisioning controls were strengthened. Residual risk remains acceptable. Legacy archive verification is complete and retirement may proceed.

## 6. Actions

1. Supplier to provide planned change notice as close as practicable to 90 days.
2. Continue quarterly audit/access review and annual restore/DR.
3. Complete Legacy LIMS retirement by 2028-03-31.
4. Next periodic review due 2029-03-15 unless triggered earlier.

## 7. Conclusion

QCLabOne remains in a validated state and fit for intended use.

## 8. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | CSI-SZ-001 | [Site Computerised System Inventory](003_Computerised_System_Inventory.md) |
| Input | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |
| Input | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |
| Input | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Input | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Input | QCL-2027-ATR-001 | [Periodic Audit Trail Review Record](081_Periodic_Audit_Trail_Review_Record.md) |
| Input | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |
| Input | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Input | QCL-2027-RST-001 | [Periodic Restore Test Report](084_Periodic_Restore_Test_Report.md) |
| Input | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Input | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |
| Input | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Input | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
| Input | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |
| Input | QCL-2028-DRE-001 | [Business Continuity and Disaster Recovery Exercise Report](095_Business_Continuity_and_DR_Exercise_Report.md) |
| Input | QCL-2028-SPR-001 | [Supplier Periodic Performance and SLA Review](096_Supplier_Periodic_Performance_and_SLA_Review.md) |
| Output | QCL-2028-RVA-001 | [Revalidation Assessment and Report](093_Revalidation_Assessment_and_Report.md) |
| Output | QCL-2028-DCR-001 | [Legacy LIMS Decommissioning Request](099_Legacy_LIMS_Decommissioning_Request.md) |
| Output | QCL-2028-RRA-001 | [Legacy LIMS Retirement Risk Assessment](100_Legacy_LIMS_Retirement_Risk_Assessment.md) |
| Output | QCL-2028-RTP-001 | [Legacy LIMS Retirement Plan](101_Legacy_LIMS_Retirement_Plan.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA System Oversight | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2028-03-15 | Initial approved fictional case version. |
