"""Doc runtime hooks for log_search_case."""

class DocRuntime:
    doc_key = "log_search_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'search', 'review', 'complete', 'escalate', 'archive']
