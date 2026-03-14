"""Doc runtime hooks for device_image_record."""

class DocRuntime:
    doc_key = "device_image_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'mount', 'archive']
