---
document_number: QCL-2026-ERES-001
title: "21 CFR Part 11 and EU Annex 11 Assessment"
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

# 21 CFR Part 11 and EU Annex 11 Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-ERES-001 |
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

## 1. Scope determination

The system creates and maintains electronic GMP records and uses electronic signatures in place of handwritten signatures for submission, review and approval. Part 11 requirements are therefore applicable to the relevant FDA-required records. EU Annex 11 applies to the GMP computerised system and supporting service model.

## 2. Compliance assessment

| Requirement | Control area | Project evidence | Conclusion |
|---|---|---|---|
| Part 11 §11.10(a); Annex 11 §4 | System validation | URS, risk, IQ/OQ/PQ, traceability and VSR | Compliant after approved VSR |
| Part 11 §11.10(b); Annex 11 §8 | Accurate and complete copies | Controlled PDF/export and archive retrieval testing | Compliant |
| Part 11 §11.10(c); Annex 11 §17 | Record protection and retention | Retention/archiving SOP, backup, read-only archive | Compliant |
| Part 11 §11.10(d) | Access limitation | Unique SSO, RBAC, access approval/review | Compliant |
| Part 11 §11.10(e); Annex 11 §9 | Audit trails | Always-on protected audit trail and review SOP | Compliant after DEV-001 closure |
| Part 11 §11.10(f) | Operational checks | Workflow sequence, prerequisites and state controls | Compliant |
| Part 11 §11.10(g) | Authority checks | Role matrix, positive/negative security test | Compliant |
| Part 11 §11.10(h) | Device checks | Device identity, unit and context validation | Compliant |
| Part 11 §11.10(i) | Training | Role training and authorisation before access | Compliant |
| Part 11 §11.10(j) | Signature accountability policy | Electronic-signature policy and user acknowledgement | Compliant |
| Part 11 §11.10(k) | System documentation control | eDMS control, versioning and access restriction | Compliant |
| Part 11 §11.50 | Signature manifestations | Name, date/time and meaning on electronic/printed view | Compliant |
| Part 11 §11.70 | Signature/record linking | Binding and post-signature invalidation test | Compliant |
| Part 11 §11.100–300 | Electronic signature controls | Unique identity, identity verification, re-authentication, credential controls | Compliant |
| Annex 11 §1 | Risk management | PRA, DIRA, FRA and residual-risk acceptance | Compliant |
| Annex 11 §2 | Personnel | RACI, training and access qualification | Compliant |
| Annex 11 §3 | Suppliers/service providers | Assessment, audit, agreement and oversight | Compliant |
| Annex 11 §4.2 | System inventory/description | Inventory, architecture, data flow and interface specs | Compliant |
| Annex 11 §5 | Data transfer checks | Interface validation and reconciliation | Compliant |
| Annex 11 §6 | Accuracy checks | Manual-entry verification and calculation testing | Compliant |
| Annex 11 §7 | Data storage | Backup, restore, retention and archive controls | Compliant |
| Annex 11 §10–13 | Change, periodic evaluation, security, incidents | Operational SOPs and records | Compliant |
| Annex 11 §14–16 | E-signature, batch release support, continuity | Signature tests, controlled status return, BCP/DR | Compliant |

## 3. Electronic record list

Sample records, LES worksheets, calculated results, review/approval records, audit trails, electronic signatures, controlled reports, migration reconciliation and archive indexes are regulated electronic records. Transient monitoring data that has no GMP decision use is governed by IT retention unless incorporated into an incident or investigation.

## 4. Open items

No compliance gap remains after closure of DEV-001. Site-specific legal certification of electronic signatures to FDA, if required by company regulatory policy, is outside this project document and shall be handled by Regulatory Affairs.

The compliance conclusion depends on the controls being implemented as approved in the released production baseline. Any later change to authentication, signature meaning, audit-trail configuration, record export, archive retention, supplier hosting or privileged access shall trigger Part 11/Annex 11 impact review before production deployment.

| Control dependency | Verification or operating evidence |
|---|---|
| Closed system access | Security/access test, access request records and periodic review |
| Electronic signature uniqueness | Identity proofing, user acknowledgement and re-authentication test |
| Signature manifestation | Screen/report verification showing signer, date/time and meaning |
| Audit trail protection | Challenge test, review SOP and privileged-access restriction |
| Accurate copies | PDF/export verification and archive retrieval challenge |

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Output | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Output | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Output | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Output | QCL-2026-ESS-001 | [Electronic Signature Specification](033_Electronic_Signature_Specification.md) |
| Output | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Output | QCL-2026-EST-001 | [Electronic Signature Test Report](055_Electronic_Signature_Test_Report.md) |
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
| 1.0 | 2026-03-20 | Initial approved fictional case version. |
