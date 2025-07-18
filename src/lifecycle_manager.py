from src.serialize import To_File
from src.group import MasterGroup, SubGroup

class LifeCycleManager:
    """
    Manages the lifecycle of configuration objects.
    
    This class is responsible for saving and loading configurations to/from files,
    maintaining the current state of configurations, and handling the serialization
    and deserialization of configuration objects.
    """
    
    def __init__(self):
        """
        Initialize a new LifeCycleManager instance.
        
        Sets up the serialization manager and initializes storage for configurations.
        """

        self._slm = To_File() # Instance of serialization manager.
        self._configurations = {} # Variable to store configuration references. 
        self._current_config = {} # Variable ot store the current configuration.
    def _save_config(self, group: MasterGroup, file_path: str = ''):
        """
        Save a configuration to a file.
        
        Params:
            group (MasterGroup): The configuration to save, must have an 'id' key.
        Args:
            file_path (str, optional): The path where to save the configuration.
                                       If None, uses the previously saved path for this config.
        """

        config = self.group_to_dict(group)

        if file_path:
            self._save_config_as(config['id'], file_path)
        self._slm.serialize(config, self._retrieve_file_info(config['id'], "Save"))
    def _save_config_as(self, config_id, file_path: str):
        """
        Associate a configuration with a file path.
        
        Params:
            config (dict): The configuration to save, must have an 'id' key.
            file_path (str): The path where the configuration should be saved.
        """

        self._configurations[config_id] = file_path
    def _retrieve_file_info(self, config_id: str, operation: str) -> str:
        """
        Get the file path associated with a configuration.
        
        Params:
            config (dict): For "Save" operations, a config dict with an 'id' key.
                           For "Load" operations, the config ID string.
            operation (str): Either "Save" or "Load" to indicate the operation type.
            
        Returns:
            str: The file path associated with the configuration.
        """

        if operation == "Save":
           return self._configurations[config_id]
        elif operation == "Load":
            return self._configurations[config_id]
    def _load_config(self, config: str) -> MasterGroup:
        """
        Load a configuration from a file.
        
        Params:
            config (str): The configuration ID to load.
            
        Returns:
            MasterGroup: The loaded and deserialized configuration.
        """

        file_path = self._retrieve_file_info(config, "Load")
        configuration = self._slm.load_config(file_path)
        deserialized_config = self._deserialize_all(configuration['config'])
        return deserialized_config   
    def _deserialize_all(self, config: dict, top_level: MasterGroup | None = None, current_level: MasterGroup | None = None) -> MasterGroup:
        """
        Recursively deserialize a configuration dictionary into a MasterGroup structure.
        
        Params:
            config (dict): The configuration dictionary to deserialize.
        Args:
            top_level (MasterGroup, optional): The top-level group being built.
            current_level (MasterGroup, optional): The current group being populated.
            
        Returns:
            MasterGroup: The fully constructed configuration group hierarchy.
        """

        for member_id, member_config in config.items():
            if isinstance(member_config, dict):
                if not top_level:
                    top_level = MasterGroup(member_id)
                    current_level = top_level
                    self._deserialize_all(member_config, top_level, current_level)  
                else:
                    new_group = current_level(member_id) # type: ignore
                    self._deserialize_all(member_config, top_level, new_group)              # type: ignore
            else:
                current_level(member_id, member_config) # type: ignore
        return top_level # type: ignore
    def group_to_dict(self, group: MasterGroup | SubGroup) -> dict:
        """
        Returns the dictionary representation of the provided group.

        Params:
            group (MasterGroup, SubGroup): The MasterGroup or SubGroup to be converted to a dictionary.
        
        Returns:
            The serialized_state of the group.
        """

        return group.serialized_state
