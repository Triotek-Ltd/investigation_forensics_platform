"""Action registry seed for investigation_report."""

from __future__ import annotations


DOC_ID = "investigation_report"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'issue', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'issued'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'issued'], 'transitions_to': 'reviewed'}, 'approve': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'issued'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': 'issued'}, 'archive': {'allowed_in_states': ['draft', 'reviewed', 'approved', 'issued'], 'transitions_to': 'archived'}}

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
