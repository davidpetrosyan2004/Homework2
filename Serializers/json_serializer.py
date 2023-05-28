import json
from BaseModel.BaseModel import BaseModel


class JSONSerializer:
    @staticmethod
    def to_json(obj):
        return json.dumps(BaseModel.to_dict(obj))

    @staticmethod
    def from_json(obj, obj_data):
        loads_data = json.loads(obj_data)
        return obj(**loads_data)


if __name__ == "__main__":
    from Homework2.Library.library import Library

    jsonserializer = JSONSerializer()

    library_1 = jsonserializer.from_json(
        Library, '{"library_name": "Polytechnic University of Armenia"}'
    )
    print(library_1.library_name)

    library_1_json = jsonserializer.to_json(library_1)
    print(library_1_json)
