import pytest


def float_to_int(x): # function to convert float to integer (i.e.: 2014.0 to 2014)
    split_string = x.split(".") # splits input argument at decimal point, returns an array (i.e.: 2014.0 to [2014, 0])
    substring = split_string[0] # takes the value at the index 0 of new array (i.e.: 2014 of [2014, 0])
    if len(substring) > 0: # if the length of the substring is greater then 0 (which means, in the case that there is data in that cell) 
        return int(substring) # convert the substring to an integer, and return that integer
    else: # otherwise (in the case that there is no data in that cell)
        return '' # return an empty string


def test_float_to_int_function():
    assert float_to_int('2014.0') == 2014

def test2_float_to_int_function():
    assert float_to_int('2014.0') == 2015

   


