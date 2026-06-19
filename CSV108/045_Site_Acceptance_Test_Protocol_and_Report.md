---
document_number: QCL-2026-SAT-001
title: "Site Acceptance Test Protocol and Report"
project_code: QCL-2026
project: "QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project"
system: "QCLabOne 2.0 LIMS/LES"
lifecycle_phase: "Verification"
version: "1.0"
effective_or_record_date: "2027-02-20"
case_status: "Approved in fictional case"
use_status: "Fictional training case — requires site-specific QA approval before operational use"
prepared_by: "Test Lead"
reviewed_by: "Business Process Owner"
approved_by: "QA Validation Manager"
---

# Site Acceptance Test Protocol and Report

> **Use notice:** This Markdown file is a fully populated fictional CSV training case. It is not an executed GMP record and does not replace company procedures, approved signatures, supplier evidence, or site-specific risk decisions.

## Document control

| Field | Value |
|---|---|
| Document number | QCL-2026-SAT-001 |
| Company | NovaSterile Pharma Co., Ltd. |
| Site | Suzhou Sterile Products Manufacturing Site |
| Project | QCLabOne 2.0 QC Laboratory Digital Platform Replacement Project |
| System | QCLabOne 2.0 LIMS/LES |
| Lifecycle phase | Verification |
| Version | 1.0 |
| Effective/record date | 2027-02-20 |
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

## 1. Objective

SAT confirmed that the approved solution operated correctly with site networks, identity, interfaces, instruments, peripherals, monitoring and archive services.

## 2. Execution

Executed 2027-02-13 to 2027-02-18 in the site validation environment using the approved deployment package.

## 3. Results

| Test | Area | Acceptance | Result |
|---|---|---|---|
| SAT-001 | Production/validation URL and network path | Accessible only from approved networks | Pass |
| SAT-002 | Corporate SSO and role claims | Correct identity/role mapping | Pass |
| SAT-003 | SAP connectivity and sample message | End-to-end acknowledgement | Pass |
| SAT-004 | eQMS/CDS connectivity | Secure connection and sandbox transaction | Pass |
| SAT-005 | 24 instrument/device endpoints | Correct device identity and normalized data | Pass |
| SAT-006 | Barcode printers/scanners | Readable, correctly associated barcode | Pass after DEF-006 |
| SAT-007 | Monitoring, logs and alerts | Alerts reach approved support groups | Pass |
| SAT-008 | Backup and gateway configuration export | Successful and monitored | Pass |
| SAT-009 | Vendor remote support workflow | Disabled by default; approved session logged | Pass |
| SAT-010 | ArchiveVault test package | Transferred, checksum and retrieved | Pass |

## 4. Deviation/defect

One printer had an obsolete driver (DEF-006). The approved driver was installed and the affected print/scan test repeated successfully.

## 5. Conclusion

The site environment met SAT exit criteria and was released to formal qualification/validation testing.

SAT release confirms that the installed site environment is stable enough for formal testing. It does not approve production use or close validation requirements. Any difference between FAT build, installed build and SAT-accepted build shall be reflected in the configuration item register and test impact assessment.

| SAT readiness area | Acceptance expectation |
|---|---|
| Environment | Correct tenant/server, network, monitoring and backup inclusion |
| Device/interface connectivity | Site devices and endpoints communicate using approved settings |
| Configuration import | Baseline package imported and smoke tested |
| Evidence control | Screenshots/logs identify environment, date/time and tester |
| Open issue | Defect/deviation has severity, owner, due date and retest plan |

## 6. Related documents

| Relationship | Document ID | Document |
|---|---|---|
| Input | QCL-2026-BLD-001 | [Installation, Build and Configuration Record](040_Installation_Build_and_Configuration_Record.md) |
| Input | QCL-2026-CIR-001 | [Configuration Item and Version Register](041_Configuration_Item_and_Version_Register.md) |
| Input | QCL-2026-FAT-001 | [Factory Acceptance Test Protocol and Report](044_Factory_Acceptance_Test_Protocol_and_Report.md) |
| Output | QCL-2026-VTP-001 | [Validation Test Plan and Strategy](046_Validation_Test_Plan_and_Strategy.md) |
| Output | QCL-2026-IQ-001 | [Installation Qualification Protocol and Report](048_Installation_Qualification_Protocol_and_Report.md) |
| Output | QCL-2026-IFT-001 | [Interface Test Protocol and Report](051_Interface_Test_Protocol_and_Report.md) |
| Output | QCL-2026-DEF-001 | [Defect Log and Resolution Report](060_Defect_Log_and_Resolution_Report.md) |

## Approval record

| Approval step | Role | Case outcome |
|---|---|---|
| Prepared by | Test Lead | Completed |
| Reviewed by | Business Process Owner | Completed |
| Approved by | QA Validation Manager | Approved in fictional case |

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2027-02-20 | Initial approved fictional case version. |
