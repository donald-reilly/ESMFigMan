from src.group import MasterGroup
from src.lifecycle_manager import LifeCycleManager

class FigMan:
    """
    FigMan (Configuration Manager) is the main interface for managing configurations.

    This class provides a high-level interface for creating, loading, and saving
    configuration objects. It manages the lifecycle of configuration objects and
    provides access to configuration groups.
    """

    def __init__(self):
        """
        Initialize a new FigMan instance.
        Creates a new LifeCycleManager instance to handle configuration lifecycle operations.
        """

        # A reference to an instance of LifeCycleManager
        self.lcm = LifeCycleManager()
    def configuration(self, member_id: str) -> MasterGroup:
        """
        Create a new configuration group.

        Params:
            member_id (str): Unique identifier for the configuration group.

        Returns:
            MasterGroup (MasterGroup): A new master configuration group instance.
        """

        # Returns the MasterGroup of the configuration.
        return MasterGroup(member_id)
    def save(self, config: MasterGroup, file_path: str):
        """
        Save a configuration to a file.

        Params:
            config (MasterGroup): The MasterGroup object to save.
            file_path (str): The path where the configuration should be saved.
        """

        # Saves the configuraiton at the file_path provided.
        self.lcm._save_config(config, file_path)
    def load(self, config_id):
        """Load a configuration from a file.

        Params:
            config: The configuration object to load into.

        Returns:
            The loaded configuration object.
        """

        # Loads the Configuration with the provided config_id.
        config = self.lcm._load_config(config_id)
        return config