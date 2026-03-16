"""Action handler seed for evidence_item:store."""

from __future__ import annotations


DOC_ID = "evidence_item"
ACTION_ID = "store"
ACTION_RULE = {'allowed_in_states': ['collected', 'stored', 'examined', 'transferred'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['chain_of_custody_event', 'forensic_examination', 'device_image_record'], 'borrowed_fields': ['source-system or device context from integration/platform docs'], 'inferred_roles': ['auditor']}, 'actors': ['auditor'], 'action_actors': {'create': ['auditor'], 'archive': ['auditor']}}

def handle_store(payload: dict, context: dict | None = None) -> dict:
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
