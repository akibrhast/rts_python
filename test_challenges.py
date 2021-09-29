from challenges import n_above_inputs, rotate_string
import pytest

@pytest.mark.parametrize(
    "test_input_array,test_input_value, expected",
    [
        ([1, 5, 2, 1, 10],6, {"above":1,"below":4}), 
        ([1, 5, 2, 1, 10],2, {"above":2,"below":2})
    ],
)
def test_n_above_inputs(test_input_array, test_input_value,expected):
    assert n_above_inputs(test_input_array,test_input_value) == expected

@pytest.mark.parametrize(
    "string_to_be_rotated, no_of_chracters_to_be_rotated, expected",
    [
        ("MyString", 2, "ngMyStri"),
        ("catgotyou", 4, "tyoucatgo")
    ],
)
def test_rotate_string(string_to_be_rotated, no_of_chracters_to_be_rotated, expected):
    assert rotate_string(string_to_be_rotated, no_of_chracters_to_be_rotated) == expected