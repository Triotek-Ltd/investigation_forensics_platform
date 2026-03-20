"""Action handler seed for chain_of_custody_event:review."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "chain_of_custody_event"
ACTION_ID = "review"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['evidence_item', 'forensic_examination'], 'borrowed_fields': ['evidence identity from evidence_item'], 'inferred_roles': ['auditor']}, 'actors': ['auditor'], 'action_actors': {'record': ['auditor'], 'review': ['auditor'], 'archive': ['auditor']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['active'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_review(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "action_contract": ACTION_CONTRACT,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
