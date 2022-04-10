import helpers.schema as schema
from cerberus import Validator


class SchemaValidator:

    def __init__(self, event: dict, schema_dict: dict):

        self.event = event
        self.schema_dict = schema_dict
        self.v = Validator()

    @property
    def validation_output(self) -> dict:

        schema_combination = f'{self.schema_dict.get("source")}-{self.schema_dict.get("artifact")}-{self.schema_dict.get("v_schema")}'
        try:
            _schema = getattr(schema, schema_combination).SCHEMA
            status = self.v.validate(self.event, _schema)
            error = self.v.errors
        except:
            status = False
            error = f"Schema {schema_combination} does not exist"

        return {'status': status, 'error': error}
