"""Doc runtime hooks for fraud_case."""

class DocRuntime:
    doc_key = "fraud_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'triage', 'assign', 'investigate', 'confirm', 'dismiss', 'close', 'archive']
