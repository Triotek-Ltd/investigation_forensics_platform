"""Action handler seed for suspicious_pattern_alert:triage."""

from __future__ import annotations


DOC_ID = "suspicious_pattern_alert"
ACTION_ID = "triage"
ACTION_RULE = {'allowed_in_states': ['raised', 'triaged', 'linked_to_case', 'dismissed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['fraud_case', 'anomaly_alert', 'fraud_alert'], 'borrowed_fields': ['source signal or transaction context from linked alert records'], 'inferred_roles': ['auditor', 'case owner']}, 'actors': ['auditor', 'case owner'], 'action_actors': {'create': ['auditor'], 'archive': ['case owner']}}

def handle_triage(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
