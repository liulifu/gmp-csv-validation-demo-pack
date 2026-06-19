---
document_number: QCL-2026-CS-001
title: "Configuration Specification"
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

# Configuration Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CS-001 |
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

This specification defines the approved site configuration baseline. Values are promoted to production only through controlled release and are verified in OQ/PQ.

## 2. Configuration parameters

| Config ID | Parameter | Approved value | Area | Control |
|---|---|---|---|---|
| CFG-GEN-001 | Production environment label | PROD — GMP | System-wide | Change control |
| CFG-GEN-002 | Site timezone | Asia/Shanghai; UTC+08:00 | System-wide | IT/System Owner |
| CFG-GEN-003 | Application language | English primary; Chinese labels for local master data | System-wide | System Owner |
| CFG-SMP-001 | Sample ID pattern | QCL-YYYY-NNNNNNN | Sample management | Locked after go-live |
| CFG-SMP-002 | Barcode symbology | Code 128 with human-readable Sample ID | Printing | Verified |
| CFG-SMP-003 | Receipt mandatory fields | Condition, quantity, unit, receiver, location | Sample receipt | Required |
| CFG-SMP-004 | Closure rule | All required tests complete; no open OOS/OOT/hold | Workflow | Required |
| CFG-SPEC-001 | Specification states | Draft → In Review → Approved → Effective → Obsolete | Master data | E-signature at approval |
| CFG-SPEC-002 | Effective-date rule | No backdating; emergency activation via deviation/change | Master data | Required |
| CFG-LES-001 | Manual critical value verification | Required for assay, impurity, sterility, bioburden and EM excursions | LES | Independent reviewer |
| CFG-LES-002 | Repeat-test permission | Supervisor and QA Investigation roles only | LES | Reason mandatory |
| CFG-CALC-001 | Default rounding | Half-up at final result unless method-specific rule | Calculation | Method-specific overrides |
| CFG-CALC-002 | Division-by-zero handling | Block calculation and raise exception | Calculation | Required |
| CFG-INT-001 | Message retry | 3 automated retries at 1/5/15 minutes; then exception queue | Interfaces | No duplicate creation |
| CFG-INT-002 | Message retention | Online 2 years; archive with incident/record if longer | Interfaces | Searchable |
| CFG-SEC-001 | Authentication | Corporate SAML SSO | Security | Unique account |
| CFG-SEC-002 | Interactive local accounts | Disabled except two sealed break-glass accounts | Security | Quarterly test |
| CFG-SEC-003 | Session inactivity lock | 15 minutes | Security | Re-authenticate |
| CFG-SEC-004 | Vendor access | Disabled by default; max 8-hour approved window | Security | MFA/session log |
| CFG-SEC-005 | Failed-login lockout | 5 failures/15 minutes; 30-minute lock | Security | Identity service |
| CFG-DI-001 | Critical reason-for-change | Mandatory for result, limit, formula, spec, role, status and signature-impacting change | Audit trail | Controlled reason list |
| CFG-DI-002 | Audit trail timezone/display | Stored UTC; displayed CST with offset | Audit trail | Immutable |
| CFG-ESIG-001 | Signature meanings | Performed by; Reviewed by; Approved by; Rejected by; Cancelled by | Electronic signature | Controlled list |
| CFG-ESIG-002 | Re-authentication | Required for submit, review, approve, reject and cancel | Electronic signature | Password/MFA policy |
| CFG-REP-001 | Controlled report footer | Record ID, template version, generated timestamp, page x of y | Reporting | Required |
| CFG-BCP-001 | Backup frequency | 15-minute database PITR; nightly attachment/configuration backup | Continuity | Encrypted |
| CFG-BCP-002 | RPO/RTO | 15 minutes / 8 hours | Continuity | Tier 1 |
| CFG-OPS-001 | Access review frequency | Quarterly all users; monthly privileged accounts | Operations | System Owner |
| CFG-OPS-002 | Audit-trail trend review | Quarterly; critical record review during approval | Operations | QA/QC |
| CFG-OPS-003 | Periodic review | Annual | Operations | Due 2028-03-15 |
| CFG-RET-001 | Legacy archive mode | Read-only; no update/delete API | Archive | Records Management approval |

## 3. Workflow configuration

| Workflow | States | Approval/segregation |
|---|---|---|
| Sample | Pending → Received → In Testing → Under Review → Approved/Rejected/Cancelled → Archived | Analyst cannot final-approve own work |
| Test | Assigned → In Progress → Submitted → Reviewed → Approved/Rejected/Invalidated | Repeat/retest requires authorised reason |
| Specification | Draft → In Review → Approved → Effective → Obsolete | Creator cannot make own version effective |
| OOS/OOT link | Detected → Case Pending → Case Open → Dispositioned → Closed | Result remains on hold until eQMS disposition |
| Configuration package | Draft → Reviewed → Approved → Promoted → Verified | Production promotion by separate administrator |

## 4. Controlled reason lists

Result correction; transcription correction; instrument retransmission; unit correction; specification correction; workflow cancellation; authorised retest; administrative metadata correction; security/role change; interface reprocessing. “Other” requires free-text explanation and supervisor review.

## 5. Baseline control

The production baseline package is `QCL-PROD-BL-1.0`, checksum recorded in Document 077. Any parameter change after go-live requires change control, impact assessment and regression evidence.

Configuration items are risk classified before baseline approval. Critical items include role permissions, workflow state transitions, calculation/report logic, audit trail settings, e-signature meanings, interface mappings, retention settings and archive/export behavior. Critical item changes require QA review and targeted regression evidence even when implemented through standard administration screens.

| Configuration class | Change-control expectation |
|---|---|
| Critical GxP control | Formal change, risk assessment, independent review and regression evidence |
| Business workflow parameter | BPO approval, test evidence and training/SOP impact check |
| Operational/support parameter | System Owner approval and monitoring/backup/security impact check |
| Cosmetic/non-GxP label | Documented rationale and verification that regulated meaning is not altered |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Input | QCL-2026-ESS-001 | [Electronic Signature Specification](033_Electronic_Signature_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Output | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |

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
