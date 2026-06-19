---
document_number: QCL-2026-RACI-001
title: "QCLabOne 2.0 CSV RACI and Responsibilities Matrix"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "CSV Governance"
version: "1.0"
effective_or_record_date: "2026-01-25"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV Program Lead"
reviewed_by: "QA Validation Manager"
approved_by: "Site Quality Head"
---

# QCLabOne 2.0 CSV RACI and Responsibilities Matrix

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-RACI-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | CSV Governance |
| Version | 1.0 |
| Effective/record date | 2026-01-25 |
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

This matrix defines lifecycle accountability. Each activity has one and only one **A (Accountable)**. Additional required quality or business approvals may be recorded in the associated document, but accountability remains singular.

## 2. Role abbreviations

- **SP** — Project Sponsor
- **BPO** — QC Business Process Owner
- **SO** — System Owner
- **QA** — QA Validation Manager
- **PM** — CSV Project Manager
- **IT** — IT/Infrastructure Owner
- **VEN** — Supplier
- **MIG** — Data Migration Lead
- **RM** — Records Management Owner

## 3. RACI matrix

| Activity | SP | BPO | SO | QA | PM | IT | VEN | MIG | RM |
|---|---|---|---|---|---|---|---|---|---|
| Approve site CSV procedure/VMP | I | I | I | A | R | C | C | I | I |
| Approve project charter and funding | A | C | C | C | R | I | I | I | I |
| Define scope and intended use | I | A | R | C | R | C | C | C | I |
| Describe business process | I | A | R | C | R | C | C | C | I |
| Maintain system inventory | I | C | A | C | R | R | I | I | C |
| Perform GxP/classification/PRA | I | C | R | A | R | C | C | C | I |
| Perform DIRA/Part 11 assessment | I | C | R | A | R | C | C | C | C |
| Approve project validation plan | I | C | R | A | R | C | C | C | I |
| Select and qualify supplier | C | C | R | A | R | C | R | I | I |
| Approve URS | I | A | R | C | R | C | C | C | I |
| Approve design/configuration | I | C | A | C | R | R | R | C | I |
| Approve migration strategy | I | C | R | C | R | C | C | A | C |
| Build/configure system | I | C | A | C | R | R | R | C | I |
| Develop custom interfaces | I | C | A | C | R | R | R | C | I |
| Approve test plan/scripts | I | C | R | A | R | C | C | C | I |
| Execute IQ | I | I | A | C | R | R | C | I | I |
| Execute OQ | I | C | A | C | R | C | R | C | I |
| Execute PQ/UAT | I | A | R | C | R | C | C | C | I |
| Manage defects/deviations | I | C | A | C | R | C | R | C | I |
| Accept residual validation risk | I | C | R | A | C | C | I | C | I |
| Approve VSR | I | C | R | A | R | C | C | C | I |
| Approve go-live business decision | I | A | R | C | R | C | I | C | I |
| Provision production access | I | C | A | C | I | R | I | I | I |
| Operate and support system | I | C | A | C | I | R | R | I | I |
| Perform periodic access/audit review | I | C | A | C | I | R | C | I | I |
| Approve changes and patches | I | C | A | C | R | R | C | I | I |
| Perform annual periodic review | I | C | A | C | R | R | C | I | C |
| Approve archive acceptance | I | C | R | C | I | C | C | R | A |
| Approve legacy retirement | I | C | A | C | R | R | C | C | R |
| Approve final retirement conclusion | I | C | R | A | R | C | I | C | C |

## 4. Decision rules

- QA is accountable for the validation strategy, residual GxP risk acceptance and final validation conclusion.
- The BPO is accountable for intended use, URS and business go-live acceptance.
- The System Owner is accountable for technical design, production access, operation, change and retirement execution.
- Records Management is accountable for archive acceptance.
- Emergency actions may be taken to protect product, data or continuity, but must be documented and entered into deviation/change control within one business day.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | SOP-CSV-001 | [Site Computerised System Lifecycle Management Procedure](001_CSV_Lifecycle_Management_Procedure.md) |
| Input | VMP-SZ-001 | [Site Validation Master Plan](002_Validation_Master_Plan.md) |
| Input | QCL-2026-CHA-001 | [QCLabOne 2.0 Project Charter](005_Project_Charter.md) |
| Output | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Output | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Output | QCL-2026-PRA-001 | [Preliminary Risk Assessment](011_Preliminary_Risk_Assessment.md) |
| Output | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Output | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Output | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Output | QCL-2026-VP-001 | [QCLabOne 2.0 Project Validation Plan](015_Project_Validation_Plan.md) |
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
| Output | SOP-QC-LIMS-001 | [QCLabOne 2.0 User Operation SOP](066_User_Operation_SOP.md) |
| Output | SOP-IT-LIMS-001 | [QCLabOne 2.0 System Administration SOP](067_System_Administration_SOP.md) |
| Output | SOP-QA-ATR-001 | [QCLabOne 2.0 Audit Trail Review SOP](068_Audit_Trail_Review_SOP.md) |
| Output | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Output | SOP-QA-ARC-001 | [Data Retention, Archiving and Record Retrieval SOP](070_Data_Retention_Archiving_and_Record_Retrieval_SOP.md) |
| Output | QCL-2026-TRN-001 | [Training Plan, Materials and Training Record](071_Training_Plan_Materials_and_Training_Record.md) |
| Output | QCL-2026-CUT-001 | [Cutover, Rollback and Contingency Plan](072_Cutover_Rollback_and_Contingency_Plan.md) |
| Output | QCL-2026-PDM-001 | [Production Data Migration Execution and Reconciliation Record](073_Production_Data_Migration_Execution_and_Reconciliation_Record.md) |
| Output | QCL-2026-PRC-001 | [Production Readiness Checklist](074_Production_Readiness_Checklist.md) |
| Output | QCL-2026-GLA-001 | [Go-Live and Production Release Approval](075_Go_Live_and_Production_Release_Approval.md) |
| Output | QCL-2026-HOV-001 | [System Handover and Support Model](076_System_Handover_and_Support_Model.md) |
| Output | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |
| Output | QCL-2027-UAR-001 | [User Access Request and Approval Records](078_User_Access_Request_and_Approval_Records.md) |
| Output | QCL-2027-UAR-002 | [Periodic User Access Review Report](079_Periodic_User_Access_Review_Report.md) |
| Output | QCL-2027-SOD-001 | [Segregation of Duties and Privileged Access Review](080_Segregation_of_Duties_and_Privileged_Access_Review.md) |
| Output | QCL-2027-ATR-001 | [Periodic Audit Trail Review Record](081_Periodic_Audit_Trail_Review_Record.md) |
| Output | QCL-2027-DIM-001 | [Data Integrity Monitoring and Trend Report](082_Data_Integrity_Monitoring_and_Trend_Report.md) |
| Output | QCL-2027-BML-001 | [Backup Monitoring Log and Exception Record](083_Backup_Monitoring_Log_and_Exception_Record.md) |
| Output | QCL-2027-RST-001 | [Periodic Restore Test Report](084_Periodic_Restore_Test_Report.md) |
| Output | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2027-PRB-006 | [Problem Record and Root Cause Analysis](086_Problem_Record_and_Root_Cause_Analysis.md) |
| Output | QCL-2027-ODV-004 | [Operational Deviation and CAPA Record](087_Operational_Deviation_and_CAPA_Record.md) |
| Output | QCL-2027-CHG-021 | [Change Control Record](088_Change_Control_Record.md) |
| Output | QCL-2027-PAT-003 | [Patch and Upgrade Impact Assessment](089_Patch_and_Upgrade_Impact_Assessment.md) |
| Output | QCL-2027-REG-003 | [Regression Test Plan and Report](090_Regression_Test_Plan_and_Report.md) |
| Output | QCL-2027-CHG-021-C | [Change Implementation Verification and Closure](091_Change_Implementation_Verification_and_Closure.md) |
| Output | QCL-2028-PRR-001 | [Annual Periodic Review Report](092_Annual_Periodic_Review_Report.md) |
| Output | QCL-2028-RVA-001 | [Revalidation Assessment and Report](093_Revalidation_Assessment_and_Report.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |
| Output | QCL-2028-DRE-001 | [Business Continuity and Disaster Recovery Exercise Report](095_Business_Continuity_and_DR_Exercise_Report.md) |
| Output | QCL-2028-SPR-001 | [Supplier Periodic Performance and SLA Review](096_Supplier_Periodic_Performance_and_SLA_Review.md) |
| Output | QCL-2028-ARC-001 | [System and Data Archive Record](097_System_and_Data_Archive_Record.md) |
| Output | QCL-2028-IRD-001 | [Inspection Readiness Dossier and Audit Response Record](098_Inspection_Readiness_Dossier_and_Audit_Response_Record.md) |
| Output | QCL-2028-DCR-001 | [Legacy LIMS Decommissioning Request](099_Legacy_LIMS_Decommissioning_Request.md) |
| Output | QCL-2028-RRA-001 | [Legacy LIMS Retirement Risk Assessment](100_Legacy_LIMS_Retirement_Risk_Assessment.md) |
| Output | QCL-2028-RTP-001 | [Legacy LIMS Retirement Plan](101_Legacy_LIMS_Retirement_Plan.md) |
| Output | QCL-2028-LAR-001 | [Legacy Data Archiving and Retention Plan](102_Legacy_Data_Archiving_and_Retention_Plan.md) |
| Output | QCL-2028-AVR-001 | [Legacy Archive Verification and Retrievability Report](103_Legacy_Archive_Verification_and_Retrievability_Report.md) |
| Output | QCL-2028-AIS-001 | [Legacy Access Revocation and Interface Shutdown Record](104_Legacy_Access_Revocation_and_Interface_Shutdown_Record.md) |
| Output | QCL-2028-DCL-001 | [Legacy System Decommissioning Checklist](105_Legacy_System_Decommissioning_Checklist.md) |
| Output | QCL-2028-RSR-001 | [Legacy LIMS Retirement Summary Report](106_Legacy_LIMS_Retirement_Summary_Report.md) |
| Output | CSI-SZ-001-CHG-2028-03 | [Computerised System Inventory Update—Retired Status](107_Computerised_System_Inventory_Update_Retired_Status.md) |
| Output | QCL-2028-FDI-001 | [Final Validation and Retirement Dossier Index](108_Final_Validation_and_Retirement_Dossier_Index.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV Program Lead | Completed |
| Reviewed by | QA Validation Manager | Completed |
| Approved by | Site Quality Head | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-01-25 | Initial approved fictional case version. |
