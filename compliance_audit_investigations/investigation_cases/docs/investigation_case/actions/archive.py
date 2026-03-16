"""Action handler seed for investigation_case:archive."""

from __future__ import annotations


DOC_ID = "investigation_case"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['opened', 'assigned', 'investigating', 'substantiated', 'unsubstantiated'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['investigation_interview_record', 'investigation_report', 'remediation_case', 'audit_engagement'], 'borrowed_fields': ['source allegation or audit context from linked records'], 'inferred_roles': ['auditor', 'compliance officer', 'case owner']}, 'actors': ['auditor', 'compliance officer', 'case owner'], 'action_actors': {'create': ['auditor'], 'assign': ['auditor'], 'close': ['case owner'], 'archive': ['case owner']}}

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
