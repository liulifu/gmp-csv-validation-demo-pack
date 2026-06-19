---
document_number: QCL-2028-DCL-001
title: "Legacy System Decommissioning Checklist"
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

# Legacy System Decommissioning Checklist

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-DCL-001 |
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

## 1. Decommissioning checklist

| Check | Complete/result | Evidence |
|---|---|---|
| Retirement request/risk/plan approved | Yes | Documents 099–101 |
| Archive/retention/retrieval accepted | Yes | Documents 102–103 |
| Open incidents/changes/investigations checked | Yes | No blocking item |
| Final backup/system image sealed | Yes | Backup ID LEG-FINAL-20280328; checksum retained |
| Users/vendor/service accounts revoked | Yes | Document 104 |
| Interfaces/schedulers/network routes stopped | Yes | Document 104 |
| Application services stopped | Yes | 2028-03-31 10:12 CST |
| Oracle database stopped and storage made offline | Yes | 2028-03-31 10:20 CST |
| VMs powered off and CMDB marked retired | Yes | 2028-03-31 10:35 CST |
| QCLabOne/SAP/eQMS/CDS smoke tests | Pass | 2028-03-31 11:10 CST |
| Archive search/retrieval after shutdown | Pass | 10 selected records |
| Licences/contracts/monitoring alerts updated | Yes | No orphan alert/service |
| Inventory and dossier update prepared | Yes | Documents 107–108 |
| 90-day secure destruction action tracked | Yes | Due 2028-06-30 |

## 2. Exceptions

No decommissioning exception occurred. The final encrypted system image is deliberately retained for 90 days as a controlled contingency and is not the official archive.

## 3. Conclusion

Legacy LIMS application and database services are shut down, network-accessible processing is disabled, and required records remain available in ArchiveVault.

## 4. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2028-RTP-001 | [Legacy LIMS Retirement Plan](101_Legacy_LIMS_Retirement_Plan.md) |
| Input | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Input | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Input | QCL-2028-AIS-001 | [Legacy Access Revocation and Interface Shutdown Record](104_Legacy_Access_Revocation_and_Interface_Shutdown_Record.md) |
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
