---
document_number: QCL-2026-SCP-001
title: "QCLabOne 2.0 Project Scope Statement"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Project Initiation"
version: "1.0"
effective_or_record_date: "2026-02-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV Project Manager"
reviewed_by: "QC Business Process Owner"
approved_by: "Project Sponsor"
---

# QCLabOne 2.0 Project Scope Statement

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-SCP-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Project Initiation |
| Version | 1.0 |
| Effective/record date | 2026-02-20 |
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

This document fixes the system and project boundaries used by all downstream requirements, risk, design, testing and supplier records.

## 2. In-scope business processes

| Area | Included scope |
|---|---|
| QC Chemistry | Raw material, in-process, finished-product and stability sample testing; calculations; review and approval |
| Microbiology | Environmental monitoring, bioburden, microbial limits, incubation tracking and result approval |
| Stability | Protocol, pull scheduling, sample assignment, result review and trend reporting |
| QA | OOS/OOT case linkage, audit-trail oversight, release and validation approvals |
| IT | Identity, connectivity, interface gateway, monitoring, backup, restore, security and DR |

## 3. In-scope modules

Sample Management; Specification and Method Management; LES; Calculation Engine; Stability; Microbiology/EM; Reagent and Reference Standard Management; Reporting; Audit Trail; Electronic Signature; Role/Access Administration; Interface Monitoring; Archive Export.

## 4. In-scope interfaces and devices

| Boundary ID | Source → destination | Data/operation | Scope decision |
|---|---|---|---|
| IF-01 | SAP → QCLabOne | Material, batch, sample request | Interface and mapping in scope; SAP core validation out of scope |
| IF-02 | QCLabOne → SAP | Inspection status and approved disposition/result summary | Interface in scope |
| IF-03 | QCLabOne ↔ eQMS | Create OOS/OOT case; receive case ID/status | CAPA creation is not part of this interface |
| IF-04 | CDS/SDMS → QCLabOne | Approved numeric result, unit, sequence ID, method version, source link | CDS remains official source for chromatographic raw data |
| IF-05 | Balances/pH/TOC → QCLabOne | Measured value, unit, device ID, timestamp, status | 24 devices listed in the Interface Specification |
| IF-06 | Corporate Identity → QCLabOne | Authentication and group claims | Identity infrastructure qualification leveraged |
| IF-07 | QCLabOne → ArchiveVault | Closed record package and legacy archive | Archive qualification and retrieval in scope |

## 5. Data scope

- Migrate 86,742 Legacy LIMS sample records, 326,115 result records, 24,806 attachments and 1,984 active stability-pull records.
- Archive all pre-2018 Legacy LIMS data and associated audit trails/attachments in read-only form.
- Migrate active stability, reagent/reference-standard and EM schedule registers from approved spreadsheets.
- Paper worksheets are not bulk digitised; an indexed image set is created only for records identified in the approved archive list.

## 6. Out of scope

Analytical method validation; method transfer; core SAP/eQMS/CDS revalidation; replacement of laboratory instrument firmware; global multi-site rollout; mobile offline execution; product batch release decision in SAP; CAPA workflow design in eQMS.

Out-of-scope items are excluded because they are controlled by separate validated systems, separate GMP processes or future project charters. Each exclusion is valid only if the boundary control remains effective; for example, CDS raw data remains controlled in ChromLink, SAP final batch release remains controlled in SAP, and eQMS investigation records remain controlled in QualiTrack.

## 7. Assumptions and constraints

- Production is a dedicated vendor tenant in China East; no personal health data is stored.
- The site retains ownership of all GxP data and can obtain a complete export.
- Supplier standard product code is not modified; only approved interfaces and report templates are custom developed.
- Legacy LIMS remains read-only and backed up until retirement approval.
- Any proposed scope change requires change control and impact assessment.

## 8. Environment and responsibility boundaries

| Boundary | Included | Excluded or leveraged |
|---|---|---|
| Development/test tenant | Configuration build, supplier dry runs, interface trials and validation test execution | Production GMP record creation |
| Production tenant | Approved configuration, live records, operational monitoring and support | Unapproved configuration changes or uncontrolled test data |
| Corporate infrastructure | Identity, network, backup, monitoring and security controls supporting QCLabOne | Core corporate service revalidation unless impacted by this project |
| Supplier cloud operations | Hosting, platform maintenance, security notification and service availability | Site GxP acceptance and release decision |
| Legacy LIMS | Read-only access, migration, archive and retirement controls | New GMP result entry after QCLabOne go-live |

## 9. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CHA-001 | [QCLabOne 2.0 Project Charter](005_Project_Charter.md) |
| Output | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Output | QCL-2026-BPD-001 | [QCLabOne 2.0 Business Process Description](008_Business_Process_Description.md) |
| Output | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Output | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Output | QCL-2026-URS-001 | [User Requirements Specification](022_User_Requirements_Specification.md) |
| Output | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Output | QCL-2026-DMP-001 | [Data Migration Strategy and Plan](036_Data_Migration_Strategy_and_Plan.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV Project Manager | Completed |
| Reviewed by | QC Business Process Owner | Completed |
| Approved by | Project Sponsor | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-02-20 | Initial approved fictional case version. |
