import pytest
from mainapp import *


# Test to check if a valid CSV file can be loaded
def test_valid_csv():
    logic_instance = TaskFiveLogic()
    assert logic_instance.load_data() is not None


# Test to ensure that an invalid CSV path raises a FileNotFoundError
def test_invalid_csv_path():
    with pytest.raises(FileNotFoundError):
        logic_instance = TaskFiveLogic(data_source='invalid_path.csv')  # Initialize with an invalid path
        logic_instance.load_data()  # Attempt to load data from the invalid path


# Test to ensure that a blank CSV file returns an empty DataFrame
def test_blank_csv():
    logic_instance = TaskFiveLogic(data_source='blank_csv.csv')
    df = logic_instance.load_data()
    assert df.empty


# Test to ensure that data can be filtered by a valid date range
def test_valid_date():
    logic_instance = TaskFiveLogic()
    start_date = "01/01/2012"
    end_date = "01/11/2017"
    df = logic_instance.filter_data_by_date(start_date, end_date)
    assert not df.empty


# Test to ensure that a reformatted date raises a ValueError
def test_reformatted_date():
    logic_instance = TaskFiveLogic()
    with pytest.raises(ValueError):
        logic_instance.filter_data_by_date("2012-01-01", "2017-11-01")


# Test to ensure that a date represented as a string raises a ValueError
def test_date_as_string():
    logic_instance = TaskFiveLogic()
    with pytest.raises(ValueError):
        logic_instance.filter_data_by_date("1st September 2015", "01/11/2017")


# Test to ensure that a float value for date raises a ValueError
def test_date_as_float():
    logic_instance = TaskFiveLogic()
    with pytest.raises(ValueError):
        logic_instance.filter_data_by_date(1.23, "01/11/2017")


# Test to ensure that a list value for date raises a ValueError
def test_date_as_list():
    logic_instance = TaskFiveLogic()
    with pytest.raises(ValueError):
        logic_instance.filter_data_by_date(["01", "01", "2012"], "01/11/2017")


# Test to ensure that a boolean value for date raises a TypeError
def test_boolean_data_type_for_date():
    logic_instance = TaskFiveLogic()
    with pytest.raises(TypeError):
        logic_instance.filter_data_by_date(True, False)


# Test to ensure that a tuple value for date raises a ValueError
def test_tuple_data_type_for_date():
    logic_instance = TaskFiveLogic()
    with pytest.raises(ValueError):
        logic_instance.filter_data_by_date(("01/01/2012", "01/11/2017"), ("02/02/2013", "02/12/2018"))


# Test to ensure that a dictionary value for date raises a ValueError
def test_dict_data_type_for_date():
    logic_instance = TaskFiveLogic()
    with pytest.raises(ValueError):
        logic_instance.filter_data_by_date({"start": "01/01/2012", "end": "01/11/2017"}, {"start": "02/02/2013", "end": "02/12/2018"})


# Test to ensure that passing 'None' for date raises a TypeError
def test_none_data_type_for_date():
    logic_instance = TaskFiveLogic()
    with pytest.raises(TypeError):
        logic_instance.filter_data_by_date(None, "01/11/2017")
    with pytest.raises(TypeError):
        logic_instance.filter_data_by_date("01/01/2012", None)


# Test to ensure that dates after a certain period (e.g. 2017) return an empty DataFrame
def test_date_after_2017():
    logic_instance = TaskFiveLogic()
    start_date = "01/01/2020"
    end_date = "01/11/2020"
    df = logic_instance.filter_data_by_date(start_date, end_date)
    assert df.empty


# Test to ensure that filtering without providing an end date still returns valid data
def test_without_end_date():
    logic_instance = TaskFiveLogic()
    start_date = "01/01/2012"
    df = logic_instance.filter_data_by_date(start_date, "01/11/2017")  # Assuming it defaults to max date
    assert not df.empty


# Test to ensure that filtering without providing a start date still returns valid data
def test_without_start_date():
    logic_instance = TaskFiveLogic()
    end_date = "01/11/2017"
    df = logic_instance.filter_data_by_date("01/01/2012", end_date)  # Assuming it defaults to min date
    assert not df.empty


# Test to check if the location dictionary is returned correctly
def test_get_location_dict():
    logic_instance = TaskFiveLogic()
    location_dict = logic_instance.get_location_dict()
    expected_dict = {
            9623: 'HINTERLAND WAY EWINGSDALE',
            9648: 'PACIFIC HIGHWAY WOODBURN',
            9636: 'NEW ENGLAND HIGHWAY LOCHINVAR',
        }
    assert location_dict == expected_dict


# Test to ensure that swapped keys/values in the location dictionary are detected
def test_swapped_keys_values_in_location_dict():
    logic_instance = TaskFiveLogic()
    location_dict = logic_instance.get_location_dict()
    incorrect_dict = {
        'Mate Street, North Albury': 11634,
        'Moorefields Road, Kingsgrove': 22462,
    }
    assert location_dict != incorrect_dict


# Test to ensure that non-integer keys in the location dictionary are detected
def test_non_integer_keys_in_location_dict():
    logic_instance = TaskFiveLogic()
    location_dict = logic_instance.get_location_dict()
    incorrect_dict = {
        '11634': 'Mate Street, North Albury',
        '22462': 'Moorefields Road, Kingsgrove',
    }
    assert location_dict != incorrect_dict


# Test to ensure that non-string values in the location dictionary are detected
def test_non_string_values_in_location_dict():
    logic_instance = TaskFiveLogic()
    location_dict = logic_instance.get_location_dict()
    incorrect_dict = {
        11634: 11634,
        22462: 22462,
    }
    assert location_dict != incorrect_dict


# Test to ensure that missing keys or values in the location dictionary are detected
def test_missing_keys_or_values_in_location_dict():
    logic_instance = TaskFiveLogic()
    location_dict = logic_instance.get_location_dict()
    incorrect_dict = {
        11634: '',
        22462: 'Moorefields Road, Kingsgrove',
    }
    assert location_dict != incorrect_dict


# Test to ensure that boolean keys/values in the location dictionary are detected
def test_boolean_keys_values_in_location_dict():
    logic_instance = TaskFiveLogic()
    location_dict = logic_instance.get_location_dict()
    incorrect_dict = {
        True: 'Mate Street, North Albury',
        22462: False,
    }
    assert location_dict != incorrect_dict


# Test to ensure that 'None' keys/values in the location dictionary are detected
def test_none_keys_values_in_location_dict():
    logic_instance = TaskFiveLogic()
    location_dict = logic_instance.get_location_dict()
    incorrect_dict = {
        None: 'Mate Street, North Albury',
        22462: None,
    }
    assert location_dict != incorrect_dict
