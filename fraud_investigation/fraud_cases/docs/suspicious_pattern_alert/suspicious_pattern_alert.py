"""Doc runtime hooks for suspicious_pattern_alert."""

class DocRuntime:
    doc_key = "suspicious_pattern_alert"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'triage', 'link_case', 'dismiss', 'archive']
