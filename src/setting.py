from src.decorators import *

class Setting:
    def __init__(self, member_id: str, initial_value):
        self.initialzie_properties(member_id, initial_value)
        self.value = initial_value
    def __str__(self):
        return str({self.member_id: self.value})
    def __repr__ (self):
        return f"Setting(member_id = {self.member_id}, initial_value = {self.value})"
    def __call__(self, value):
        self.value = value
    def __add__(self, other):
        if isinstance(other, Setting):
            if type(self.value) is type(other.value) and self.member_id == other.member_id:
                new_value = self.value + other.value
                return Setting(self.member_id, new_value)
            else:
                raise ValueError("Cannot combine dissimilar settings")
        else: 
            raise TypeError()
                
    def initialzie_properties(self, member_id, initial_value):
        self.member_id = member_id
        self.value = initial_value
    @property
    def member_id(self) -> str:
        return self._member_id
    @member_id.setter
    def member_id(self, member_id: str):
        self._member_id = member_id
    @property
    def value(self) -> any:
        return self._value
    @value.setter
    def value(self, value: any):
        self._value = value
    @property
    @serialize("member_id", "value")
    def serialized_state(self) -> dict:
        return self._serialized_state
    def to_dict(self):
        return{self.member_id: self.value}