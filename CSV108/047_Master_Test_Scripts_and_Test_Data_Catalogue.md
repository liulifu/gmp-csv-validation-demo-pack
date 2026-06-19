---
document_number: QCL-2026-MTS-001
title: "Master Test Scripts and Test Data Catalogue"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Verification"
version: "1.0"
effective_or_record_date: "2027-02-28"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "Business Process Owner"
approved_by: "QA Validation Manager"
---

# Master Test Scripts and Test Data Catalogue

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-MTS-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Verification |
| Version | 1.0 |
| Effective/record date | 2027-02-28 |
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

This catalogue is the controlled index of formal test scripts and test data used by the validation programme.

## 2. Script catalogue

| Test ID | Title | Level/type | Final case outcome |
|---|---|---|---|
| IQ-001 | Verify approved cloud tenant, production URL and environment identification | IQ | Pass |
| IQ-002 | Verify application version 8.4.2-HF1 and license modules | IQ | Pass |
| IQ-003 | Verify QCL-IGW-01 server OS, CPU, memory, disk and hardening | IQ | Pass |
| IQ-004 | Verify PostgreSQL managed database service and encryption settings | IQ | Pass |
| IQ-005 | Verify corporate identity federation and time synchronization | IQ | Pass |
| IQ-006 | Verify network routes, firewall rules and TLS certificates | IQ | Pass |
| IQ-007 | Verify backup jobs, retention and monitoring configuration | IQ | Pass |
| IQ-008 | Verify antivirus/EDR and vulnerability baseline on gateway | IQ | Pass |
| IQ-009 | Verify production, validation and training environment segregation | IQ | Pass |
| IQ-010 | Verify installed barcode printers, scanners and drivers | IQ | Pass |
| IQ-011 | Verify interface service accounts and secret storage | IQ | Pass |
| IQ-012 | Verify application log and audit log storage | IQ | Pass |
| IQ-013 | Verify approved configuration package checksum | IQ | Pass |
| IQ-014 | Verify document and supplier evidence availability | IQ | Pass |
| IQ-015 | Verify restore and DR procedures are available and approved | IQ | Pass |
| OQ-SMP-001 | Create SAP-origin sample request; generate sample ID and barcode | OQ | Pass |
| OQ-SMP-002 | Record receipt, reject, transfer, aliquot and disposal with custody history | OQ | Pass |
| OQ-SMP-003 | Assign tests from effective specification and block closure with open work | OQ | Pass |
| OQ-SMP-004 | Calculate stability pull date and overdue alert | OQ | Pass |
| OQ-SPEC-001 | Create, approve, effective-date and obsolete a specification | OQ | Pass |
| OQ-SPEC-002 | Confirm historical record retains original specification/method version | OQ | Pass |
| OQ-SPEC-003 | Verify numeric, qualitative, text and enumerated result types | OQ | Pass |
| OQ-LES-001 | Execute approved LES steps and enforce prerequisites/mandatory fields | OQ | Pass |
| OQ-LES-002 | Capture reagent, standard, instrument and lot references | OQ | Pass |
| OQ-LES-003 | Direct capture from balance, pH meter and TOC analyzer | OQ | Pass |
| OQ-LES-004 | Manual entry reason and independent verification | OQ | Pass |
| OQ-LES-005 | Pause, abort, repeat-test and exception dashboard | OQ | Pass |
| OQ-LES-006 | Prevent analyst self-approval | OQ | Pass |
| OQ-CALC-001 | Verify assay and dilution formula calculations | OQ | Pass |
| OQ-CALC-002 | Verify significant figures, rounding and boundary limits | OQ | Pass |
| OQ-CALC-003 | Verify formula history and controlled change | OQ | Pass |
| OQ-SEC-001 | Verify SSO, unique account and disabled local login | OQ | Pass |
| OQ-SEC-002 | Verify positive/negative permissions for each business role | OQ | Pass |
| OQ-SEC-003 | Verify session lock and account disablement | OQ | Pass |
| OQ-SEC-004 | Verify vendor remote access approval, timeout and logging | OQ | Pass |
| OQ-DI-001 | Verify system time synchronization and timezone control | OQ | Pass |
| OQ-DI-002 | Verify record retention and routine deletion restrictions | OQ | Pass |
| OQ-OPS-001 | Generate access, audit trail, backup and operational reports | OQ | Pass |
| OQ-GEN-001 | Verify application/environment/version display | OQ | Pass |
| OQ-GEN-002 | Verify unique identifier non-reuse and production baseline control | OQ | Pass |
| IFT-SAP-001 | Inbound SAP sample request happy path | Interface | Pass |
| IFT-SAP-002 | Duplicate and malformed SAP message handling | Interface | Pass |
| IFT-SAP-003 | Outbound inspection status/result acknowledgement and reconciliation | Interface | Pass |
| IFT-EQM-001 | Create one OOS/OOT case and receive case ID/status | Interface | Pass |
| IFT-EQM-002 | Retry without duplicate eQMS case creation | Interface | Pass after DEF-003 |
| IFT-CDS-001 | Transfer approved result, unit, sequence ID, method version and link | Interface | Pass |
| IFT-CDS-002 | Reject unapproved or inconsistent CDS result | Interface | Pass |
| IFT-INS-001 | Instrument message source identity, unit and timestamp | Interface | Pass |
| IFT-INS-002 | Exception queue and authorized reprocessing | Interface | Pass |
| IFT-ALL-001 | Interface outage contingency entry and reconciliation | Interface | Pass |
| SEC-001 | Role matrix positive and negative access challenge | Security | Pass |
| SEC-002 | Segregation of administration and QC approval | Security | Pass |
| SEC-003 | Account request, approval, change and disablement evidence | Security | Pass |
| SEC-004 | Failed login and security event reporting | Security | Pass |
| SEC-005 | Service account non-interactive restrictions | Security | Pass |
| ATC-001 | Audit trail for result create/change/delete attempt | Audit trail | Pass |
| ATC-002 | Audit trail for specification, formula and master-data change | Audit trail | Pass after DEV-001 |
| ATC-003 | Mandatory reason for critical change | Audit trail | Pass after DEV-001 |
| ATC-004 | Audit trail protection, filter, export and review | Audit trail | Pass |
| ATC-005 | Audit trail for role, signature and workflow status events | Audit trail | Pass |
| EST-001 | Electronic signature uniqueness and re-authentication | E-signature | Pass |
| EST-002 | Signature manifestation: name, date/time and meaning | E-signature | Pass |
| EST-003 | Signature-to-record binding and post-signature change workflow | E-signature | Pass |
| EST-004 | Negative test for invalid credentials and session reuse | E-signature | Pass |
| DMT-001 | Legacy data extraction count and checksum | Migration | Pass |
| DMT-002 | Critical field mapping and transformation verification | Migration | Pass |
| DMT-003 | Attachment and special-character filename migration | Migration | Pass after DEV-002 |
| DMT-004 | Record relationship and audit trail preservation | Migration | Pass |
| DMT-005 | Archive-only record retrieval and comparison | Migration | Pass |
| DMT-006 | Migration exception disposition and rerun | Migration | Pass |
| BRT-001 | Full backup completion and encrypted storage | Backup/Restore | Pass |
| BRT-002 | Point-in-time database restore | Backup/Restore | Pass |
| BRT-003 | Attachment, configuration and audit trail restore | Backup/Restore | Pass |
| BRT-004 | Restored record reconciliation and access control | Backup/Restore | Pass |
| PLC-001 | 200 concurrent user mixed workload | Performance | Pass |
| PLC-002 | Peak interface throughput of 10,000 messages/hour | Performance | Pass |
| PLC-003 | Report generation for 100,000-result dataset | Performance | Pass |
| PLC-004 | Capacity forecast for five years and alert thresholds | Performance | Pass |
| DRT-001 | Application node failover without data loss | DR/Failover | Pass |
| DRT-002 | Regional DR activation and service restoration | DR/Failover | Pass |
| DRT-003 | RPO/RTO measurement and data reconciliation | DR/Failover | Pass |
| DRT-004 | Manual business continuity and post-recovery reconciliation | DR/Failover | Pass |
| RPT-001 | Controlled analytical test report verification | Report | Pass |
| RPT-002 | CoA-supporting data extract verification | Report | Pass |
| RPT-003 | PDF/print pagination, units and signature manifestation | Report | Pass |
| RPT-004 | Ad hoc extract access and query-criteria retention | Report | Pass |
| PQ-001 | Raw material sample end-to-end workflow | PQ/UAT | Pass |
| PQ-002 | Finished product assay workflow with CDS result | PQ/UAT | Pass |
| PQ-003 | Microbiology environmental monitoring workflow | PQ/UAT | Pass |
| PQ-004 | Stability pull scheduling and result approval | PQ/UAT | Pass |
| PQ-005 | OOS/OOT initiation and eQMS linkage | PQ/UAT | Pass |
| PQ-006 | Sample rejection, cancellation and resampling | PQ/UAT | Pass |
| PQ-007 | Outage manual contingency and reconciliation | PQ/UAT | Pass |
| PQ-008 | Reviewer audit trail review and approval | PQ/UAT | Pass |
| PQ-009 | Controlled report generation and SAP disposition return | PQ/UAT | Pass |
| PQ-010 | Role-based operating scenario for analyst/reviewer/supervisor/QA | PQ/UAT | Pass |
| PQ-011 | Legacy record retrieval during inspection simulation | PQ/UAT | Pass |
| PQ-012 | System administration under approved change and access procedure | PQ/UAT | Pass |

## 3. Test data catalogue

| Data set | Purpose | Key records |
|---|---|---|
| TD-QCL-BASE-01 | Normal sample workflows | RM-001, FP-001, STAB-001, EM-001 |
| TD-QCL-BND-01 | Calculation and limit boundaries | Assay lower/upper, rounding half values, zero/negative invalid cases |
| TD-QCL-SEC-01 | Role/negative access | Ten synthetic users mapped to each approved/conflicting role |
| TD-QCL-INT-01 | Interface normal/error/retry | Valid, duplicate, malformed, late and out-of-order messages |
| TD-QCL-MIG-01 | Migration trial | 10,000 samples, 38,000 results, 2,000 attachments incl. special characters |
| TD-QCL-LOAD-01 | Performance/load | 100,000 samples and five-year projected transaction set |
| TD-QCL-DR-01 | Recovery reconciliation | Selected signed records, audit events, attachments and queued messages |

## 4. Script control

Scripts are version 1.0 unless the deviation/retest record identifies a controlled revision. Final executed evidence remains in the eDMS and is referenced by the same Test ID.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Input | QCL-2026-FRA-001 | [Functional Risk Assessment](038_Functional_Risk_Assessment.md) |
| Input | QCL-2026-RTM-001 | [Initial Requirements Traceability Matrix](039_Initial_Requirements_Traceability_Matrix.md) |
| Input | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
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

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-02-28 | Initial approved fictional case version. |
