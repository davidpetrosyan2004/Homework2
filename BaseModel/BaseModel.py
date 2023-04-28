class BaseModel:
    @classmethod
    def to_dict(cls, obj):
        obj_dict = {}
        for key, value in vars(obj).items():
            obj_dict[key] = cls.__serialize(value)
        return obj_dict

    @classmethod
    def __serialize(cls, value):
        if isinstance(value, (int, float, str, bool)) or value is None:
            return value
        elif isinstance(value, (tuple, list, set)):
            new_value = []
            for element in value:
                new_value.append(cls.__serialize(element))
            return new_value
        elif isinstance(value, dict):
            new_dict = {}
            for key, element in value:
                new_dict[key] = cls.__serialize(element)
            return new_dict


