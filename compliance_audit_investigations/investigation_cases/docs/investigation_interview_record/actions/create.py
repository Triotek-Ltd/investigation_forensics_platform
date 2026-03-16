"""Action handler seed for investigation_interview_record:create."""

from __future__ import annotations


DOC_ID = "investigation_interview_record"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'accepted'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['investigation_case', 'investigation_report'], 'borrowed_fields': ['case context from investigation_case'], 'inferred_roles': ['auditor', 'compliance officer', 'case owner']}, 'actors': ['auditor', 'compliance officer', 'case owner'], 'action_actors': {'create': ['auditor'], 'review': ['auditor'], 'archive': ['case owner']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
