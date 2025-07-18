import json
import yaml

class To_File:
    """
    A class for serializing and deserializing configuration data to/from files.

    Supports multiple file formats including JSON and YAML. Handles the reading and
    writing of configuration data to persistent storage.
    """

    def __init__(self):
        """
        Initialize the serializer with supported file formats.
        """

        self.supported_formats = {
            'json': json,
            'yaml': yaml
        } 
    def serialize(self, configuration_dict: dict, file_path: str) -> None:
        """
        Serialize a configuration dictionary to a file.

        Params:
            configuration_dict (dict): The configuration data to serialize.
            file_path (str): Path to the file where the data should be saved. Must end in .json or .yaml.
        """

        with open(file_path, 'w') as config_dict:
            self.supported_formats[self.file_format(file_path)].dump(
                configuration_dict, config_dict, indent=4)
    def load_config(self, file_path: str) -> dict:
        """
        Load a configuration from a file.

        Params:
            file_path (str): Path to the configuration file to load. Must end in .json or .yaml.
        Returns:
            dict: The loaded configuration data.
        Raises:
            ValueError: If the file format is not supported.
        """

        with open(file_path, 'r') as config_dict:
            loaders = {
                "json": json.load(config_dict),
                "yaml": yaml.load(config_dict, Loader=yaml.FullLoader)
            }
            return loaders[self.file_format(file_path)]
    def file_format(self, file_path: str) -> str:
        """
        Extract the file format from a file path.

        Params:
            file_path (str): The path to the file.

        Returns:
            str: The file format (json or yaml).
        """
        return file_path[-4:len(file_path)]