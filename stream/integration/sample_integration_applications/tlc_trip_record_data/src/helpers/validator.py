import helpers.schema as schema
from pydantic import ValidationError


class SchemaValidator:

    def __init__(self, event: dict, schema_dict: dict):

        self.event = event
        self.schema_dict = schema_dict

    @property
    def validation_output(self) -> dict:

        schema_combination = f'{self.schema_dict.get("source")}-{self.schema_dict.get("artifact")}-{self.schema_dict.get("v_schema")}'
        try:
            data = getattr(schema, schema_combination).Schema(**self.event)
            status = True
            error = None
        except ValidationError as e:
            data = None
            status = False
            error = f"Schema {schema_combination} does not exist"

        return {'status': status, 'error': error, 'data': data}
