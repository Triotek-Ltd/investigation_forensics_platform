"""Integration-service seed for investigation_interview_record."""

from __future__ import annotations


DOC_ID = "investigation_interview_record"
INTEGRATION_RULES = {'external_refs': [], 'sync_rules': []}

class IntegrationService:
    def sync_rules(self) -> list:
        return INTEGRATION_RULES.get("sync_rules", [])

    def integration_profile(self) -> dict:
        return {'external_sync_enabled': True, 'tracks_external_refs': True}
