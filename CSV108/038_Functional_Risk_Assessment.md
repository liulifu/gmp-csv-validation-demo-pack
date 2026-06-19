---
document_number: QCL-2026-FRA-001
title: "Functional Risk Assessment"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Risk and Compliance"
version: "1.0"
effective_or_record_date: "2026-10-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV/Quality Risk Lead"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# Functional Risk Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-FRA-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Risk and Compliance |
| Version | 1.0 |
| Effective/record date | 2026-10-31 |
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

Severity, probability and detectability are scored 1–5. Controls are assigned to requirements, design and tests. Residual risk is accepted only after evidence passes.

## 2. Functional risk register

| Risk ID | Failure mode | Linked requirement | S | P | D | Initial rating | Control | Verification |
|---|---|---|---|---|---|---|---|---|
| FRA-001 | Duplicate SAP sample request creates duplicate QC work | URS-SMP-001, URS-INT-001 | 5 | 3 | 3 | 45 High | Idempotency key, duplicate rejection, message reconciliation | IFT-SAP-001/002 |
| FRA-002 | Incorrect material/batch mapping | URS-SMP-001 | 5 | 2 | 3 | 30 Medium | Schema validation, master-data lookup, exception queue | IFT-SAP-001 |
| FRA-003 | Sample ID reused or barcode misprinted | URS-SMP-002, URS-GEN-002 | 5 | 2 | 3 | 30 Medium | Database sequence, barcode verification | OQ-SMP-001 |
| FRA-004 | Receipt or custody event omitted/backdated | URS-SMP-003/004/007 | 4 | 3 | 3 | 36 Medium | Mandatory fields, timestamp, audit trail, reason | OQ-SMP-002 |
| FRA-005 | Obsolete specification assigned | URS-SMP-005, URS-SPEC-001/003 | 5 | 2 | 4 | 40 High | Effective dating, immutable version, historical verification | OQ-SMP-003; OQ-SPEC-001/002 |
| FRA-006 | Sample closed with required test open | URS-SMP-006 | 5 | 2 | 3 | 30 Medium | Workflow closure rule | OQ-SMP-003 |
| FRA-007 | Stability pull date miscalculated | URS-SMP-008 | 4 | 2 | 3 | 24 Medium | Approved schedule algorithm, boundary testing | OQ-SMP-004 |
| FRA-008 | Unauthorized specification/master-data approval | URS-SPEC-002/005 | 5 | 2 | 4 | 40 High | Role control, e-signature, change control | SEC-001; EST-001 |
| FRA-009 | Historical specification overwritten | URS-SPEC-003 | 5 | 2 | 4 | 40 High | Immutable historical version | OQ-SPEC-002 |
| FRA-010 | LES step bypassed or mandatory data omitted | URS-LES-001/002 | 5 | 3 | 3 | 45 High | Sequence and required-field enforcement | OQ-LES-001 |
| FRA-011 | Wrong reagent, standard or instrument used | URS-LES-003 | 4 | 3 | 3 | 36 Medium | Effective master data and qualification status | OQ-LES-002 |
| FRA-012 | Instrument value associated to wrong test | URS-LES-004, URS-INT-004 | 5 | 2 | 4 | 40 High | Device/test context, source ID, exception queue | OQ-LES-003; IFT-INS-001 |
| FRA-013 | Manual critical result entered incorrectly | URS-LES-005 | 5 | 3 | 3 | 45 High | Reason, independent verification, audit trail | OQ-LES-004 |
| FRA-014 | Repeat or abort obscures original attempt | URS-LES-006 | 4 | 3 | 3 | 36 Medium | Controlled status and retained history | OQ-LES-005 |
| FRA-015 | Analyst self-approves result | URS-LES-007 | 5 | 2 | 4 | 40 High | Segregation workflow | OQ-LES-006; SEC-002 |
| FRA-016 | Formula, unit or rounding error | URS-CALC-001/002/004 | 5 | 3 | 4 | 60 High | Independent calculation verification and boundary tests | OQ-CALC-001/002 |
| FRA-017 | Formula history cannot be reconstructed | URS-CALC-003/005 | 5 | 2 | 4 | 40 High | Version history, change control, regression | OQ-CALC-003 |
| FRA-018 | eQMS retry creates duplicate OOS case | URS-INT-002 | 4 | 3 | 3 | 36 Medium | Idempotent request and returned case ID | IFT-EQM-002 |
| FRA-019 | CDS result differs from LIMS value | URS-INT-003 | 5 | 3 | 4 | 60 High | Approved-result transfer, unit/method checks, stable link | IFT-CDS-001/002 |
| FRA-020 | Interface error is silently lost | URS-INT-004/005 | 5 | 2 | 4 | 40 High | Exception queue, alerts, message audit | IFT-INS-002 |
| FRA-021 | Shared or orphan account used | URS-SEC-001/005 | 5 | 2 | 4 | 40 High | Unique identity, joiner/mover/leaver process | OQ-SEC-001; SEC-003 |
| FRA-022 | Excess privilege enables unreviewed data change | URS-SEC-002/003 | 5 | 3 | 4 | 60 High | Least privilege, SoD, periodic access review | SEC-001/002 |
| FRA-023 | Vendor remote access is uncontrolled | URS-SEC-006 | 5 | 2 | 4 | 40 High | Time-limited ticketed access and session logging | OQ-SEC-004 |
| FRA-024 | Audit trail omits old/new value or reason | URS-DI-001/002 | 5 | 3 | 4 | 60 High | Always-on audit, critical reason configuration | ATC-001/003 |
| FRA-025 | Audit trail can be altered or not reviewed | URS-DI-003/004 | 5 | 2 | 4 | 40 High | Protected storage and periodic review SOP | ATC-004; PQ-008 |
| FRA-026 | Signature detached, reused or meaning unclear | URS-ESIG-001/002/003 | 5 | 2 | 4 | 40 High | Unique identity, re-authentication, manifestation, binding | EST-001/002/003 |
| FRA-027 | Report/PDF differs from source record | URS-REP-001/002/003 | 5 | 2 | 4 | 40 High | Template control and output verification | RPT-001/003 |
| FRA-028 | Backup cannot restore complete record set | URS-BCP-001/003 | 5 | 2 | 5 | 50 High | Monitored backup and full restore reconciliation | BRT-001/003/004 |
| FRA-029 | DR exceeds RTO/RPO | URS-BCP-002/004 | 4 | 2 | 4 | 32 Medium | Standby environment and exercised continuity plan | DRT-002/003/004 |
| FRA-030 | Migration loses fields, attachments or relationships | URS-MIG-001/003, URS-DI-007 | 5 | 3 | 5 | 75 High | Trial migration, mapping, hash/count/relationship reconciliation | DMT-001 to DMT-006 |
| FRA-031 | Legacy archive record is unreadable | URS-MIG-002, URS-OPS-004 | 5 | 2 | 4 | 40 High | Read-only archive qualification and retrievability sample | DMT-005; PQ-011 |
| FRA-032 | Source system altered or retired prematurely | URS-MIG-004 | 5 | 2 | 4 | 40 High | Read-only control and retirement gate | DMT-001; retirement documents |
| FRA-033 | Operational review evidence unavailable | URS-OPS-001/003 | 4 | 3 | 3 | 36 Medium | Scheduled reports and annual periodic review | OQ-OPS-001; PRR |
| FRA-034 | Supplier change affects validated state without notice | URS-OPS-002 | 4 | 3 | 4 | 48 High | Quality agreement, change notice and impact assessment | Supplier review; PAT |
| FRA-035 | Retirement removes required access/interface too early | URS-OPS-004 | 5 | 2 | 4 | 40 High | Retirement plan, archive verification and staged shutdown | AVR; DCL |

## 3. Residual-risk criteria

After verified controls, no risk remains High. FRA-016, FRA-019, FRA-024, FRA-028 and FRA-030 are expected to reduce to Medium because consequences remain severe but probability/detectability are improved. Medium residual risks are accepted by QA and the Business/System Owner in the VSR.

Residual-risk reduction shall be evidence based. A risk may be reduced only when the specified control is implemented, verified and linked in the RTM. If a control fails testing, is deferred, or is replaced by a procedural workaround, the residual score shall be reassessed and the VSR shall document the impact on intended use.

| Residual-risk decision | Required support |
|---|---|
| Reduce to Low | Preventive/detective control verified and no severe consequence remains credible |
| Reduce to Medium | Severe consequence remains possible but probability/detection is controlled |
| Keep High | Control not verified or unacceptable data/product quality risk remains |
| Accept Medium | QA plus Business/System Owner acceptance in VSR |
| Reopen risk | Defect, deviation, change or incident invalidates control assumption |

## 4. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-PRA-001 | [Preliminary Risk Assessment](011_Preliminary_Risk_Assessment.md) |
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-RCS-001 | [Report and Calculation Specification](029_Report_and_Calculation_Specification.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Input | QCL-2026-ESS-001 | [Electronic Signature Specification](033_Electronic_Signature_Specification.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Input | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Input | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Output | QCL-2026-RTM-001 | [Initial Requirements Traceability Matrix](039_Initial_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Output | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Output | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Output | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Output | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Output | QCL-2026-EST-001 | [Electronic Signature Test Report](055_Electronic_Signature_Test_Report.md) |
| Output | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Output | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Output | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Output | QCL-2026-RPT-001 | [Report, Print and Export Verification Report](059_Report_Print_and_Export_Verification_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV/Quality Risk Lead | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-31 | Initial approved fictional case version. |
