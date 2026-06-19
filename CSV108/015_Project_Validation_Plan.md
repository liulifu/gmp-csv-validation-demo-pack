---
document_number: QCL-2026-VP-001
title: "QCLabOne 2.0 Project Validation Plan"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Validation Planning"
version: "1.0"
effective_or_record_date: "2026-05-15"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV Project Manager"
reviewed_by: "QC Business Process Owner"
approved_by: "QA Validation Manager"
---

# QCLabOne 2.0 Project Validation Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-VP-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Validation Planning |
| Version | 1.0 |
| Effective/record date | 2026-05-15 |
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

This Project Validation Plan defines the prospective, risk-based strategy for implementing and releasing QCLabOne 2.0 LIMS/LES. It is subordinate to the site CSV procedure and VMP.

## 2. Validation scope

The scope is defined in [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) and includes the configurable application, custom interfaces, site configuration, calculations/reports, data migration, production baseline, SOP/training and legacy-retirement dependencies.

## 3. Validation approach

| Area | Approach |
|---|---|
| Supplier evidence | Leverage assessed standard product SDLC, platform qualification and baseline functional tests |
| Site configuration | Company-approved specification and risk-based OQ |
| Custom integrations | Development plan, code review, unit test, FAT/SAT and interface verification |
| Business processes | Representative PQ/UAT by trained QC users |
| Data migration | Two trial cycles plus production reconciliation and exception management |
| Electronic records/signatures | Dedicated Part 11/Annex 11, audit trail and e-signature assessment/testing |
| Infrastructure | Supplier qualification plus IQ of site gateway, connectivity, identity, backup and monitoring |
| Operation | Approved SOPs, training, handover, baseline and first-year review evidence |

## 4. Deliverables

Applicable deliverables are listed in the Master Deliverable List. Documents may be combined only through approved change to this plan; traceability and approval requirements shall remain satisfied.

## 5. Risk and traceability

PRA and DIRA establish early controls. FRA links functional hazards to URS and verification. The initial RTM is established after design; the final RTM must show every approved URS covered by passing evidence or an approved rationale.

## 6. Test governance

- Test scripts require objective preconditions, steps, expected result and evidence reference.
- Testers shall be trained and independent of the specific configuration where practicable.
- Critical functions use scripted challenge tests; lower-risk usability observations may use unscripted UAT with recorded results.
- Test data shall be synthetic and uniquely identified.
- Failed expected results are recorded as defects/deviations; correction and retest evidence remain linked.
- Production data shall not be used in non-production environments without approved masking.

## 7. Acceptance and release criteria

| Criterion | Requirement |
|---|---|
| Requirements coverage | 100% of Must URS have approved passing coverage |
| Critical/high risk | Control verified; no unacceptable residual risk |
| Defects/deviations | No Critical/High open; Medium items formally assessed |
| Migration | Counts and critical fields accepted; no critical unresolved exception |
| Training/SOP | Effective and complete before production access |
| Backup/DR | Restore and DR evidence meets approved objectives or accepted exception |
| Production baseline | Configuration/version/checksum documented and approved |
| Quality conclusion | Approved VSR and release approval |

## 8. Schedule and gates

Design baseline: 2026-10-31; FAT: 2027-01-25; SAT: 2027-02-20; IQ/OQ/PQ: 2027-03-01 to 2027-04-30; VSR: 2027-06-05; go-live: 2027-06-15.

Gate review shall include deliverable status, traceability coverage, open risks, deviations, defects, supplier actions, training readiness, environment readiness and data-migration status. Conditional gate approval is permitted only when the condition does not allow unvalidated regulated use and has a named owner, due date and QA-approved impact statement.

| Gate decision input | Acceptance expectation |
|---|---|
| Deliverable completeness | Required records are approved or have QA-approved deferral rationale |
| Traceability | High-risk URS/risk controls have planned or completed verification coverage |
| Test readiness | Environment, data, scripts and trained executors are approved before execution |
| Release readiness | VSR, SOPs, training, migration, support and baseline are complete |
| Residual risk | No unacceptable residual GxP or data-integrity risk remains |

## 9. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Governing | SOP-CSV-001 | [Site Computerised System Lifecycle Management Procedure](001_CSV_Lifecycle_Management_Procedure.md) |
| Governing | VMP-SZ-001 | [Site Validation Master Plan](002_Validation_Master_Plan.md) |
| Input | QCL-2026-RACI-001 | [QCLabOne 2.0 CSV RACI and Responsibilities Matrix](004_CSV_RACI_and_Responsibilities_Matrix.md) |
| Input | QCL-2026-CHA-001 | [QCLabOne 2.0 Project Charter](005_Project_Charter.md) |
| Input | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Input | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Input | QCL-2026-PRA-001 | [Preliminary Risk Assessment](011_Preliminary_Risk_Assessment.md) |
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Output | QCL-2026-MDL-001 | [Master Deliverable List and Schedule](016_Master_Deliverable_List_and_Schedule.md) |
| Output | QCL-2026-RFP-001 | [RFI, RFP and Product Selection Record](017_RFI_RFP_and_Product_Selection_Record.md) |
| Output | QCL-2026-SQA-001 | [Supplier Qualification Assessment](018_Supplier_Qualification_Assessment.md) |
| Output | QCL-2026-SAR-001 | [Supplier Audit Report and CAPA](019_Supplier_Audit_Report_and_CAPA.md) |
| Output | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Output | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Output | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Output | QCL-2026-FS-001 | [Functional Specification](023_Functional_Specification.md) |
| Output | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Output | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Output | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Output | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Output | QCL-2026-DDS-001 | [Data Flow, Data Dictionary and Metadata Specification](028_Data_Flow_Data_Dictionary_and_Metadata_Specification.md) |
| Output | QCL-2026-RCS-001 | [Report and Calculation Specification](029_Report_and_Calculation_Specification.md) |
| Output | QCL-2026-MDS-001 | [Master Data Specification](030_Master_Data_Specification.md) |
| Output | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Output | QCL-2026-ATS-001 | [Audit Trail Specification](032_Audit_Trail_Specification.md) |
| Output | QCL-2026-ESS-001 | [Electronic Signature Specification](033_Electronic_Signature_Specification.md) |
| Output | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Output | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Output | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |
| Output | QCL-2026-DMS-001 | [Data Mapping, Cleansing and Transformation Specification](037_Data_Mapping_Cleansing_and_Transformation_Specification.md) |
| Output | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Output | QCL-2026-RTM-001 | [Initial Requirements Traceability Matrix](039_Initial_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Output | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Output | QCL-2026-SDP-001 | [Software Development and Source Control Plan](042_Software_Development_and_Source_Control_Plan.md) |
| Output | QCL-2026-CRU-001 | [Code Review and Unit Test Report](043_Code_Review_and_Unit_Test_Report.md) |
| Output | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Output | QCL-2026-MTS-001 | [Master Test Scripts and Test Data Catalogue](047_Master_Test_Scripts_and_Test_Data_Catalogue.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-OQ-001 | [Operational Qualification Protocol and Report](049_Operational_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-PQ-001 | [Performance Qualification and User Acceptance Test Report](050_Performance_Qualification_and_UAT_Report.md) |
| Output | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Output | QCL-2026-DMT-001 | [Data Migration Test and Reconciliation Report](052_Data_Migration_Test_and_Reconciliation_Report.md) |
| Output | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Output | QCL-2026-ATC-001 | [Audit Trail Challenge Test Report](054_Audit_Trail_Challenge_Test_Report.md) |
| Output | QCL-2026-EST-001 | [Electronic Signature Test Report](055_Electronic_Signature_Test_Report.md) |
| Output | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Output | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Output | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Output | QCL-2026-RPT-001 | [Report, Print and Export Verification Report](059_Report_Print_and_Export_Verification_Report.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |
| Output | QCL-2026-DEV-001 | [Validation Deviation Log and Investigation Report](061_Validation_Deviation_Log_and_Investigation_Report.md) |
| Output | QCL-2026-CAPA-001 | [CAPA Record and Effectiveness Check](062_CAPA_Record_and_Effectiveness_Check.md) |
| Output | QCL-2026-TSR-001 | [Test Summary Report](063_Test_Summary_Report.md) |
| Output | QCL-2026-RTM-002 | [Final Requirements Traceability Matrix](064_Final_Requirements_Traceability_Matrix.md) |
| Output | QCL-2026-VSR-001 | [Validation Summary Report](065_Validation_Summary_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV Project Manager | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-05-15 | Initial approved fictional case version. |
