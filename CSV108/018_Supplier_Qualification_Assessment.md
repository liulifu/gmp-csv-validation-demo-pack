---
document_number: QCL-2026-SQA-001
title: "Supplier Qualification Assessment"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Supplier Management"
version: "1.0"
effective_or_record_date: "2026-04-30"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Supplier Quality Lead"
reviewed_by: "IT System Owner"
approved_by: "QA Validation Manager"
---

# Supplier Qualification Assessment

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-SQA-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Supplier Management |
| Version | 1.0 |
| Effective/record date | 2026-04-30 |
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

## 1. Supplier

**Supplier:** LabSphere Technologies Ltd.  
**Product/service:** LabSphere LIMS/LES 8.4.2 and managed private-cloud service  
**Assessment date:** 2026-04-22

## 2. Qualification assessment

| Domain | Evidence reviewed | Conclusion |
|---|---|---|
| Corporate/QMS governance | Documented quality manual, internal audit, CAPA and management review | Satisfactory |
| Software development lifecycle | Requirements, design, code review, automated/manual test, release and configuration management | Satisfactory |
| Validation documentation | Product description, release qualification, traceability and test summaries available | Satisfactory |
| Cloud operations | Dedicated tenant controls, monitoring, backup, DR and capacity management | Satisfactory |
| Information security | ISO 27001 certificate, annual penetration test, vulnerability and incident process | Satisfactory with agreement controls |
| Data ownership/export | Contract confirms customer ownership and complete export at termination | Satisfactory |
| Subcontractor control | Cloud infrastructure subcontractors listed and change-notified | Satisfactory |
| Support/change notification | 24×7 critical support; 90-day planned change notice proposed | Satisfactory |
| Business continuity | Annual DR test; application-layer evidence to be improved | Conditional—audited CAPA |
| Regulatory inspection support | Records and SME availability under quality agreement | Satisfactory |

## 3. Risk rating

The supplier is classified **Critical GxP Service Provider** because it hosts the application and database and can influence availability, configuration and security. Supplier failure could affect required records and QC operations.

## 4. Qualification decision

**Conditionally approved**, subject to:
1. closure or accepted plan for supplier audit findings;
2. signed quality/technical agreement;
3. customer approval for production remote access;
4. documented change/security incident notifications;
5. annual supplier performance review.

## 5. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-RFP-001 | [RFI, RFP and Product Selection Record](017_RFI_RFP_and_Product_Selection_Record.md) |
| Input | QCL-2026-CLA-001 | [System Classification and Criticality Assessment](010_System_Classification_and_Criticality_Assessment.md) |
| Input | QCL-2026-CYB-001 | [Cybersecurity and Privacy Impact Assessment](014_Cybersecurity_and_Privacy_Impact_Assessment.md) |
| Output | QCL-2026-SAR-001 | [Supplier Audit Report and CAPA](019_Supplier_Audit_Report_and_CAPA.md) |
| Output | QCL-2026-QTA-001 | [Quality/Technical Agreement and Service Level Agreement](020_Quality_Technical_Agreement_and_SLA.md) |
| Output | QCL-2026-SDL-001 | [Supplier Documentation Leveraging Assessment](021_Supplier_Documentation_Leveraging_Assessment.md) |
| Output | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Supplier Quality Lead | Completed |
| Reviewed by | IT System Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-30 | Initial approved fictional case version. |
