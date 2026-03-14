"""Doc runtime hooks for asset_trace_case."""

class DocRuntime:
    doc_key = "asset_trace_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'trace', 'review', 'close', 'archive']
