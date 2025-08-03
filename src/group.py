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
        Initialize a group with a unique identifier.
        
        Params:
            member_id (str): A unique identifier for the group.
        """

        # Set the properties of the group which include a unique identifier and a dictionary to hold members.
        self.member_id = member_id
        self._members = []
    def __str__(self) -> str:
        """
        Returns a string representation of the group.
        
        Returns:
            str: A string representation of the group in the format "Group ID: member_id, Members: [member1, member2, ...]".
        """

        # Creates and returns a string that represents the Configuration as a whole. 
        return f"Group ID: {self.member_id}, Members: {[f'{member}' for member in self.members]}"
    def __repr__(self) -> str:
        """
        Returns a string representation of the group for debugging purposes.
        
        Returns:
            str: A string representation of the group in the format "Group(member_id), [member1, member2, ...]".
        """

        return f"Group({self.member_id}), {[f"{repr(value)}" for value in self.members]}"
    def __call__(self, initial_value = None,
                 member_id : str = "",
                 member : 'SubGroup | Setting | None' = None
                 ) -> 'Setting | SubGroup':
        """
        Allows the group to be called with a member ID and an optional initial value,
        adding a new member to the group.

        Params:
            initial_value: The initial value of the Setting to be created and added.
            member_id (str): A unique identifier for the member to be created and added.
            member (SubGroup | Setting): A prexisting member to add to the group.

        Returns:
            Setting: A new Setting instance if initial_value is provided, otherwise a SubGroup instance.
            Group: A new SubGroup instance if initial_value is not provided.
        """

        if (initial_value or member_id) and member:
            raise ValueError("Still gonna rework this and not writing anything fancy right now")
        if initial_value and member_id:
            new_member = Setting(member_id, initial_value)
            self.add_member(new_member)
        elif member_id:
            new_member = SubGroup(member_id, self)
            self.add_member(new_member)
        elif member:
            new_member = member
            self.add_member(new_member)
        else:
            raise ValueError("Same shit as before I'm not really ready to work on this")
        return new_member
    @property
    def member_id(self) -> str:
        """
        Provides access to the private variable member_id.

        Returns:
            _member_id (str): A unique identifier for the member to be added.
        """

        # Provides access to the private variable _member_id through member_id
        return self._member_id
    @member_id.setter
    def member_id(self, member_id: str):
        """
        Assigns a new member id to the private variable member_id.
        
        Parmas: 
            member_id (str): A unique identifier for the member to be added.
        """

        self._member_id = member_id
    @property
    def members(self) -> list:
        """
        Returns the private variable _members.

        Returns:
            _members (list): A list of the current members of the Master Group.
        """

        return self._members
    @members.deleter
    def members(self):
        """
        Deletes the private variable _members.
        """

        del self._members
    @property
    def serialized_state(self)-> dict:
        """
        Calls the to_dict methods to assemble the dictionary representation of the configuration.

        Returns:
            to_dict (dict): A dictionary representation of the entire configuration.
        """

        # returns the a dictionary representation of the the enitre configuration.
        return self.to_dict()
    def add_member(self, member_to_add: 'Setting | SubGroup | MasterGroup'):
        """
        Adds a member to the configuration.
        
        Params:
            member_to_add (Setting | SubGroup): A member of the configuration.
        """

        # Adds a new entry.
        self._members.append(member_to_add)
    def remove_member(self, member_id: str) -> bool:
        """
        Removes a member with the member_id from the configuration.

        Params:
            member_id (str): A unique identifier for the member. 
        """

        found_member = False # Tracks if member is found.
        # Loops through the members list, if a member with the correct id is found. Removes it.
        for i in (0, len(self.members)):
            if self.members[i] == member_id:
                self.members[i].pop
                found_member = True
        return found_member # Returns bool to determine if member is found and deleted
    def to_dict(self)-> dict:
        """
        Convert the group and its members to a dictionary representation.

        Returns:
            dict: A dictionary containing the group's ID and all its members' configurations.
        """

        # This function has each member return it's set up members to build the complete configuration.
        app_dict = {}
        for member in self.members:
            app_dict.update(member.to_dict())
        # Returns the formatted dictionary representation of the configuration.
        return {
            "id": self.member_id,
            "config":{
                self.member_id: app_dict
            }
        }
class SubGroup(MasterGroup):
    """
    A subgroup within a configuration hierarchy.
    
    SubGroup extends MasterGroup to provide hierarchical organization of settings.
    It maintains a reference to its parent group and prevents circular references
    in the configuration hierarchy.
    """

    def __init__(self, member_id: str, master_group: 'MasterGroup | SubGroup'):
        """
        Initialize a SubGroup instance.

        Params:
            member_id (str): Unique identifier for this subgroup.
            master_group (MasterGroup): Parent group containing this subgroup.
        """

        super().__init__(member_id)
        self._master_group = master_group
    @property
    def master_group(self) -> 'MasterGroup':
        """
        Get the parent group of this subgroup.

        Returns:
            MasterGroup: The parent group containing this subgroup.
        """
        
        return self._master_group
    def add_member(self, member: 'Setting | SubGroup'):
        """
        Add a new member to this subgroup.

        Checks for circular references before adding the member.

        Params:
            member (Setting | SubGroup): The member to add to this subgroup.

        Raises:
            ValueError: If adding the member would create a circular reference.
        """

        if not self.check_heritage(member, self.master_group):
            raise ValueError(f"To avoid circular references, {member.member_id} cannot be added to {self.member_id}")
        super().add_member(member)
    def check_heritage(self, member_to_add: 'Setting | SubGroup', master_group: 'MasterGroup | SubGroup') -> bool:
        """
        Check if adding a member would create a circular reference.

        Traverses up the group hierarchy to ensure the member is not already
        present in the parent chain.

        Params:
            member_to_add (Setting | SubGroup): The member to check.
            master_group (MasterGroup): The current group to check against.

        Returns:
            bool: True if the member can be added safely, False if it would create a circular reference.
        """

        searching = True
        while searching:
            if member_to_add == master_group:
                return False
            elif isinstance(master_group, MasterGroup):
                return True
            else:
                master_group = master_group.master_group
        return False
    def to_dict(self) -> dict:
        """
        Convert the subgroup to a dictionary representation.

        Returns:
            dict: A dictionary containing all members of this subgroup.
                Format: {member_id: {member_configurations}}
        """

        member_dict = {}
        for member in self.members:
            member_dict.update(member.to_dict())
        return {self.member_id: member_dict}