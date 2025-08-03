from src.figman import FigMan
from src.group import MasterGroup , SubGroup
from src.setting import Setting
from src.serialize import To_File

def test_setting(window_list):
    for window in range(0, len(window_list)):
        group_id = window_list[window].member_id
        for i in range(0, 4):
            test_setting = window_list[window](f'{group_id}_{i}', f"test1")

def mock_configuration():
    manager = FigMan()
    app = manager.configuration("New_App")
    main_window = app(member_id="Main_Window")
    pop_up = app(member_id = "Pop_up")

    setting_list = [app, main_window, pop_up]
    test_setting(setting_list)
    return manager, app, main_window, pop_up

def map_object(object):
    
manager, app, main_winsow, pop_up = mock_configuration()