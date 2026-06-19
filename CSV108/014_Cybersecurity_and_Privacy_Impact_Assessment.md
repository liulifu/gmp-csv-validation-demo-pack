---
document_number: QCL-2026-CYB-001
title: "Cybersecurity and Privacy Impact Assessment"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Risk and Compliance"
version: "1.0"
effective_or_record_date: "2026-03-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "CSV/Quality Risk Lead"
reviewed_by: "System Owner"
approved_by: "QA Validation Manager"
---

# Cybersecurity and Privacy Impact Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-CYB-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Risk and Compliance |
| Version | 1.0 |
| Effective/record date | 2026-03-20 |
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

## 1. Scope

The assessment covers the vendor cloud tenant, interface gateway, identity federation, interfaces, remote support, backups and employee-identifying audit/signature data.

## 2. Data classification and privacy

The system stores GMP records and limited business-personal data: employee name, corporate ID, role, signature manifestation and work activity. It stores no patient, clinical-subject, biometric or special-category health data. Production data is hosted in China East; no routine cross-border transfer is designed. Supplier support outside the hosting region may access only approved masked/non-production data unless exceptional access is approved and logged.

## 3. Threat and control assessment

| Threat | Initial risk | Key controls | Residual risk |
|---|---|---|---|
| Unauthorised external access | High | Dedicated tenant, WAF, MFA for privileged access, deny-by-default firewall, monitored vendor access | Medium |
| Credential compromise | High | Corporate SSO, MFA, lockout, session timeout, security-event monitoring | Low |
| Excess privilege/SoD conflict | High | Approved RBAC matrix, privileged access review and recertification | Medium |
| Malware/ransomware on gateway | High | EDR, application allowlisting, restricted service accounts, patching and offline/immutable backups | Medium |
| Interface spoofing or tampering | High | Mutual TLS, certificate management, message schema/ID validation and reconciliation | Low |
| Cloud service vulnerability | High | Supplier vulnerability management, penetration testing summary, 24-hour critical-event notification | Medium |
| Data exfiltration | High | Encryption, export permission, DLP logging and supplier agreement | Medium |
| Backup compromise | High | Encrypted immutable copy, separated credentials and restore test | Low |
| Certificate expiry | Medium | Inventory and automated 60/30/7-day alerts; change record for renewal | Low |
| Privacy breach | Low | Only employee name/ID and work activity; no patient data; minimisation and role restriction | Low |

## 4. Security requirements

TLS 1.2 or higher; encryption at rest; corporate SSO; MFA for privileged/vendor access; 15-minute session lock; monthly critical patch assessment; annual penetration-test summary; daily vulnerability monitoring; event retention for at least two years or longer when linked to a GMP investigation; security incident notification within four hours for suspected GxP impact.

## 5. Privacy conclusion

The privacy impact is low after minimisation and access controls. Employee transparency is provided through the company privacy notice. Export of user activity is limited to legitimate quality, security and investigation purposes.

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-SCP-001 | [QCLabOne 2.0 Project Scope Statement](006_Project_Scope_Statement.md) |
| Input | QCL-2026-IUS-001 | [QCLabOne 2.0 Intended Use Statement](007_Intended_Use_Statement.md) |
| Input | QCL-2026-GXP-001 | [QCLabOne 2.0 GxP Impact Assessment](009_GxP_Impact_Assessment.md) |
| Input | QCL-2026-DIRA-001 | [Data Integrity Risk Assessment](012_Data_Integrity_Risk_Assessment.md) |
| Output | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Output | QCL-2026-IAD-001 | [Infrastructure and Architecture Design](026_Infrastructure_and_Architecture_Design.md) |
| Output | QCL-2026-RAC-001 | [Role and Access Control Matrix](031_Role_and_Access_Control_Matrix.md) |
| Output | QCL-2026-BCP-001 | [Business Continuity and Disaster Recovery Plan](035_Business_Continuity_and_Disaster_Recovery_Plan.md) |
| Output | QCL-2026-SEC-001 | [Security, Access and Segregation of Duties Test Report](053_Security_Access_and_Segregation_of_Duties_Test.md) |
| Output | QCL-2028-CVM-001 | [Cybersecurity Vulnerability and Monitoring Report](094_Cybersecurity_Vulnerability_and_Monitoring_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | CSV/Quality Risk Lead | Completed |
| Reviewed by | System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-20 | Initial approved fictional case version. |
