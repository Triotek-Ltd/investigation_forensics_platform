"""Doc runtime hooks for evidence_item."""

class DocRuntime:
    doc_key = "evidence_item"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'collect', 'store', 'transfer', 'archive']
