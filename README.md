# Microsoft Security Operations & Detection Engineering Lab

## Project Overview

This project demonstrates the design and implementation of a Microsoft-based Security Operations Center (SOC) monitoring environment.

The lab simulates a fictional financial services organization operating Microsoft Azure infrastructure, Microsoft Entra ID, and Windows endpoints.

The objective is to build practical capabilities in:

- Cloud security monitoring
- Security Information and Event Management (SIEM)
- Detection engineering
- Incident investigation and response
- Security automation (SOAR)
- Kusto Query Language (KQL)

**Project status:** Phase 1 — Architecture and Threat Modeling.

## High-Level Architecture

```text
                  ENTERPRISE ENVIRONMENT
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
       Entra ID       Windows VM       Azure Resources
          |                |                |
          +----------------+----------------+
                           |
                           v
                  DATA COLLECTION
                           |
                           v
                    LOG ANALYTICS
                           |
                           v
                  MICROSOFT SENTINEL
                           |
                    KQL DETECTIONS
                           |
                           v
                    SOC INVESTIGATION
                           |
                           v
                    RESPONSE AUTOMATION
                      Logic Apps
                           |
                           v
                    Analyst Approval
```

## Detection Engineering Scenarios

| ID | Detection | MITRE ATT&CK | Status |
|---|---|---|---|
| DET-001 | Password spraying | T1110.003 | Planned |
| DET-002 | Suspicious PowerShell | T1059.001 | Planned |
| DET-003 | Privileged role modification | T1098 | Planned |
| DET-004 | Azure security configuration changes | Scenario-dependent | Planned |
| DET-005 | Suspicious remote authentication | T1021 | Planned |

## Technology Stack

- Microsoft Azure
- Microsoft Entra ID
- Microsoft Sentinel
- Azure Monitor
- Log Analytics
- Kusto Query Language (KQL)
- Windows Security Events
- Azure Logic Apps
- Python

## Project Roadmap

| Phase | Description | Status |
|---|---|---|
| 1 | Architecture and Threat Modeling | In Progress |
| 2 | Azure and Entra ID Foundation | Planned |
| 3 | Microsoft Sentinel and Log Ingestion | Planned |
| 4 | Detection Engineering and Validation | Planned |
| 5 | Incident Response and SOAR | Planned |
| 6 | Documentation and Interview Preparation | Planned |

## Project Deliverables

1. Security monitoring architecture and threat model.
2. Documented Azure and Entra ID configurations.
3. Five validated detection scenarios.
4. Three incident investigation reports.
5. One automated response workflow.
6. Final technical report and lessons learned.

## Repository Structure

- `architecture/` — Architecture, security requirements, threat model.
- `infrastructure/` — Azure and Entra ID configuration.
- `detections/` — KQL detection queries.
- `simulations/` — Controlled attack simulations and sample logs.
- `investigations/` — Incident investigation reports.
- `automation/` — Security response playbooks.
- `docs/` — Technical documentation and lessons learned.
- `screenshots/` — Supporting evidence.

## Scope and Safety

All security testing will be performed in authorized lab environments.

The project will distinguish synthetic events from live telemetry. No production credentials, secrets, or sensitive customer data will be committed.

## Author

**Ibrahim Sheikh**

Security Engineering | Detection Engineering | Cloud Security
