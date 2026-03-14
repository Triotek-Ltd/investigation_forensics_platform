"""Doc runtime hooks for remediation_case."""

class DocRuntime:
    doc_key = "remediation_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'verify', 'close', 'archive']
