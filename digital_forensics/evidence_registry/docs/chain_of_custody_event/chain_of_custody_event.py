"""Doc runtime hooks for chain_of_custody_event."""

class DocRuntime:
    doc_key = "chain_of_custody_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
