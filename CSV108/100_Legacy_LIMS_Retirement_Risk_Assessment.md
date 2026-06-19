---
document_number: QCL-2028-RRA-001
title: "Legacy LIMS Retirement Risk Assessment"
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

# Legacy LIMS Retirement Risk Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2028-RRA-001 |
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

## 1. Method

Severity, probability and detectability are scored 1–5. Retirement proceeds only after controls reduce each risk to acceptable residual level.

## 2. Retirement risk register

| ID | Risk | S | P | D | Initial | Control | Residual |
|---|---|---|---|---|---|---|---|
| RET-01 | Required legacy record omitted from archive | 5 | 2 | 4 | 40 High | 100% count/manifest reconciliation; stratified retrieval | Low |
| RET-02 | Attachments or audit trail not linked/readable | 5 | 2 | 4 | 40 High | Checksum, relationship and retrieval verification | Low |
| RET-03 | Archive index cannot locate record during inspection | 4 | 2 | 4 | 32 Medium | Search index by sample/batch/material/test/date; retrieval timing test | Low |
| RET-04 | Legacy system shut down before acceptance | 5 | 2 | 4 | 40 High | Formal retirement gate and QA/Records approval | Low |
| RET-05 | Legacy account/interface remains active | 4 | 3 | 3 | 36 Medium | Access revocation and network/interface shutdown checklist | Low |
| RET-06 | Final backup contains uncontrolled sensitive credentials | 3 | 2 | 3 | 18 Medium | Encrypted sealed backup; access list; scheduled secure destruction | Low |
| RET-07 | Old data modified during read-only period | 5 | 2 | 4 | 40 High | DB/app read-only controls and audit review | Low |
| RET-08 | Retention schedule incorrectly applied | 5 | 2 | 4 | 40 High | Records/legal review and archive category mapping | Low |
| RET-09 | Vendor/licence termination removes export utility | 3 | 2 | 3 | 18 Medium | Complete open-format archive and documented viewer before termination | Low |
| RET-10 | Decommissioning affects QCLabOne or enterprise interfaces | 4 | 2 | 3 | 24 Medium | Network dependency review and post-shutdown smoke tests | Low |

## 3. Critical retirement gates

1. Complete archive count/checksum and retrieval approval.
2. Written Records Management and QA acceptance.
3. Confirm no legal hold or open investigation depends on live system.
4. Final read-only audit/access review.
5. Approved shutdown sequence and rollback/sealed backup.
6. Post-shutdown QCLabOne/SAP/eQMS/CDS smoke checks.
7. Inventory and dossier update.

## 4. Risk conclusion

No retirement risk remains High after planned controls. The irreversible step—destruction of the final system image—is deferred for 90 days after shutdown and requires separate confirmation that archive and inspection retrieval remain effective.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2028-DCR-001 | [Legacy LIMS Decommissioning Request](099_Legacy_LIMS_Decommissioning_Request.md) |
| Input | SOP-QA-ARC-001 | [Data Retention, Archiving and Record Retrieval SOP](070_Data_Retention_Archiving_and_Record_Retrieval_SOP.md) |
| Input | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Input | QCL-2028-ARC-001 | [System and Data Archive Record](097_System_and_Data_Archive_Record.md) |
| Output | QCL-2028-RTP-001 | [Legacy LIMS Retirement Plan](101_Legacy_LIMS_Retirement_Plan.md) |
| Output | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Output | QCL-2028-AIS-001 | [Legacy Access Revocation and Interface Shutdown Record](104_Legacy_Access_Revocation_and_Interface_Shutdown_Record.md) |
| Output | QCL-2028-DCL-001 | [Legacy System Decommissioning Checklist](105_Legacy_System_Decommissioning_Checklist.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |

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
