---
document_number: QCL-2026-IAD-001
title: "Infrastructure and Architecture Design"
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

# Infrastructure and Architecture Design

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-IAD-001 |
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

This document defines qualified infrastructure and network dependencies for the application, gateway, identity, backup and archive.

## 2. Physical and service architecture

| Item | Approved design |
|---|---|
| Cloud tenant | Dedicated QCLabOne tenant in China East; production and non-production separated |
| Application service | Redundant supplier-managed nodes behind web application firewall/load balancer |
| Database | Managed PostgreSQL 15, encrypted, multi-zone replication and PITR |
| Attachment storage | Encrypted object store with versioning and checksum |
| Gateway | QCL-IGW-01; Windows Server 2022; 8 vCPU; 32 GB RAM; 500 GB encrypted disk |
| Network | Site DMZ-to-cloud TLS route; deny-by-default firewall; no inbound Internet access to gateway |
| Identity | Corporate AD FS 2022/SAML; corporate NTP |
| Monitoring | Availability, CPU/memory/disk, interface queues, certificates, backup, security and time drift |
| DR | Supplier standby region plus site DR copy for gateway configuration |

## 3. Network zones and ports

| Path | Protocol/port | Direction | Purpose |
|---|---|---|---|
| User network → cloud application | HTTPS 443 | Outbound | User access |
| Gateway → cloud API | mTLS HTTPS 443 | Outbound | Interfaces |
| Gateway ↔ SAP/eQMS/CDS | HTTPS 443 / approved message queue | Bidirectional | Enterprise interfaces |
| Instruments → gateway | Approved serial/TCP ports | Inbound from laboratory VLAN | Device capture |
| Gateway → NTP/DNS/identity/logging | Approved enterprise services | Outbound | Infrastructure control |
| Vendor remote support | Approved bastion over MFA | Time-limited | Diagnostic support only |

## 4. Qualification and hardening

Server build follows approved CIS-aligned baseline. EDR, patching, logging, backup and least-privilege service accounts are mandatory. Unsupported software, local email, web browsing and removable-media use are prohibited.

## 5. Capacity

Initial design supports 200 concurrent users, 10,000 interface messages/hour, 5 TB attachment growth over five years and 30% headroom. Alert thresholds are 70% warning and 85% critical for capacity resources.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Input | QCL-2026-DS-001 | [System Design Specification](024_System_Design_Specification.md) |
| Input | QCL-2026-BRS-001 | [Backup and Restore Specification](034_Backup_and_Restore_Specification.md) |
| Input | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Output | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Output | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-BRT-001 | [Backup and Restore Test Report](056_Backup_and_Restore_Test_Report.md) |
| Output | QCL-2026-PLC-001 | [Performance, Load and Capacity Test Report](057_Performance_Load_and_Capacity_Test_Report.md) |
| Output | QCL-2026-DRT-001 | [Failover and Disaster Recovery Test Report](058_Failover_and_Disaster_Recovery_Test_Report.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |

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
