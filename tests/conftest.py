import pytest
from src.setting import Setting

@pytest.fixture
def setting_example():
    """
    A factory fixture for providing controlled instances of the Setting class.
    """
    def _create_setting(**kwargs):
        if kwargs:
            return Setting(**kwargs)
        else:
            return Setting("default_id", "default_value")
    return _create_setting
