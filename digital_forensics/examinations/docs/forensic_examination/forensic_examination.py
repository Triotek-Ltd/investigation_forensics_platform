"""Doc runtime hooks for forensic_examination."""

class DocRuntime:
    doc_key = "forensic_examination"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'examine', 'complete', 'close', 'archive']
