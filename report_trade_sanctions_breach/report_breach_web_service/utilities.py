# utility methods
# json validators, anything which doesn't necessarily fit in the class based views or Forms
import json
import os

from jsonschema import ValidationError
from jsonschema import validate


def json_is_valid(path_to_schema, json_to_validate):
    file_dir = os.path.dirname(__file__)
    with open(os.path.join(file_dir, path_to_schema), "r") as json_reader:
        json_schema = json.load(json_reader)
        try:
            validate(json_to_validate, json_schema)
            return True
        except ValidationError as err:
            raise err
