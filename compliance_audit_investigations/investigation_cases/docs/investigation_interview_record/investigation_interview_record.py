"""Doc runtime hooks for investigation_interview_record."""

class DocRuntime:
    doc_key = "investigation_interview_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'finalize', 'archive']
