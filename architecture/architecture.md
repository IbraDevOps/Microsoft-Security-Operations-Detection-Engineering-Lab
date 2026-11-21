# Security Monitoring Architecture

## 1. Business Context

The lab models a fictional financial services organization
with 50 employees and five privileged administrators.

The organization requires centralized monitoring of
identity activity, Windows endpoints, and Azure resources.

These are scenario assumptions, not deployed resource counts.

## 2. Security Objectives

- Detect suspicious authentication activity.
- Monitor privileged identity changes.
- Identify suspicious endpoint execution.
- Monitor security-relevant Azure configuration changes.
- Support incident triage and investigation.
- Automate low-risk response tasks.

## 3. Logical Architecture

### Telemetry Sources

1. Microsoft Entra ID
   - Sign-in logs, subject to licensing and availability.
   - Audit logs.

2. Windows Endpoint
   - Windows Security Events.
   - PowerShell operational events.
   - Sysmon events where configured.

3. Microsoft Azure
   - Azure Activity Logs.
   - Selected resource diagnostic logs.

### Collection Layer

Azure Monitor Agent and supported Microsoft Sentinel
data connectors will collect available telemetry.

Connector requirements and licensing will be verified
before deployment.

### Storage and Analytics

Azure Log Analytics will provide centralized log
storage and KQL query capabilities.

### Detection Layer

Microsoft Sentinel analytics rules will evaluate
supported telemetry and generate security alerts.

### Response Layer

Azure Logic Apps will support controlled automation,
beginning with notifications and analyst approval.

## 4. Security Design Principles

- Least privilege.
- Separation of administrative duties.
- MFA for privileged access where supported.
- Centralized logging.
- Minimal collection of sensitive data.
- Explicit authorization for simulated attacks.
- Human approval before high-impact response actions.
- Cost monitoring and resource cleanup.

## 5. Deployment Strategy

Stage 1: Architecture and offline KQL practice.

Stage 2: Minimal Azure and Entra ID configuration.

Stage 3: Log Analytics and Sentinel onboarding.

Stage 4: Detection validation using permitted telemetry.

Stage 5: Incident-response automation.

## 6. Cost Controls

Before deployment:

- Confirm subscription and available credits.
- Review Azure Monitor and Sentinel pricing.
- Set budget alerts.
- Limit data ingestion and retention.
- Avoid unnecessary virtual machines.
- Define resource cleanup procedures.

Azure budget alerts do not automatically prevent
additional charges.

## 7. Acceptance Criteria

The project is complete when its detection scenarios,
investigations, automation, and supporting documentation
have been tested and reviewed.

## 8. Current Status

Architecture design in progress.
No Azure resources have been deployed yet.
