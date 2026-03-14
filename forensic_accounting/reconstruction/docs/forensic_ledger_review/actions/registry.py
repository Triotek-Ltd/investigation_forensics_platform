"""Action registry seed for forensic_ledger_review."""

from __future__ import annotations


DOC_ID = "forensic_ledger_review"
ALLOWED_ACTIONS = ['create', 'review', 'complete', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'in_review', 'completed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['opened', 'in_review', 'completed'], 'transitions_to': 'in_review'}, 'complete': {'allowed_in_states': ['opened', 'in_review', 'completed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['opened', 'in_review', 'completed'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
