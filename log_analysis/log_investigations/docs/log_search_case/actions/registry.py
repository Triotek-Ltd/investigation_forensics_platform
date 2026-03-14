"""Action registry seed for log_search_case."""

from __future__ import annotations


DOC_ID = "log_search_case"
ALLOWED_ACTIONS = ['create', 'assign', 'search', 'review', 'complete', 'escalate', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'completed', 'escalated'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'completed', 'escalated'], 'transitions_to': 'in_progress'}, 'search': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'completed', 'escalated'], 'transitions_to': None}, 'review': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'completed', 'escalated'], 'transitions_to': None}, 'complete': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'completed', 'escalated'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'completed', 'escalated'], 'transitions_to': 'escalated'}, 'archive': {'allowed_in_states': ['opened', 'assigned', 'in_progress', 'completed', 'escalated'], 'transitions_to': 'archived'}}

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
