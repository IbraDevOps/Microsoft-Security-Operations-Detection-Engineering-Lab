# Security Requirements

## 1. Purpose

Define the functional and security requirements for the
Microsoft Security Operations & Detection Engineering Lab.

## 2. Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-001 | Collect supported Entra ID security logs | High |
| FR-002 | Collect Windows endpoint security events | High |
| FR-003 | Collect Azure Activity Logs | High |
| FR-004 | Query telemetry using KQL | Critical |
| FR-005 | Develop five security detection scenarios | Critical |
| FR-006 | Generate and investigate security alerts | High |
| FR-007 | Implement a controlled response workflow | Medium |
| FR-008 | Document three incident investigations | High |

## 3. Security Requirements

| ID | Requirement | Priority |
|---|---|---|
| SR-001 | Enforce least-privilege access | Critical |
| SR-002 | Use MFA for privileged access where available | Critical |
| SR-003 | Protect security monitoring configurations | High |
| SR-004 | Prevent secrets from entering GitHub | Critical |
| SR-005 | Restrict simulated attacks to authorized assets | Critical |
| SR-006 | Require approval for high-impact response actions | High |
| SR-007 | Document detection limitations | High |

## 4. Operational Requirements

- Document deployment procedures.
- Define log ingestion and retention settings.
- Monitor Azure resource costs.
- Define a resource cleanup procedure.
- Maintain version-controlled detection rules.
- Preserve evidence of testing.

## 5. Acceptance Criteria

The lab is considered complete when:

1. Five detection scenarios have been tested.
2. Three investigations have been documented.
3. One response automation workflow has been validated.
4. The architecture and security controls are documented.
5. The repository contains reproducible instructions.
6. All Azure resources and costs are accounted for.

## 6. Current Status

Requirements defined.

Implementation and validation are pending.
