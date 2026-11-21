# Threat Model — Microsoft Security Operations Lab

## 1. Organization Profile

The lab simulates a fictional financial services organization.

### Environment

- 50 employees (simulated)
- 5 privileged administrators (simulated)
- Microsoft Entra ID identity management
- Windows endpoints
- Microsoft Azure infrastructure
- Centralized security monitoring

## 2. Security Objectives

The SOC must be able to:

1. Detect suspicious authentication patterns.
2. Identify unauthorized privileged role assignments.
3. Monitor suspicious endpoint activity.
4. Detect security-relevant cloud configuration changes.
5. Identify possible lateral movement.
6. Support investigation and incident response.

## 3. Critical Assets

| Asset | Security Concern | Priority |
|---|---|---|
| Entra ID identities | Account compromise | Critical |
| Privileged accounts | Unauthorized administrative access | Critical |
| Azure resources | Misconfiguration and compromise | High |
| Windows endpoints | Malicious execution | High |
| Security telemetry | Loss of detection visibility | Critical |

## 4. Threat Actors

### External Attacker

May attempt credential attacks against exposed authentication services.

### Compromised Employee Account

May be used to access resources or perform unauthorized actions.

### Malicious Insider

May abuse legitimate access privileges.

### Compromised Endpoint

May execute unauthorized scripts or initiate suspicious network connections.

## 5. Detection Scenarios

### DET-001: Password Spraying

**Threat:** An attacker attempts authentication against multiple accounts.

**Telemetry:** Entra ID sign-in logs, where available.

**Detection:** Multiple failed authentication attempts across distinct users within a defined time window.

**ATT&CK:** T1110.003

### DET-002: Suspicious PowerShell

**Threat:** PowerShell is used to execute suspicious commands.

**Telemetry:** Windows PowerShell operational logs and optional Sysmon events.

**Detection:** Suspicious script content, execution patterns, or related activity.

**ATT&CK:** T1059.001

### DET-003: Privileged Role Modification

**Threat:** An account receives unexpected administrative privileges.

**Telemetry:** Entra ID audit logs.

**Detection:** Security-relevant privileged role assignments.

**ATT&CK:** T1098

### DET-004: Azure Security Configuration Changes

**Threat:** An attacker modifies cloud security controls.

**Telemetry:** Azure Activity Logs and relevant resource diagnostic logs.

**Detection:** Changes to selected security-sensitive configurations.

**ATT&CK:** Mapping will depend on the specific change.

### DET-005: Suspicious Remote Authentication

**Threat:** An attacker attempts lateral movement using remote services.

**Telemetry:** Windows Security Events and relevant endpoint telemetry.

**Detection:** Suspicious remote logon patterns.

**ATT&CK:** T1021

## 6. Detection Validation

Each detection must include:

- Detection objective
- Required telemetry
- KQL query
- Test procedure
- Expected result
- Observed result
- False-positive analysis
- Limitations

## 7. Response Strategy

Alerts will be reviewed by an analyst.

Automation will initially be restricted to low-risk actions, such as notifications and incident enrichment.

High-impact actions will require explicit authorization.

## 8. Assumptions and Limitations

The organization and its employee counts are fictional.

Not all telemetry sources may be available because of licensing or cost constraints.

Synthetic test events will be clearly distinguished from real endpoint or Azure telemetry.

## 9. Status

Threat model drafted.

Detection rules and test scenarios have not yet been validated.
