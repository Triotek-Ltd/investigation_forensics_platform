"""Action handler seed for fraud_case:investigate."""

from __future__ import annotations


DOC_ID = "fraud_case"
ACTION_ID = "investigate"
ACTION_RULE = {'allowed_in_states': ['opened', 'triaged', 'investigating', 'confirmed', 'dismissed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['transaction_trace_record', 'suspicious_pattern_alert', 'fraud_alert', 'chargeback_case'], 'borrowed_fields': ['source alert/transaction context from linked fraud/payment docs'], 'inferred_roles': ['auditor', 'finance officer', 'case owner']}, 'actors': ['auditor', 'finance officer', 'case owner'], 'action_actors': {'create': ['auditor'], 'assign': ['auditor'], 'confirm': ['finance officer'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_investigate(payload: dict, context: dict | None = None) -> dict:
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
