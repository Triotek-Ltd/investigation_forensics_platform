"""Action handler seed for log_finding_record:record."""

from __future__ import annotations


DOC_ID = "log_finding_record"
ACTION_ID = "record"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'accepted'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['log_search_case', 'fraud_case', 'investigation_case'], 'borrowed_fields': ['search context from log_search_case'], 'inferred_roles': ['auditor', 'case owner']}, 'actors': ['auditor', 'case owner'], 'action_actors': {'record': ['auditor'], 'review': ['auditor'], 'archive': ['case owner']}}

def handle_record(payload: dict, context: dict | None = None) -> dict:
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
