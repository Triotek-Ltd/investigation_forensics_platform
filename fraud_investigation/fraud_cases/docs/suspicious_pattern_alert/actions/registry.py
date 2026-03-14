"""Action registry seed for suspicious_pattern_alert."""

from __future__ import annotations


DOC_ID = "suspicious_pattern_alert"
ALLOWED_ACTIONS = ['create', 'triage', 'link_case', 'dismiss', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['raised', 'triaged', 'linked_to_case', 'dismissed'], 'transitions_to': None}, 'triage': {'allowed_in_states': ['raised', 'triaged', 'linked_to_case', 'dismissed'], 'transitions_to': None}, 'link_case': {'allowed_in_states': ['raised', 'triaged', 'linked_to_case', 'dismissed'], 'transitions_to': None}, 'dismiss': {'allowed_in_states': ['raised', 'triaged', 'linked_to_case', 'dismissed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['raised', 'triaged', 'linked_to_case', 'dismissed'], 'transitions_to': 'archived'}}

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
