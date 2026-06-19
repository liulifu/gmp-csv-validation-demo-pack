---
document_number: QCL-2026-BLD-001
title: "Installation, Build and Configuration Record"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Build and Installation"
version: "1.0"
effective_or_record_date: "2026-12-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "IT System Owner"
reviewed_by: "Vendor Technical Lead"
approved_by: "QA CSV Lead"
---

# Installation, Build and Configuration Record

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-BLD-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Build and Installation |
| Version | 1.0 |
| Effective/record date | 2026-12-20 |
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

This record documents the controlled installation, build, deployment and configuration of the validated environments.

## 2. Build execution record

| Step | Activity | Date | Actual result/evidence | Status |
|---|---|---|---|---|
| BLD-001 | Supplier production tenant provisioned | 2026-11-10 | Tenant QCL-PROD-CN-E01; dedicated; production label verified | Accepted |
| BLD-002 | Validation tenant provisioned | 2026-11-10 | Tenant QCL-VAL-CN-E01 | Accepted |
| BLD-003 | Application release installed | 2026-12-05 | LabSphere LIMS/LES 8.4.2 + HF1; package SHA-256 8f3d...a91c | Accepted |
| BLD-004 | Database service provisioned | 2026-11-12 | PostgreSQL 15.5 managed cluster; encryption enabled | Accepted |
| BLD-005 | QCL-IGW-01 built | 2026-11-18 | Windows Server 2022 build 20348; Gateway 3.6.1 | Accepted |
| BLD-006 | Firewall/TLS routes enabled | 2026-11-25 | Rules FW-QCL-001–014; certificates valid to 2027-11-30 | Accepted |
| BLD-007 | SAML federation configured | 2026-11-28 | Entity ID qclabone-prod; signed assertions; group mapping | Accepted |
| BLD-008 | Interfaces deployed | 2026-12-12 | SAP 2.1.0; eQMS 1.4.1; CDS 2.3.0; instrument adapter 3.6.1 | Accepted |
| BLD-009 | Site configuration package imported | 2026-12-16 | QCL-CONFIG-1.0; checksum 51aa...b2e7 | Accepted |
| BLD-010 | Monitoring/backup configured | 2026-12-18 | Dashboards, alerts, PITR and nightly jobs enabled | Accepted |
| BLD-011 | Initial master data loaded | 2026-12-19 | Controlled load set MD-LOAD-01 | Accepted with reconciliation |
| BLD-012 | Build review completed | 2026-12-20 | No unauthorised component detected | Approved |

## 3. Build controls

Deployment used supplier-signed packages and company-approved configuration. Checksums were verified before import. Production administrative access was limited to approved accounts. No production data was introduced during build.

## 4. Exceptions

No open build exception remains. The barcode driver issue detected at SAT is recorded as DEF-006 and closed before IQ completion.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-CS-001 | [Configuration Specification](025_Configuration_Specification.md) |
| Input | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Input | QCL-2026-ICS-001 | [Interface Control Specification](027_Interface_Control_Specification.md) |
| Input | QCL-2026-MDS-001 | [Master Data Specification](030_Master_Data_Specification.md) |
| Input | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-SDP-001 | [Software Development and Source Control Plan](042_Software_Development_and_Source_Control_Plan.md) |
| Output | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Output | QCL-2026-SAT-001 | [Site Acceptance Test Protocol and Report](045_Site_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-PBL-001 | [Production Baseline and Approved Configuration Record](077_Production_Baseline_and_Approved_Configuration_Record.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | IT System Owner | Completed |
| Reviewed by | Vendor Technical Lead | Completed |
| Approved by | QA CSV Lead | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-12-20 | Initial approved fictional case version. |
