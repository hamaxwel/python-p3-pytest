

import pytest
from not_none_functions import return_not_none  

def test_return_not_none_with_value():
    assert return_not_none("Test") is True  

def test_return_not_none_with_none():
    assert return_not_none(None) is False 
