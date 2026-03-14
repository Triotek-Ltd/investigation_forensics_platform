"""Action registry seed for evidence_item."""

from __future__ import annotations


DOC_ID = "evidence_item"
ALLOWED_ACTIONS = ['create', 'collect', 'store', 'transfer', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['collected', 'stored', 'examined', 'transferred'], 'transitions_to': None}, 'collect': {'allowed_in_states': ['collected', 'stored', 'examined', 'transferred'], 'transitions_to': None}, 'store': {'allowed_in_states': ['collected', 'stored', 'examined', 'transferred'], 'transitions_to': None}, 'transfer': {'allowed_in_states': ['collected', 'stored', 'examined', 'transferred'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['collected', 'stored', 'examined', 'transferred'], 'transitions_to': 'archived'}}

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
