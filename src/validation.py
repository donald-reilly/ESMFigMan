
class Validation:
    """A class for validating configuration values against their expected types.
    
    Provides type checking for various Python data types and allows registration
    of configuration members with their expected types. Can validate individual
    values or entire configuration dictionaries.
    """
    def __init__(self, **kwargs):
        """Initialize the validator with member type mappings.

        Args:
            **kwargs: Keyword arguments mapping member names to lists of valid types.
        """
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
        
    def __call__(self, property_name: str, value: any, *args) -> bool:
        """Validate a value against its expected types.

        Args:
            property_name (str): The name of the property to validate.
            value (any): The value to validate.
            *args: Optional type names to register for this property.

        Returns:
            bool: True if validation succeeds.

        Raises:
            ValueError: If validation fails for all registered types.
        """
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
        raise ValueError(f"Validation failed for variable '{property_name}' with value '{value}'.")
        
    def validate_all(self, variables: dict) -> None:
        """Validate all variables in a dictionary.

        Args:
            variables (dict): Dictionary of variable names and values to validate.

        Raises:
            ValueError: If any validation fails.
        """
        for key, value in variables.items():
            self(key, value)
            
    def register_member(self, member_id: str, validators: list[str]) -> None:
        """Register a new member with its valid types.

        Args:
            member_id (str): The name of the member to register.
            validators (list[str]): List of valid type names for this member.

        Raises:
            KeyError: If the member is already registered.
        """
        if member_id not in self.member_map:
            self.member_map[member_id] = validators
        else:
            raise KeyError(f"Member '{member_id}' already exists")
    def string_validator(self, value: any) -> bool:
        """Validate that a value is a string.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a string.
        """
        return isinstance(value, str)

    def int_validator(self, value: any) -> bool:
        """Validate that a value is an integer.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is an integer.
        """
        return isinstance(value, int)

    def float_validator(self, value: any) -> bool:
        """Validate that a value is a float.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a float.
        """
        return isinstance(value, float)

    def complex_validator(self, value: any) -> bool:
        """Validate that a value is a complex number.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a complex number.
        """
        return isinstance(value, complex)

    def list_validator(self, value: any) -> bool:
        """Validate that a value is a list.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a list.
        """
        return isinstance(value, list)

    def tuple_validator(self, value: any) -> bool:
        """Validate that a value is a tuple.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a tuple.
        """
        return isinstance(value, tuple)

    def dict_validator(self, value: any) -> bool:
        """Validate that a value is a dictionary.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a dictionary.
        """
        return isinstance(value, dict)

    def set_validator(self, value: any) -> bool:
        """Validate that a value is a set.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a set.
        """
        return isinstance(value, set)

    def bool_validator(self, value: any) -> bool:
        """Validate that a value is a boolean.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a boolean.
        """
        return isinstance(value, bool)

    def none_validator(self, value: any) -> bool:
        """Validate that a value is None.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is None.
        """
        return value is None

    def bytes_validator(self, value: any) -> bool:
        """Validate that a value is a bytes object.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a bytes object.
        """
        return isinstance(value, bytes)

    def bytearray_validator(self, value: any) -> bool:
        """Validate that a value is a bytearray.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is a bytearray.
        """
        return isinstance(value, bytearray)

    def object_validator(self, value: any) -> bool:
        """Validate that a value is any Python object.

        Args:
            value (any): The value to validate.

        Returns:
            bool: True if the value is any Python object (always returns True).
        """
        return isinstance(value, object)