"""Doc runtime hooks for investigation_case."""

class DocRuntime:
    doc_key = "investigation_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'investigate', 'substantiate', 'dismiss', 'close', 'archive']
