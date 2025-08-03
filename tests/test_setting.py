import pytest
import json

from src.setting import Setting

"""
Test for the setting class.
 -Initializaiton test
 -Str and repr test
 -Property getter and setter test
 -__add__ test
 -__call__ test
 -to_dict test
"""
# setting_setup_params is the base case for creating the Setting class for testing
# it covers all "legal" inputs for both the member_id and initial value
# I
with open("tests/setting_parameters.json", 'r') as setup_params:
    setting_setup_params = json.load(setup_params)

mixed_test_id = [f"{param["member_id"]!r}--{type(param["initial_value"]).__name__}" for param in setting_setup_params["mixed_setup"]]
math_test_id = [f"{param["member_id"]!r}--{type(param["initial_value"]).__name__}" for param in setting_setup_params["math_setup"]]
mixed_standard_tests = ("params", setting_setup_params["mixed_setup"])


@pytest.mark.parametrize(*mixed_standard_tests, ids=mixed_test_id)
def test_setting(setting_example, params):
    """
    Tests that Setting initializes and that both member_id and initial_value only accept valid arguements
    """
    test_setting = setting_example(**params) # Unpack kwargs for Setting creation
    assert isinstance(test_setting, Setting)# Tests that Setting is instantiated correctly
    assert test_setting.member_id == params["member_id"] and type(test_setting.member_id) == type(params["member_id"]) # Tests that member_id's value and type are correct
    assert test_setting.value == params["initial_value"] and type(test_setting.value) == type(params["initial_value"]) # Tests that initial_value's value and type are correct
    assert test_setting.to_dict == {params["member_id"]: params["initial_value"]}

@pytest.mark.parametrize(*mixed_standard_tests, ids=mixed_test_id)
def test_str_repr_standard(setting_example, params):
    """
    Tests the both the str and repr methods of Setting for accuracy.
    """

    test_setting = setting_example(**params)
    assert str(test_setting) == str({params["member_id"]: params["initial_value"]})
    assert repr(test_setting) == f"Setting(member_id = {params["member_id"]}, initial_value = {params["initial_value"]})"
    test_setting("member_id", "change_test")
    assert str(test_setting) == str({"member_id": "change_test"})
@pytest.mark.parametrize("params", setting_setup_params["mixed_setup"], ids=mixed_test_id)
def test_call(setting_example, params):
    """
    Tests the call dunder method for changing the value held at member.value
    """
    test_setting = setting_example()
    test_setting(params["member_id"], params["initial_value"])
    print(test_setting.value)
    print(params["initial_value"])
    assert test_setting.value == params["initial_value"]

@pytest.mark.parametrize("params", setting_setup_params["math_setup"], ids=math_test_id)
def test_add(setting_example, params):
    """
    Tests the __add__ method
    """
    test_setting_0 = setting_example(member_id = params["member_id"], initial_value = params["initial_value"])
    test_setting_1 = setting_example(member_id = params["member_id"], initial_value = params["additional_value"])

    result_setting = test_setting_0 + test_setting_1

    assert result_setting.value == params["initial_value"] + params["additional_value"]