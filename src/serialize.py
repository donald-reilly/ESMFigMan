import json
import yaml

class To_File:
    def __init__(self):
        self.supported_formats = {
            'json' : json,
            'yaml' : yaml
        }
         
    def serialize(self, configuration_dict, file_path):
        with open(file_path, 'w') as config_dict:
            self.supported_formats[self.file_format(file_path)].dump(configuration_dict, config_dict, indent=4)
  
    def load_config(self, file_path):
        with open(file_path, 'r') as config_dict:
            loaders = {
                    "json":json.load(config_dict),
                    "yaml":yaml.load(config_dict, Loader=yaml.FullLoader)
                }
            return loaders[self.file_format(file_path)]
    
    def file_format(self, file_path):
        return file_path[-4:len(file_path)]