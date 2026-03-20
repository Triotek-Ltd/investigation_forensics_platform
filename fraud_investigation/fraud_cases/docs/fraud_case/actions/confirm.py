"""Action handler seed for fraud_case:confirm."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "fraud_case"
ACTION_ID = "confirm"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['opened', 'triaged', 'investigating', 'confirmed', 'dismissed'], 'transitions_to': 'confirmed'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['transaction_trace_record', 'suspicious_pattern_alert', 'fraud_alert', 'chargeback_case'], 'borrowed_fields': ['source alert/transaction context from linked fraud/payment docs'], 'inferred_roles': ['auditor', 'finance officer', 'case owner']}, 'actors': ['auditor', 'finance officer', 'case owner'], 'action_actors': {'create': ['auditor'], 'assign': ['auditor'], 'confirm': ['finance officer'], 'close': ['case owner'], 'archive': ['case owner']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['opened', 'triaged', 'investigating', 'confirmed', 'dismissed'], 'transitions_to': 'confirmed'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_confirm(payload: dict, context: dict | None = None) -> dict:
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
