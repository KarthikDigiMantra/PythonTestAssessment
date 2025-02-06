from main import add 
import pytest
# checking method for empty value 
def test_empty():
    assert add('') == 0
# checking for single value 
def test_singlevalue():
    assert add('1') == 1
# checking for multiple values 
def test_multiplevalues():
    assert add('1,5') == 6
# checking for negative values 
def test_negative_num():
    with pytest.raises(Exception) as expInfo:
        add('1,-5') 
    assert str(expInfo.value) == "negative number not allowed -5"
# checking for newline characters 
def test_newline_chars():
    assert add('1,\n5') == 6
# checking different demiliter 
def test_newline_chars():
    assert add('//;1;\n5') == 6
