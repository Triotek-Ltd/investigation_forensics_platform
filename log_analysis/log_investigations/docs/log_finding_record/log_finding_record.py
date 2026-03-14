"""Doc runtime hooks for log_finding_record."""

class DocRuntime:
    doc_key = "log_finding_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'accept', 'archive']
