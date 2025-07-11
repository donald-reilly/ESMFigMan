from src.serialize import To_File
from src.group import MasterGroup

class LifeCycleManager:
    def __init__(self):
        self._slm = To_File()
        self._configurations = {}
        self._current_config = {}
        
    def _save_config(self, config, file_path = None):
        if config['id'] in self._current_config:
            file_path = self._retrieve_file_info(config, "Save")
            self._slm.serialize(config, file_path)
        else:
            self._save_config_as(config, file_path)
            self._save_config(config, file_path)
            
    def _save_config_as(self, config, file_path):
        self._current_config[config['id']] = file_path
        
    def _retrieve_file_info(self, config, operation):
        if operation == "Save":
           return self._current_config[config['id']]
        elif operation == "Load":
            return self._current_config[config]
    
    def _load_config(self, config):
        file_path =self._retrieve_file_info(config, "Load")
        config = self._slm.load_config(file_path)
        deseraizled_config = self._deserialize_all(config['config'])
        return deseraizled_config   
    
    def _deserialize_all(self, config, top_level = None, current_level = None):
        for member_id, member_config in config.items():
            if isinstance(member_config, dict):
                if not top_level:
                    top_level = MasterGroup(member_id)
                    current_level = top_level
                    self._deserialize_all(member_config, top_level, current_level)  
                else:
                    new_group = current_level(member_id)
                    self._deserialize_all(member_config, top_level, new_group)             
            else:
                current_level(member_id, member_config)
        return top_level