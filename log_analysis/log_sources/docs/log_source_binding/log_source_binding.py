"""Doc runtime hooks for log_source_binding."""

class DocRuntime:
    doc_key = "log_source_binding"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
