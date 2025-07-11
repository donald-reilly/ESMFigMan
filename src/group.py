from src.setting import Setting
from src.decorators import *
#TODO: Make Iterable
#TODO: Fix __str__ and __repr__
#THOUGHTS: __str__ should be simple, a list of id's would be fine.
#THOUGHTS: __repr__ is going to be a bit harder. Recreating this object is easy enough, but since this is a container i would need to also recreate it's members.
#THOUGHTS: Going about that is kinda difficult I guess. I could just have it print all members, and thier respective values. Could be difficult though idk.
#TODO: __add__ __multiply__ those methods need looking into. 
#THOUGHTS: adding two would be no issue other than the id's again. I"m really not sure how to handle that. The more I mess with this thing the less I want user provided id's.
#THOUGHTS: If I get rid of user provided id's this thing might be easier. 
class MasterGroup:
    def __init__(self, member_id: str):
        self.member_id = member_id
        self.members = {}
    def __str__(self):
        return f"Group ID: {self.member_id}, Members: {[f"{value}" for value in self.members.values()]}"
    def __repr__(self):
        return f"Group({self.member_id}), {[f"{repr(value)}" for value in self.members.values()]}"
    def __call__(self, member_id, initial_value = None):
        if initial_value:
            new_member = Setting(member_id, initial_value)
            self.add_member(new_member)
            return new_member
        else: 
            new_member = SubGroup(member_id, self)
            self.add_member(new_member)
            return new_member
    @property
    def member_id(self):
        return self._member_id
    @member_id.setter
    def member_id(self, member_id: str):
        self._member_id = member_id
    @property
    def members(self):
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
    def add_member(self, member: object):
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
            