"""Doc runtime hooks for reconstruction_entry."""

class DocRuntime:
    doc_key = "reconstruction_entry"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'accept', 'archive']
