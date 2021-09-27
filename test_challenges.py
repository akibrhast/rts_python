from challenges import n_above_inputs, rotate_string


def test_n_above_inputs():
    assert n_above_inputs([1, 5, 2, 1, 10],6) == {"above":1,"below":4}


def test_rotate_string():
    assert rotate_string("MyString", 2) == "mgMyStri"