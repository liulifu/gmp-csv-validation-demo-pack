---
document_number: QCL-2026-RCS-001
title: "Report and Calculation Specification"
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

# Report and Calculation Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-RCS-001 |
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

This specification defines regulated calculations and controlled outputs. Analytical-method scientific content remains approved under laboratory procedures; this document controls software implementation.

## 2. Calculation catalogue

| ID | Calculation | Formula/logic | Rounding | Control |
|---|---|---|---|---|
| CALC-ASSAY-01 | Assay % | (Sample response / Standard response) × (Standard weight / Sample weight) × Potency × Dilution factors × 100 | Full precision internal; final 1 decimal unless method states otherwise | 0 and boundary denominators tested |
| CALC-RSD-01 | Relative standard deviation | STDEV.S(results) / AVERAGE(results) × 100 | Final 2 decimals | n≥2; zero mean blocked |
| CALC-AVG-01 | Average | Sum(valid replicate results) / count | Method-specific | Invalidated replicate excluded only with approved reason |
| CALC-DIL-01 | Dilution factor | Final volume / aliquot volume × subsequent factors | Full precision | Units must be compatible |
| CALC-CFU-01 | CFU result | Colony count × dilution factor / plated volume | Integer or method-specific | TNTC and zero handling configured |
| CALC-EM-01 | Environmental monitoring alert/action | Compare result to location/grade/time-effective limits | No numeric rounding before comparison | Alert/action boundary tested |

## 3. General calculation rules

- Store source inputs and full precision; round only at the approved final/display point.
- Record formula/version, units and input record IDs.
- Block missing, invalid, incompatible-unit or division-by-zero inputs.
- Recalculation after critical input change is audit-trailed and invalidates affected approval.
- Independent reference calculations shall verify normal, boundary and negative scenarios.

## 4. Report catalogue

| ID | Report | Required content | Format | Business owner |
|---|---|---|---|---|
| RPT-TEST-01 | Analytical Test Report | Sample, specification/method version, observations, results, calculations, signatures, exceptions and audit-review status | PDF/A | QC Supervisor |
| RPT-COA-01 | CoA Supporting Data Extract | Approved test/result/status data sent to ERP/CoA process | JSON/PDF | QC/QA |
| RPT-STAB-01 | Stability Summary | Protocol, pull schedule, results, trend and missing/late pulls | PDF/CSV | Stability Manager |
| RPT-EM-01 | EM Trend Report | Location, grade, organism/count, alert/action and investigation link | PDF/CSV | Microbiology/QA |
| RPT-ATR-01 | Audit Trail Review Report | Filters, events, reviewer, review decision and exceptions | PDF/CSV | QA/QC Reviewer |
| RPT-OPS-01 | Operational Health Report | Access, interface, backup, incidents and configuration baseline | PDF/CSV | System Owner |

## 5. Output controls

Controlled reports show record ID, template/version, generation time, page x of y and signature manifestation. PDF/print/export shall not truncate values or omit context. Ad hoc extracts retain requester and query criteria.

Calculation and report verification shall use independent expected results, including boundary, rounding, unit-conversion and invalid-input cases. Report output verification shall compare displayed values, hidden metadata, pagination, filters, sorting, export format and signature manifestation against the approved source record.

| Verification focus | Minimum evidence |
|---|---|
| Formula correctness | Independent calculation workbook or script output retained as evidence |
| Boundary behavior | Values at and around specification limits are challenged |
| Unit/rounding control | Source precision, conversion rule and final display are verified |
| Report completeness | Required fields, signatures, exceptions and audit-review status are present |
| Export/print fidelity | PDF/CSV/print output matches source values and does not truncate context |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Input | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Output | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Output | QCL-2026-RPT-001 | [Report, Print and Export Verification Report](059_Report_Print_and_Export_Verification_Report.md) |
| Output | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |

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
