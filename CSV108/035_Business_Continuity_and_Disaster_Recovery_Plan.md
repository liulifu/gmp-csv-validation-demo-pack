---
document_number: QCL-2026-BCP-001
title: "Business Continuity and Disaster Recovery Plan"
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

# Business Continuity and Disaster Recovery Plan

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-BCP-001 |
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

## 1. Objectives

Maintain safe QC operations during outage and restore the system without loss or uncontrolled duplication. Target RPO is 15 minutes and RTO is 8 hours for declared disaster.

## 2. Scenario matrix

| Scenario | Immediate response | Continuity mode | Recovery |
|---|---|---|---|
| Application unavailable | Open P1 incident; confirm scope; notify QC/QA | Controlled paper sample receipt/results where authorised | Restore service; reconcile all contingency records |
| Interface gateway failure | Queue upstream messages; stop direct capture | Manual verified entry and controlled message log | Restore gateway; replay/reconcile by message ID |
| Cloud region disaster | Declare DR after supplier/company approval | Prioritise critical samples and paper controls | Activate standby region and reconcile to recovery point |
| Identity service unavailable | Use sealed break-glass accounts only if QA/IT approve | Restricted critical operation | Reconcile users/actions and disable break-glass |
| Cybersecurity event | Isolate affected component; preserve evidence | Use unaffected validated controls/manual process | Forensic assessment, clean recovery, QA release |
| Archive unavailable | Use secondary archive copy | Inspection retrieval by Records Management | Restore primary and verify integrity |

## 3. Roles and communications

Incident Commander: IT Duty Manager. Business Continuity Lead: QC BPO. GxP impact: QA. Technical recovery: Supplier + IT. External/regulatory communication: Site Quality Head/Regulatory Affairs.

## 4. Manual continuity controls

Pre-numbered controlled forms capture sample ID, source request, date/time, user, instrument/raw-data reference, result, unit, reason, verifier and later electronic reconciliation ID. Forms are issued/logged by QC and reconciled 100% after recovery.

## 5. DR activation and exit criteria

Activation requires credible inability to restore primary service within RTO or site leadership decision. Exit requires application health, identity, interfaces, backup, data reconciliation, sample retrieval and QA/business approval.

## 6. Exercise frequency

Annual technical DR exercise and annual business-continuity tabletop; additional exercise after material architecture change or failed recovery.

Manual continuity records are controlled GMP originals until reconciled into QCLabOne or linked to the electronic record. After restoration, the System Owner and BPO shall reconcile issued forms, electronic entries, interface messages and sample status before routine processing resumes. Any unreconciled item is managed as an incident/deviation with QA disposition.

| Continuity control | Exit evidence |
|---|---|
| Form issuance | Pre-numbered form log reconciled to returned forms |
| Manual result entry | Independent verification and reason for manual entry |
| Interface downtime | Backlog processed or dispositioned with source/target counts |
| Business decision hold | Affected samples/batches identified and released from hold only after review |
| DR return | Health checks, retrieval checks and QA/business approval retained |

## 7. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Input | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Output | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Output | SOP-IT-LIMS-002 | [QCLabOne 2.0 Operations, Maintenance, Backup, Incident, Change and Security SOP](069_Operations_Maintenance_Backup_Incident_Change_and_Security_SOP.md) |
| Output | QCL-2026-CUT-001 | [Cutover, Rollback and Contingency Plan](072_Cutover_Rollback_and_Contingency_Plan.md) |
| Output | QCL-2027-INC-014 | [Incident Record and Impact Assessment](085_Incident_Record_and_Impact_Assessment.md) |
| Output | QCL-2028-DRE-001 | [Business Continuity and Disaster Recovery Exercise Report](095_Business_Continuity_and_DR_Exercise_Report.md) |

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
