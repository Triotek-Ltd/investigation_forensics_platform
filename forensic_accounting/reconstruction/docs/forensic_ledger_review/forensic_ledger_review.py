"""Doc runtime hooks for forensic_ledger_review."""

class DocRuntime:
    doc_key = "forensic_ledger_review"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'complete', 'archive']
