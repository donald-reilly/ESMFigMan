import pytest
from src.setting import Setting

@pytest.fixture
def setting_example():
    """
    A factory fixture for providing controlled instances of the Setting class.
    """
    def _create_setting(**kwargs):
        """
        Creates an instance of Setting. If no arguements are provided 
        then a default setting is created.
        """
        if kwargs:
            return Setting(**kwargs) # returns a custom setting.
        else:
            return Setting("default_id", "default_value") # returns a default setting.
    return _create_setting
