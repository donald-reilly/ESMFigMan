from src.group import MasterGroup
from src.lifecycle_manager import LifeCycleManager

class FigMan:
    def __init__(self):
        self.lcm = LifeCycleManager()

    def configuration(self, member_id):
        return MasterGroup(member_id)
    
    def save(self, config, file_path):
        self.lcm._save_config(config, file_path)
    
    def load(self, config):
        config = self.lcm._load_config(config)
        return config