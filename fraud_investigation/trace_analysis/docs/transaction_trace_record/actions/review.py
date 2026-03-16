"""Action handler seed for transaction_trace_record:review."""

from __future__ import annotations


DOC_ID = "transaction_trace_record"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['fraud_case', 'payment_log_entry', 'ledger_posting', 'inventory_movement'], 'borrowed_fields': ['source transaction context from linked records'], 'inferred_roles': ['auditor', 'finance officer', 'operations coordinator', 'case owner']}, 'actors': ['auditor', 'finance officer', 'operations coordinator', 'case owner'], 'action_actors': {'record': ['auditor'], 'review': ['auditor'], 'archive': ['case owner']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
