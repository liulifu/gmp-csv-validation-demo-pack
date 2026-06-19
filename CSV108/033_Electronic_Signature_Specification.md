---
document_number: QCL-2026-ESS-001
title: "Electronic Signature Specification"
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

# Electronic Signature Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-ESS-001 |
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

This specification defines the electronic-signature controls used for GMP submission, review, approval, rejection and cancellation.

## 2. Signature events

| Meaning | Who may sign | Effect |
|---|---|---|
| Performed by | Analyst | Confirms execution/data entry is complete and attributable |
| Reviewed by | Qualified Reviewer | Confirms source data, calculation, exceptions and audit trail were reviewed |
| Approved by | QC Supervisor/QA as configured | Confirms result/record is approved for downstream use |
| Rejected by | Reviewer/Supervisor/QA | Returns record with required reason |
| Cancelled by | Authorised Supervisor/QA | Terminates workflow while retaining history and reason |

## 3. Controls

- Each signature belongs to one verified individual and is not reassigned.
- Critical signatures require re-entry of corporate credentials or approved strong re-authentication.
- Manifestation displays printed name, date/time and meaning on electronic and printed views.
- Signature is linked to the record ID/version and cannot be copied to another record through ordinary means.
- A critical post-signature change invalidates affected approvals and re-routes the workflow.
- Failed signature attempts are logged.

## 4. Signature accountability

Before access, each user completes training acknowledging that the electronic signature is legally and procedurally equivalent to their handwritten signature for authorised company records.

Signature meaning shall be specific enough to distinguish submission, review, approval, QA approval, rejection, invalidation and retirement acceptance. A signature shall not be applied silently by workflow automation. Where a service account advances workflow status, the action shall be attributable to the approved service and shall not replace a required human signature.

| Signature control | Verification focus |
|---|---|
| Re-authentication | User must provide approved credential/strong authentication at signing |
| Manifestation | Printed/electronic view shows signer, date/time and meaning |
| Record binding | Signature is linked to record ID/version and cannot be copied |
| Post-signature change | Affected approval is invalidated and routed for re-review |
| Accountability training | User acknowledgement is complete before signature privilege |

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-EST-001 | [Electronic Signature Test Report](055_Electronic_Signature_Test_Report.md) |
| Output | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |
| Output | QCL-2026-TRN-001 | [Training Plan, Materials and Training Record](071_Training_Plan_Materials_and_Training_Record.md) |

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
