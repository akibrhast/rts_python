def n_above_inputs(array: list[int],value:int) -> dict:
    """Print's the number of integer array that are above the given input value
    and the number that are below the input value

    Arguments:
    array -- a list of integers
    value -- a integer to use against the list 
    """

    result_object = {"above": 0, "below": 0}
    for index,arr_value in enumerate(array):
        if(arr_value < value):
            result_object["below"] +=1
        elif(arr_value > value):
            result_object["above"] +=1

    return result_object

print(n_above_inputs([1, 5, 2, 1, 10],6))  # prints: {"above":1,"below":4}



def rotate_string(string_value: str, input_value: int) -> str:
    """Rotate the characters in a string by a given input 
    and have the overflow appear at the beginning

    Arguments
    string_value -- the string that is to be rotated
    input_value -- the number of charecters to rotate from end of the string
    """
    return  string_value[len(string_value)-input_value : ]  + string_value[0 : len(string_value)-input_value] 

print(rotate_string("MyString", 2)) # prints: "ngMyStri"