"""Action handler seed for reconstruction_entry:archive."""

from __future__ import annotations


DOC_ID = "reconstruction_entry"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'accepted'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['asset_trace_case', 'forensic_ledger_review', 'ledger_posting'], 'borrowed_fields': ['trace context from asset_trace_case', 'account refs from ledger_posting'], 'inferred_roles': ['auditor', 'finance officer', 'case owner']}, 'actors': ['auditor', 'finance officer', 'case owner'], 'action_actors': {'record': ['auditor'], 'review': ['auditor'], 'archive': ['case owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
