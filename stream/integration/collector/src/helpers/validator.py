import helpers.schema as schema
from cerberus import Validator


class SchemaValidator:

    def __init__(self, event: dict):

        self.event = event
        self.v = Validator()

    @property
    def validation_output(self) -> dict:

        return {'status': self.v.validate(self.event, getattr(schema, 'payload').SCHEMA), 'error': self.v.errors}
