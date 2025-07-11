
class Validation:
    def __init__(self, **kwargs):
        self.member_map = kwargs
        self.validator_map = {
            "string": self.string_validator,
            "int": self.int_validator,
            "float": self.float_validator,
            "complex": self.complex_validator,
            "list": self.list_validator,
            "tuple": self.tuple_validator,
            "dict": self.dict_validator,
            "set": self.set_validator,
            "bool": self.bool_validator,
            "none": self.none_validator,
            "bytes": self.bytes_validator,
            "bytearray": self.bytearray_validator,
            "object": self.object_validator
        }
    def __call__(self, property_name: str, value: any, *args):
        if property_name not in self.member_map and args:
            self.register_member(property_name, list(args))
        else:
            return True
        for validator in self.member_map[property_name]:
            valid = self.validator_map[validator](value)
            if valid:
                return True
            else:
                print(f"{validator} failed for variable '{property_name}' with value '{value}'.")
                continue
        raise ValueError(f"{self.variable_map[property_name]} validation failed for variable '{property_name}' with value '{value}'.")
    def validate_all(self, variables: dict):
        for key, value in variables.items():
             valid = self.validate(key, value)
    def register_member(self, member_id: str, validators: list[str]):
        member_id = member_id
        validators = validators
        if member_id not in self.member_map:
            self.member_map[member_id] = validators
        else:
            raise KeyError(f"{self.member_id} already exists")
    def string_validator(self, value):
        return isinstance(value, str)
    def int_validator(self, value):
        return isinstance(value, int)
    def float_validator(self, value):
        return isinstance(value, float)
    def complex_validator(self, value):
        return isinstance(value, complex)
    def list_validator(self, value):
        return isinstance(value, list)
    def tuple_validator(self, value):
        return isinstance(value, tuple)
    def dict_validator(self, value):
        return isinstance(value, dict)
    def set_validator(self, value):
        return isinstance(value, set)
    def bool_validator(self, value):
        return isinstance(value, bool)
    def none_validator(self, value):
        if value is None:
            return True
        else:
            return False
    def bytes_validator(self, value):
        return isinstance(value, bytes)
    def bytearray_validator(self, value):
        return isinstance(value, bytearray)
    def object_validator(self, value):
        return isinstance(value, object)