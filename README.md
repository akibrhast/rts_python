# RTS Labs-[Python]

This repository contains a coding  excercise by RTS Labs. The coding excercise contains three questions which are listed below


## Questions Asked
1. Print the number of integers in an array that are above the given input and the number that are below, e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.

```python
def n_above_inputs(array: list,value:int) -> dict:
    '''
    Print's the number of integer array that are above the given input value
    and the number that are below the input value
    '''

    return result
print(n_above_inputs([1, 5, 2, 1, 10],6))  # prints: {"above":1,"below":4}
```


2. Rotate the characters in a string by a given input and have the overflow appear at the beginning, e.g. “MyString” rotated by 2 is “ngMyStri”.

```python
def rotate_string(string_value, input_value):
    '''
    Rotate the characters in a string by a given input 
    and have the overflow appear at the beginning
    '''
    return result
print(rotate_string("MyString", 2))# prints: "mgMyStri"
```

3. If you could change 1 thing about your favorite framework/language/platform (pick one), what would it be?

```python
# My favourite language would be python at the moment,
# and my favourite framework would be flask.
# The flask framework has some typical common design pattern of begeiner,
# intermediary and advanced level. I have often wished for the core framework to 
# come bootstrapped with commands such that it will allow for hoisting 
# the structure of said level of design pattern
# For example, # I could possibly do something like 
# `flask hoist entry/intermediary/advanced`
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/akibrhast/rts_python.git
```

Go to the project directory

```bash
  cd rts_python
```

Install dependencies

```bash
  python -m venv env
  pip install -r requirements.txt
```

Run Tests

```bash
  pytest -v
```




## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/akibmr)

[HomeCheff](https://homecheff.herokuapp.com/)

[Open-Lib](https://open-lib.herokuapp.com/) ... [Ask me for demo]

[Perfect Sense Blog](https://perfectsenseblog.herokuapp.com/) ... [use 'testuser' for username and password]

[HackOrSnooze](https://akibrhast.github.io/Hack-Or-Snooze/)
