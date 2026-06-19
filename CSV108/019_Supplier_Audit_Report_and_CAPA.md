---
document_number: QCL-2026-SAR-001
title: "Supplier Audit Report and CAPA"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Supplier Management"
version: "1.0"
effective_or_record_date: "2026-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Supplier Quality Lead"
reviewed_by: "IT System Owner"
approved_by: "QA Validation Manager"
---

# Supplier Audit Report and CAPA

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-SAR-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Supplier Management |
| Version | 1.0 |
| Effective/record date | 2026-04-30 |
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

## 1. Audit scope and method

A remote document review and on-site audit were conducted 2026-05-18 to 2026-05-20. Scope covered QMS, SDLC, validation, configuration management, cloud operations, data integrity, security, backup/DR, support, change notification, subcontractors and data return.

## 2. Summary

The supplier demonstrated an established QMS and controlled product lifecycle. No critical or major finding was identified. Two minor findings and one observation were issued.

## 3. Findings and CAPA

| ID | Class | Finding | Supplier CAPA | Due | Status |
|---|---|---|---|---|---|
| SA-F-01 | Minor | DR exercise report did not include application-level data/retrieval verification after infrastructure failover. | Supplier to add application login, sample retrieval, audit trail and interface health checks to 2026 DR protocol. | 2026-06-30 | Closed 2026-06-18 |
| SA-F-02 | Minor | Privileged access review was quarterly; proposed QCLabOne agreement requires monthly review of customer-tenant access. | Implement monthly customer-tenant privileged review and provide quarterly summary. | 2026-07-31 | Closed 2026-07-20 |
| SA-OBS-01 | Observation | Release notes did not consistently distinguish security-only changes from functional changes. | Add release-note field for GxP/security/customer action. | 2026-09-30 | Closed 2026-09-10 |

## 4. Evidence verified

Quality manual; organisation chart; training matrix; SDLC procedures; sample requirements/design/code/test records; release 8.4.2 qualification summary; change/CAPA logs; access-control procedure; vulnerability process; backup/restore and DR reports; incident examples; subcontractor register; customer data-return procedure.

## 5. Audit conclusion

Supplier qualification is approved after CAPA closure. The site will maintain annual performance review and may re-audit after significant ownership, hosting, QMS or adverse compliance change.

CAPA effectiveness shall be checked against objective evidence rather than supplier statement alone. Evidence may include revised procedures, completed training, sample defect records, updated traceability reports or demonstration during a follow-up meeting. Any CAPA that weakens confidence in leveraged testing shall be reflected in the Supplier Documentation Leveraging Assessment.

| Finding class | Project impact rule |
|---|---|
| Critical | Supplier cannot be qualified until contained and QA disposition is approved |
| Major | Qualification may proceed with CAPA, owner, due date and affected evidence review |
| Minor | Track to closure through supplier oversight; no release block unless repeated |
| Observation | Consider for improvement and periodic supplier review |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-SQA-001 | [Supplier Qualification Assessment](018_Supplier_Qualification_Assessment.md) |
| Output | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Output | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Output | QCL-2028-SPR-001 | [Supplier Periodic Performance and SLA Review](096_Supplier_Periodic_Performance_and_SLA_Review.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Supplier Quality Lead | Completed |
| Reviewed by | IT System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-30 | Initial approved fictional case version. |
