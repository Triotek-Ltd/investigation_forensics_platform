"""Action handler seed for forensic_ledger_review:complete."""

from __future__ import annotations


DOC_ID = "forensic_ledger_review"
ACTION_ID = "complete"
ACTION_RULE = {'allowed_in_states': ['opened', 'in_review', 'completed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['asset_trace_case', 'reconstruction_entry', 'journal_entry'], 'borrowed_fields': ['trace', 'account context from linked records'], 'inferred_roles': ['auditor', 'finance officer', 'case owner']}, 'actors': ['auditor', 'finance officer', 'case owner'], 'action_actors': {'create': ['auditor'], 'review': ['auditor'], 'archive': ['case owner']}}

def handle_complete(payload: dict, context: dict | None = None) -> dict:
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
