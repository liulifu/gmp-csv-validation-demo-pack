---
document_number: QCL-2026-URS-001
title: "User Requirements Specification"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Requirements"
version: "1.0"
effective_or_record_date: "2026-06-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "QC Business Process Owner"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# User Requirements Specification

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-URS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Requirements |
| Version | 1.0 |
| Effective/record date | 2026-06-30 |
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

This URS defines what the regulated users require from QCLabOne 2.0. Requirements describe intended outcomes and acceptance criteria without prescribing unnecessary implementation detail.

## 2. Requirement conventions

**Must** requirements are mandatory for release. **Should** requirements may be deferred only by approved change and business/quality risk assessment. Every requirement is uniquely identified and traceable.

## 3. Approved user requirements

| Requirement ID | Category | Requirement | Priority | Acceptance criterion |
|---|---|---|---|---|
| URS-GEN-001 | GEN | The system shall support GMP QC activities for chemistry, microbiology, stability and environmental monitoring at the Suzhou site. | Must | Approved workflows are available to each in-scope business area. |
| URS-GEN-002 | GEN | The system shall use a unique, non-reusable identifier for each sample, test assignment and approved record. | Must | Duplicate identifiers are rejected and all records remain traceable. |
| URS-GEN-003 | GEN | The system shall display the application name, environment and version to authorized users. | Should | Production, test and training environments are visibly distinguishable. |
| URS-GEN-004 | GEN | The system shall retain date/time in China Standard Time and store a synchronized technical timestamp. | Must | Timestamps reconcile to the approved time source within ±60 seconds. |
| URS-GEN-005 | GEN | The system shall prevent use of unapproved configuration in production. | Must | Only approved baseline items can be promoted through controlled release. |
| URS-SMP-001 | SMP | The system shall receive material, batch and sample-request data from SAP and create a pending sample request. | Must | A valid SAP message creates one pending request with message ID and source data. |
| URS-SMP-002 | SMP | The system shall generate a unique sample ID and barcode when a request is accepted. | Must | The sample ID and barcode are unique and printable. |
| URS-SMP-003 | SMP | The system shall record sample receipt date/time, receiver, condition, quantity and location. | Must | Required receipt fields cannot be bypassed. |
| URS-SMP-004 | SMP | The system shall support aliquot, transfer, return, rejection, cancellation and disposal events with reason and user attribution. | Must | Each event is time-stamped and audit-trailed. |
| URS-SMP-005 | SMP | The system shall assign tests from the effective product/material specification and sampling plan. | Must | Only the effective approved version is used. |
| URS-SMP-006 | SMP | The system shall prevent completion of a sample while required tests or investigations remain open. | Must | Completion is blocked with an explanatory message. |
| URS-SMP-007 | SMP | The system shall display chain-of-custody history for each sample and aliquot. | Must | All custody events are retrievable chronologically. |
| URS-SMP-008 | SMP | The system shall support stability pull schedules and overdue alerts. | Should | Pull dates, windows and overdue status are calculated correctly. |
| URS-SPEC-001 | SPEC | The system shall maintain version-controlled specifications, test methods and acceptance limits with effective dates. | Must | Draft, approved, effective and obsolete states are enforced. |
| URS-SPEC-002 | SPEC | Only authorized roles shall create, revise, approve or make a specification effective. | Must | Unauthorized attempts are rejected and logged. |
| URS-SPEC-003 | SPEC | A change to an effective specification shall not alter the historical version used by completed records. | Must | Historical records continue to display the original version. |
| URS-SPEC-004 | SPEC | The system shall support numeric, text, enumerated and qualitative result types. | Must | Configured result types validate data and limits correctly. |
| URS-SPEC-005 | SPEC | The system shall require documented approval before master data or specifications are promoted to production. | Must | Promotion requires approved change and electronic approval. |
| URS-LES-001 | LES | The system shall present approved electronic laboratory execution steps in the defined sequence. | Must | The analyst can execute only the effective approved worksheet. |
| URS-LES-002 | LES | Mandatory fields and prerequisite steps shall be enforced before a step can be completed. | Must | Omitted required data blocks completion. |
| URS-LES-003 | LES | The system shall record analyst observations, reagent, standard, instrument, lot and equipment references. | Must | References are linked to the test record and retrievable. |
| URS-LES-004 | LES | The system shall support direct capture from configured balances, pH meters and TOC analyzers. | Must | Transferred values include source device, date/time, unit and status. |
| URS-LES-005 | LES | Manual result entry shall require a reason and, for critical results, independent verification. | Must | Manual entries are identifiable and require configured verification. |
| URS-LES-006 | LES | The system shall support pause, resume, abort and repeat-test workflows with controlled reasons. | Must | Each action is recorded and follows configured authorization. |
| URS-LES-007 | LES | The system shall prevent an analyst from approving their own final result where second-person review is required. | Must | Self-approval is blocked. |
| URS-LES-008 | LES | The system shall identify overdue work and workflow exceptions to supervisors. | Should | Dashboards and notifications show overdue items accurately. |
| URS-CALC-001 | CALC | The system shall execute approved formulas using controlled input values and units. | Must | Calculated values match independently verified expected results. |
| URS-CALC-002 | CALC | The system shall apply approved significant figures and rounding rules. | Must | Boundary examples produce the specified rounded result. |
| URS-CALC-003 | CALC | The system shall maintain calculation version and formula history. | Must | Historical records identify the calculation version used. |
| URS-CALC-004 | CALC | The system shall evaluate results against effective limits and assign pass/fail or alert status. | Must | Boundary, inclusive and exclusive limits are handled correctly. |
| URS-CALC-005 | CALC | Changes to formulas or limit logic shall require change control, approval and regression testing. | Must | Unapproved changes cannot reach production. |
| URS-INT-001 | INT | The SAP interface shall receive sample requests and return inspection status and approved result disposition. | Must | Bidirectional messages reconcile by unique message ID. |
| URS-INT-002 | INT | The eQMS interface shall create OOS/OOT cases and receive the case identifier and status; CAPA creation is outside scope. | Must | One LIMS event creates one eQMS case without duplication. |
| URS-INT-003 | INT | The CDS/SDMS interface shall transfer approved numeric results, unit, sequence ID, method version and a stable record link; CDS remains the source of chromatographic raw data. | Must | Transferred data matches the approved CDS result and link opens for authorized users. |
| URS-INT-004 | INT | Instrument interfaces shall reject malformed, duplicate or out-of-range messages and place them in an exception queue. | Must | Exceptions are visible, attributable and reprocessable only by authorized roles. |
| URS-INT-005 | INT | All interfaces shall log send/receive time, source, destination, message ID, status and error text. | Must | Audit and reconciliation reports are available. |
| URS-INT-006 | INT | The system shall support controlled manual contingency entry during an approved interface outage. | Should | Manual fallback is labeled and independently verified. |
| URS-SEC-001 | SEC | Users shall authenticate through the corporate identity service using unique individual accounts. | Must | Shared accounts are rejected except approved technical accounts. |
| URS-SEC-002 | SEC | Role-based access shall follow least privilege and the approved access matrix. | Must | Each role passes positive and negative access testing. |
| URS-SEC-003 | SEC | Privileged administration shall be separated from routine QC data approval. | Must | No production role can both administer configuration and approve final QC results. |
| URS-SEC-004 | SEC | Inactive sessions shall lock after 15 minutes and require re-authentication. | Must | Session behavior meets the configured timeout. |
| URS-SEC-005 | SEC | Account creation, change, disablement and privileged access shall be approved and logged. | Must | Access records identify requester, approver, executor and date. |
| URS-SEC-006 | SEC | Vendor remote access shall be time-limited, company-approved, monitored and disabled by default. | Must | Remote sessions require a ticket and generate connection logs. |
| URS-SEC-007 | SEC | Security events and failed logins shall be logged and reviewable. | Should | Reports show user, timestamp, source and event outcome. |
| URS-DI-001 | DI | The system shall maintain secure computer-generated audit trails for creation, modification, deletion, status change and approval of GxP records. | Must | Challenge tests show complete old/new values, user and timestamp. |
| URS-DI-002 | DI | A reason for change shall be mandatory for changes to results, specifications, formulas, workflow status and critical master data. | Must | The record cannot be saved without an approved reason. |
| URS-DI-003 | DI | Audit trails shall be protected from alteration by ordinary users and administrators performing routine tasks. | Must | No tested role can edit or delete audit trail entries. |
| URS-DI-004 | DI | Authorized reviewers shall be able to filter, view and export audit trails without changing the source data. | Must | Exported audit trail is complete and attributable. |
| URS-DI-005 | DI | The system shall preserve record context, metadata, attachments and links for the full retention period. | Must | Archived records remain readable and retrievable. |
| URS-DI-006 | DI | Deletion or purge of GxP records shall be disabled except through an approved retention process with documented authorization. | Must | Routine roles cannot permanently delete records. |
| URS-DI-007 | DI | Data transfers and migration shall be reconciled for completeness, accuracy and relationship integrity. | Must | Approved reconciliation criteria are met. |
| URS-DI-008 | DI | System time shall be synchronized and time-zone changes shall be controlled and logged. | Must | Time records align with the approved authoritative source. |
| URS-ESIG-001 | ESIG | Electronic signatures shall be unique to one individual and linked to the signed record. | Must | The signature cannot be copied or detached through ordinary means. |
| URS-ESIG-002 | ESIG | The signature manifestation shall show signer name, date/time and meaning. | Must | Printed and electronic views show all required elements. |
| URS-ESIG-003 | ESIG | Critical signatures shall require re-entry of credentials or approved re-authentication. | Must | A second authentication event is recorded. |
| URS-ESIG-004 | ESIG | Signed records shall be invalidated or re-routed for approval when defined critical data changes after signature. | Must | Post-signature changes trigger the configured workflow and audit trail. |
| URS-REP-001 | REP | The system shall generate controlled test reports and CoA-supporting data using approved templates. | Must | Report content matches approved record data and template version. |
| URS-REP-002 | REP | Reports shall identify record ID, report version, generation date/time and generating user or service. | Must | Metadata is visible on each output. |
| URS-REP-003 | REP | PDF export and printing shall preserve content, pagination, units and signature manifestations. | Must | Verification confirms no truncation or data substitution. |
| URS-REP-004 | REP | Ad hoc data extracts used for GMP decisions shall be access-controlled and retain query criteria. | Should | The extract records filters, date/time and requester. |
| URS-BCP-001 | BCP | Production data shall be backed up according to approved recovery objectives. | Must | Backup logs meet frequency and retention requirements. |
| URS-BCP-002 | BCP | The service shall support an RPO of 15 minutes and RTO of 8 hours for a declared disaster. | Must | DR testing demonstrates approved objectives or documents justified deviations. |
| URS-BCP-003 | BCP | A tested restore process shall recover application data, configuration, audit trails and attachments. | Must | Restored records reconcile to the selected backup point. |
| URS-BCP-004 | BCP | Business continuity procedures shall define manual sample receipt, result recording and later reconciliation during outage. | Must | A tabletop and technical exercise demonstrate the fallback. |
| URS-MIG-001 | MIG | Legacy records selected for migration shall be mapped, transformed, reconciled and approved before production use. | Must | Record counts, critical fields and relationships meet approved criteria. |
| URS-MIG-002 | MIG | Historical records not migrated shall be retained in a validated read-only archive with audit trail and attachment access. | Must | Retrieval tests meet the approved sample plan. |
| URS-MIG-003 | MIG | Migration exceptions shall be documented, risk-assessed, resolved or accepted before go-live. | Must | No critical unresolved exception remains. |
| URS-MIG-004 | MIG | Source data shall remain protected and available until migration and archive acceptance are approved. | Must | Legacy data is not altered or decommissioned early. |
| URS-OPS-001 | OPS | The system shall support periodic access review, audit trail review, backup monitoring, incident and change records. | Must | Required reports and evidence can be generated. |
| URS-OPS-002 | OPS | The supplier shall notify the company of planned changes, incidents and security events within agreed timelines. | Must | SLA evidence demonstrates notification and escalation. |
| URS-OPS-003 | OPS | The validated state shall be reviewed at least annually and after significant change or incident. | Must | Periodic review evaluates current configuration, risks and records. |
| URS-OPS-004 | OPS | System retirement shall preserve required records and remove obsolete access and interfaces in a controlled manner. | Must | Retirement evidence confirms retention and decommissioning. |

## 4. Category key

GEN—general; SMP—sample management; SPEC—specification/master data; LES—laboratory execution; CALC—calculation; INT—interface; SEC—security; DI—data integrity; ESIG—electronic signature; REP—reporting; BCP—continuity; MIG—migration; OPS—operation/retirement.

## 5. Change control

After approval, changes require documented rationale, impact on risk/design/test/training/migration, version update and approval by the Business Process Owner with QA review.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Input | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Input | QCL-2026-PRA-001 | [Preliminary Risk Assessment](011_Preliminary_Risk_Assessment.md) |
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Input | QCL-2026-ERES-001 | [21 CFR Part 11 and EU Annex 11 Assessment](013_21_CFR_Part_11_and_EU_Annex_11_Assessment.md) |
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Input | QCL-2026-RFP-001 | [RFI, RFP and Product Selection Record](017_RFI_RFP_and_Product_Selection_Record.md) |
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
| Prepared by | QC Business Process Owner | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-06-30 | Initial approved fictional case version. |
