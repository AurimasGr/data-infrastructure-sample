class Processor:

    def __init__(self, event: dict, top_level_fields: dict):

        self.event = event
        self.top_level_fields = top_level_fields

    @staticmethod
    def process_event(event: dict, top_level_fields: dict) -> dict:

        def _add_top_level_fields(event: dict, top_level_fields: dict) -> dict:

            changed_event = top_level_fields
            changed_event['data'] = event

            return changed_event

        processed_event = event

        return _add_top_level_fields(processed_event, top_level_fields)

    @property
    def processed_event(self) -> dict:

        return self.process_event(self.event, self.top_level_fields)
