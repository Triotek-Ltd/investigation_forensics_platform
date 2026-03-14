"""Doc runtime hooks for investigation_report."""

class DocRuntime:
    doc_key = "investigation_report"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'issue', 'archive']
