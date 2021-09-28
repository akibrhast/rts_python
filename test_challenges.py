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


def test_rotate_string():
    assert rotate_string("MyString", 2) == "ngMyStri"