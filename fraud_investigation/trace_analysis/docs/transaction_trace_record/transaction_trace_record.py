"""Doc runtime hooks for transaction_trace_record."""

class DocRuntime:
    doc_key = "transaction_trace_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
