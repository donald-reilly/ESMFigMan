from src.setting import Setting
from src.decorators import *

class MasterGroup:
    """
    A class representing the master group of a configuration.
    It can contain multiple members, which can be either individual settings or subgroups.
    Members can be added or removed, and the group can be serialized to a dictionary format.
    """

    def __init__(self, member_id: str):
        """
        Initialized a group with a unique identifier.
        
        Args:
            member_id (str): A unique identifier for the group.
        """

        # Set the properties of the group which include a unique identifier and a dictionary to hold members.
        self.member_id = member_id
        self.members = {}
    def __str__(self) -> str:
        """
        Returns a string representation of the group.
        
        Returns:
            str: A string representation of the group in the format "Group ID: member_id, Members: [member1, member2, ...]".
        """

        return f"Group ID: {self.member_id}, Members: {[{value} for value in self.members.values()]}"
    def __repr__(self) -> str:
        """
        Returns a string representation of the group for debugging purposes.
        
        Returns:
            str: A string representation of the group in the format "Group(member_id), [member1, member2, ...]".
        """

        return f"Group({self.member_id}), {[f"{repr(value)}" for value in self.members.values()]}"
    def __call__(self, member_id : str, initial_value = None) -> 'Setting | SubGroup':
        """
        Allows the group to be called with a member ID and an optional initial value,
        adding a new member to the group.

        Args:
            member_id (str): A unique identifier for the member to be added.
        Params:
            initial_value: The initial value of the member, if applicable.

        Returns:
            Setting: A new Setting instance if initial_value is provided, otherwise a SubGroup instance.
            Group: A new SubGroup instance if initial_value is not provided.
        """
       
        # Creates and returns a new member, a Setting if intial_value is not None, or a SubGroup if it is None.
        if initial_value is not None:
            new_member = Setting(member_id, initial_value)
            self.add_member(new_member)
            return new_member
        else: 
            new_member = SubGroup(member_id, self)
            self.add_member(new_member)
            return new_member
    @property
    def member_id(self) -> str:
        """
        Provides access to the private variable member_id.

        Returns:
            _member_id: A unique identifier for the member to be added.
        """

        return self._member_id
    @member_id.setter
    def member_id(self, member_id: str):
        """
        Assigns a new member id to the private variable member_id.
        
        Parmas: 
            member_id: A unique identifier for the member to be added.
        """

        self._member_id = member_id
    @property
    def members(self) -> dict:
        """
        Returns the private variable _members.

        Returns:
            _members: 
        """

        return self._members
    @members.setter
    def members(self, members: dict):
        self._members = members
    @members.deleter
    def members(self):
        self._members = {}
    @property
    def serialized_state(self):
        return self.to_dict()
    def add_member(self, member):
        self.members[member.member_id] = member
    def remove_member(self, member_id: str):
        if member_id in self.members:
            del self.members[member_id]
        else:
            raise KeyError(f"Member with ID {member_id} not found in group {self.member_id}")
    def to_dict(self):
        app_dict = {}
        for member in self.members.values():
            app_dict.update(member.to_dict())
        return {
            "id": self.member_id,
            "config":{
                self.member_id: app_dict
            }
        }
class SubGroup(MasterGroup):
    def __init__(self, member_id: str, master_group: object = None):
        super().__init__(member_id)
        self.master_group = master_group
    @property
    def master_group(self):
        return self._master_group
    @master_group.setter
    def master_group(self, master_group: object):
        self._master_group = master_group
    def add_member(self, member):
        if not self.check_heritage(member, self.master_group):
            raise ValueError(f"To avoid circular references, {member.member_id} cannot be added to {self.member_id}")
        super().add_member(member)
    def check_heritage(self, member_to_add, master_group):
        searching = True
        while searching:
            if isinstance(master_group, MasterGroup) and member_to_add is not master_group:
                return True
            elif member_to_add is master_group:
                return False
            else:
                master_group = master_group.master_group
    def to_dict(self):
        member_dict = {}
        for member in self.members.values():
            member_dict.update(member.to_dict())
        return {self.member_id: member_dict}
            