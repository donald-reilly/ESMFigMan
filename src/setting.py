class Setting:
    """
    A class representing a member, which has a unique identifier and a value.
    """

    def __init__(self, member_id: str, initial_value): 
        """
        Initializes a member with a unique identifier and an initial value.
        
        Params:
            member_id (str): A unique identifier for the member.
            initial_value: The initial value of the member.
        """

        # Set the properties of the member
        self._initialize_properties(member_id, initial_value)
    def __str__(self) -> str:
        """
        Returns a string representation of the member.

        Returns:
            str: A string representation of the member in the format "member_id: value".
        """

        return str(self.to_dict)
    def __repr__ (self) -> str:
        """
        Returns a string representation of the member for debugging purposes.
        
        Returns:
            str: A string representation of the member in the format "Setting(member_id = member_id, initial_value = value)".
        """
        
        return f"Setting(member_id = {self.member_id}, initial_value = {self.value})"
    def __call__(self, member_id: str = "", value = None):
        """
        Allows the member to be called with a new value, or member_id updating their values.

        Params:
            member_id: (str) A member id for the instance
            value: The value for the instance.
        """

        if value:
            self.value = value
        if member_id:
            self.member_id = member_id

    def __add__(self, other) -> 'Setting':
        """
        Combines the value of this member with another member's value if they are compatible.

        Params:
            other: (Setting): Another Setting instance to combine with.
            
        Returns:
            Setting: A new Setting instance with the combined value if compatible, otherwise raises an error.
        Raises:
            ValueError: If the values are not compatible for addition.
            TypeError: If the other object is not a Setting instance.
        """

        # Check if the other object is an instance of Setting and shares the same member_id
        if isinstance(other, Setting):
            if type(self.value) is type(other.value) and self.member_id == other.member_id:
                new_value = self.value + other.value
                return Setting(self.member_id, new_value)
            else:
                raise ValueError("Cannot combine dissimilar settings")
        else: 
            raise TypeError()
                
    def _initialize_properties(self, member_id, initial_value):
        """
        Initializes the properties of the member.
        
        Params:
            member_id (str): A unique identifier for the member.
            initial_value: The initial value of the member.
        """

        # Initialize the properties of the member
        self.member_id = member_id 
        self.value = initial_value
        self._to_dict = {self.member_id: self.value}
        self._has_changed = False # Tracks object state for dictionary update
    @property
    def member_id(self) -> str:
        return self._member_id # Grants access to the private variable _member_id
    @member_id.setter
    def member_id(self, member_id: str):
        self._has_changed = True # Update state change 
        self._member_id = member_id # Setter for the private variable _member_id
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._has_changed = True # Update state change
        self._value = value
    @property
    def to_dict(self) -> dict:
        """
        Returns the dictionary representation of the member's state.

        Returns:
            dict: A dictionary representation of the member's state.
        """
        
        # Returns the dictionary representation of the member's state
        if self._has_changed is True:
            self._has_changed = False
            self._to_dict = {self.member_id: self.value} 
        return self._to_dict
            