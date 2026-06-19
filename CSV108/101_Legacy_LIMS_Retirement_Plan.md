---
document_number: QCL-2028-RTP-001
title: "Legacy LIMS Retirement Plan"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Retirement"
version: "1.0"
effective_or_record_date: "2028-03-31"
case_status: "Approved/Closed in fictional retirement record"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Legacy System Owner"
reviewed_by: "Records Management Owner"
approved_by: "Site Quality Head"
---

# Legacy LIMS Retirement Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-RTP-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Retirement |
| Version | 1.0 |
| Effective/record date | 2028-03-31 |
| Case status | Approved/Closed in fictional retirement record |

## Governing references

- China GMP (2010 Revision), Appendix: Computerised Systems (effective 1 December 2015)
- China GMP (2010 Revision), Appendix: Qualification and Validation (effective 1 December 2015)
- EU GMP Annex 11: Computerised Systems (2011)
- EU GMP Annex 15: Qualification and Validation (2015)
- 21 CFR Part 11: Electronic Records; Electronic Signatures
- FDA Guidance: Part 11, Electronic Records; Electronic Signatures — Scope and Application
- PIC/S PI 041-1: Good Practices for Data Management and Integrity in Regulated GMP/GDP Environments (2021)
- ISPE GAMP 5, Second Edition (2022), used as non-binding industry guidance

## 1. Objective

Retire Legacy LIMS without loss of records, inspection access, business continuity or unintended impact on QCLabOne/enterprise systems.

## 2. Retirement sequence

| Step | Activity | Owner | Target | Case status |
|---|---|---|---|---|
| R1 | Confirm archive/retrieval and retention approval | Records Management/QA | 2028-03-20 | Complete |
| R2 | Notify users/support/enterprise owners and freeze changes | Legacy System Owner | 2028-03-22 | Complete |
| R3 | Final read-only backup and checksum; seal recovery package | IT Infrastructure | 2028-03-28 | Complete |
| R4 | Disable user/vendor/service accounts except retirement team | IT/Security | 2028-03-29 | Complete |
| R5 | Stop legacy SAP/CDS/instrument interfaces and firewall routes | IT Integration | 2028-03-30 | Complete |
| R6 | Execute final record/audit retrieval and open-item check | QC/QA/Records | 2028-03-30 | Complete |
| R7 | Shutdown application/database and retain VM/storage offline | IT Infrastructure | 2028-03-31 | Complete |
| R8 | Post-shutdown QCLabOne/enterprise smoke tests | System Owners | 2028-03-31 | Complete |
| R9 | Update inventory, CMDB, licences and support contracts | System Owner/Procurement | 2028-03-31 | Complete |
| R10 | Approve retirement summary/dossier | QA/System/Records | 2028-03-31 | Complete |
| R11 | After 90 days, securely destroy sealed image if no issue | IT/Records/QA | 2028-06-30 | Planned outside immediate shutdown; tracked |

## 3. Rollback/contingency

Until the 90-day hold ends, the final encrypted VM/database backup is retained offline with controlled access. If a material archive defect is discovered, the retirement team may restore the legacy environment in an isolated network for recovery only, under QA/Records approval. It will not resume routine processing.

## 4. Communications

QC/QA users, IT service desk, ERP/CDS/eQMS owners, supplier, Records Management, Security, Finance/Procurement and inspection coordinators receive the approved schedule and official-record-source statement.

## 5. Acceptance criteria

All preconditions complete; archive accepted; accounts/interfaces shut; server shutdown verified; no effect on QCLabOne/enterprise services; inventory/dossier updated; final report approved.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2028-DCR-001 | [Legacy LIMS Decommissioning Request](099_Legacy_LIMS_Decommissioning_Request.md) |
| Input | QCL-2028-RRA-001 | [Legacy LIMS Retirement Risk Assessment](100_Legacy_LIMS_Retirement_Risk_Assessment.md) |
| Input | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Input | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Output | QCL-2028-AIS-001 | [Legacy Access Revocation and Interface Shutdown Record](104_Legacy_Access_Revocation_and_Interface_Shutdown_Record.md) |
| Output | QCL-2028-DCL-001 | [Legacy System Decommissioning Checklist](105_Legacy_System_Decommissioning_Checklist.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | CSI-SZ-001-CHG-2028-03 | [Computerised System Inventory Update—Retired Status](107_Computerised_System_Inventory_Update_Retired_Status.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Legacy System Owner | Completed |
| Reviewed by | Records Management Owner | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2028-03-31 | Initial approved fictional case version. |
