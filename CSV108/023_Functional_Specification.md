---
document_number: QCL-2026-FS-001
title: "Functional Specification"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Design"
version: "1.0"
effective_or_record_date: "2026-10-31"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "System Owner"
reviewed_by: "Vendor Solution Architect"
approved_by: "QA CSV Lead"
---

# Functional Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-FS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Design |
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

## 1. Purpose

This specification describes the functional behaviour that will satisfy the approved URS. Detailed implementation parameters are controlled in the design and configuration specifications.

## 2. Functional requirements

| Function ID | Function | URS coverage | Functional behaviour |
|---|---|---|---|
| FS-GEN-001 | Environment identification and production baseline control | URS-GEN-003, URS-GEN-005 | Application banner displays environment/version; deployment requires approved release package. |
| FS-GEN-002 | Unique identifiers and synchronized timestamps | URS-GEN-002, URS-GEN-004 | Database sequences generate immutable IDs; all services synchronize to corporate NTP. |
| FS-GEN-003 | In-scope QC business process enablement | URS-GEN-001 | Configured modules and workflows support chemistry, microbiology, stability and environmental monitoring. |
| FS-SMP-001 | SAP sample request intake | URS-SMP-001, URS-INT-001 | Gateway validates schema, checks idempotency and creates a pending request. |
| FS-SMP-002 | Sample ID and barcode generation | URS-SMP-002 | LIMS assigns QCL-YYYY-NNNNNNN and Code 128 barcode. |
| FS-SMP-003 | Receipt and chain of custody | URS-SMP-003, URS-SMP-004, URS-SMP-007 | Receipt and custody events require user, timestamp, location, quantity and reason where applicable. |
| FS-SMP-004 | Test assignment and sample completion | URS-SMP-005, URS-SMP-006 | Effective specification creates required tests; closure is blocked while mandatory tasks/investigations remain open. |
| FS-SMP-005 | Stability scheduling | URS-SMP-008 | Protocol-derived pull dates, windows and alerts are generated nightly. |
| FS-SPEC-001 | Specification and method lifecycle | URS-SPEC-001, URS-SPEC-002, URS-SPEC-003 | Draft-review-approve-effective-obsolete states with effective dating and immutable history. |
| FS-SPEC-002 | Result type and limit configuration | URS-SPEC-004 | Numeric, text, enumerated and qualitative types support configured validation and limits. |
| FS-SPEC-003 | Production promotion approval | URS-SPEC-005, URS-GEN-005 | Approved change record and electronic approval are prerequisites for promotion. |
| FS-LES-001 | Controlled electronic worksheet execution | URS-LES-001, URS-LES-002 | Only approved versions are executable; mandatory steps enforce sequence and completion. |
| FS-LES-002 | Resource references | URS-LES-003 | Reagent, standard, instrument and lot are selected from effective master data. |
| FS-LES-003 | Direct instrument capture | URS-LES-004 | Gateway associates device message with active test and retains source metadata. |
| FS-LES-004 | Manual entry and verification | URS-LES-005 | Manual critical values require reason and independent verifier. |
| FS-LES-005 | Pause/abort/repeat and exception workflow | URS-LES-006, URS-LES-008 | Controlled states require reason and supervisor action; dashboards show exceptions. |
| FS-LES-006 | Second-person review segregation | URS-LES-007 | Workflow engine prevents submitter from final review/approval. |
| FS-CALC-001 | Formula execution and unit handling | URS-CALC-001 | Versioned calculation service executes approved formulas with dimensional checks. |
| FS-CALC-002 | Rounding and significant figures | URS-CALC-002 | Rounding occurs only at configured display/final step using half-up rules unless specified. |
| FS-CALC-003 | Formula history and limit evaluation | URS-CALC-003, URS-CALC-004 | Record stores formula version and evaluates effective limit set. |
| FS-CALC-004 | Calculation change control | URS-CALC-005 | Formula changes require approved configuration package and regression evidence. |
| FS-INT-001 | SAP bidirectional interface | URS-INT-001 | Inbound sample and outbound status/result messages use unique message IDs and acknowledgements. |
| FS-INT-002 | eQMS OOS/OOT interface | URS-INT-002 | Idempotent REST message creates one case and stores returned case ID/status. |
| FS-INT-003 | CDS/SDMS approved-result interface | URS-INT-003 | Interface receives approved numeric result, unit, sequence ID, method version and stable source link. |
| FS-INT-004 | Instrument exception handling | URS-INT-004, URS-INT-005 | Malformed/duplicate messages enter a controlled queue with error and reprocessing history. |
| FS-INT-005 | Manual contingency processing | URS-INT-006 | Approved outage mode labels manually entered data and requires independent reconciliation. |
| FS-SEC-001 | Corporate authentication and individual identity | URS-SEC-001 | SAML federation uses unique corporate identity; local interactive accounts are disabled except break-glass accounts. |
| FS-SEC-002 | Role-based authorization | URS-SEC-002, URS-SEC-003 | Permissions are assigned through approved roles; admin and QC approval privileges are mutually exclusive. |
| FS-SEC-003 | Session and account lifecycle controls | URS-SEC-004, URS-SEC-005 | 15-minute lock; approved request controls create/change/disable actions. |
| FS-SEC-004 | Vendor remote support | URS-SEC-006 | Just-in-time access requires company ticket, MFA, time window and session logging. |
| FS-SEC-005 | Security event logging | URS-SEC-007 | Failed logins, lockouts, role changes and privileged actions are reportable. |
| FS-DI-001 | Protected audit trail | URS-DI-001, URS-DI-003 | Database audit service is always on; no application role can alter entries. |
| FS-DI-002 | Reason for change | URS-DI-002 | Critical changes require selection from controlled reason list plus optional comment. |
| FS-DI-003 | Audit trail review/export | URS-DI-004 | Authorized filters and PDF/CSV exports preserve source identifiers and criteria. |
| FS-DI-004 | Retention, deletion and archive | URS-DI-005, URS-DI-006 | Purge disabled for routine roles; archive job preserves data, metadata, audit and attachments. |
| FS-DI-005 | Transfer/migration reconciliation | URS-DI-007 | Count, hash, critical-field and relationship controls generate reconciliation reports. |
| FS-DI-006 | Time control | URS-DI-008 | NTP sync alarms at >60 seconds drift; timezone configuration is change-controlled. |
| FS-ESIG-001 | Signature identity and re-authentication | URS-ESIG-001, URS-ESIG-003 | Signature uses individual identity and credential re-entry for submit/review/approve. |
| FS-ESIG-002 | Signature manifestation and binding | URS-ESIG-002, URS-ESIG-004 | Name, time and meaning display; post-signature critical change invalidates approval and re-routes workflow. |
| FS-REP-001 | Controlled reports | URS-REP-001, URS-REP-002 | Approved templates generate reports with record and template metadata. |
| FS-REP-002 | PDF/print/export fidelity | URS-REP-003, URS-REP-004 | Rendered output retains units, pagination, signatures and query criteria. |
| FS-BCP-001 | Backup and restore | URS-BCP-001, URS-BCP-003 | Encrypted backups cover database, configuration and attachments; restore procedure verifies consistency. |
| FS-BCP-002 | Disaster recovery and continuity | URS-BCP-002, URS-BCP-004 | Standby region supports RPO 15 min/RTO 8 h; controlled manual forms support outage. |
| FS-MIG-001 | Migration and archive | URS-MIG-001, URS-MIG-002 | ETL and archive paths use approved mapping, validation and read-only retention. |
| FS-MIG-002 | Migration exceptions and source protection | URS-MIG-003, URS-MIG-004 | Exception log requires disposition; source remains read-only and backed up until acceptance. |
| FS-OPS-001 | Operational evidence and periodic review | URS-OPS-001, URS-OPS-003 | Reports and schedules support access/audit/backup review and annual validated-state assessment. |
| FS-OPS-002 | Supplier notification and retirement | URS-OPS-002, URS-OPS-004 | Quality agreement routes notices; retirement workflow requires archive and decommissioning approvals. |

## 3. Cross-cutting functional rules

- All GxP state changes are attributable to an individual or approved service account.
- Historical effective versions remain linked to completed records.
- Interface processing is idempotent and exceptions are visible.
- Post-signature changes invalidate affected approval as configured.
- Routine users cannot delete GxP records or audit trails.
- Application errors display a user-safe message and create diagnostic logs without exposing secrets.

## 4. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Output | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Output | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Output | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Output | QCL-2026-RCS-001 | [Report and Calculation Specification](029_Report_and_Calculation_Specification.md) |
| Output | QCL-2026-MDS-001 | [Master Data Specification](030_Master_Data_Specification.md) |
| Output | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Output | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Output | QCL-2026-ESS-001 | [Electronic Signature Specification](033_Electronic_Signature_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-RTM-001 | [Initial Requirements Traceability Matrix](039_Initial_Requirements_Traceability_Matrix.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | System Owner | Completed |
| Reviewed by | Vendor Solution Architect | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-31 | Initial approved fictional case version. |
