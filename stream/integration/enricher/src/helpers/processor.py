class Processor:

    def __init__(self, event: dict):

        self.event = event

    @staticmethod
    def process_event(event: dict) -> dict:

        processed_event = event

        return processed_event

    @property
    def processed_event(self) -> dict:

        return self.process_event(self.event)
