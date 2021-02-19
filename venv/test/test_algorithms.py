import pytest
import os
import json
import sys

VALUE_WITH_CHECKSUM = 0
VALUE_INITIAL = 1
EXPECTED_CHECK_DIGIT_LENGTH = 1
EXPECTED_VALUES = [
    ('1996012101289', '199601210128'),
    ('1960031203012', '196003120301'),
    ('1995050921153', '199505092115'),
    ('0000000000000', '000000000000')
]

sys.path.insert(1, '../src')

from algorithms import mod_11_algorithm

def test_mod11Algorithm():
    for index, expectedValue in enumerate(EXPECTED_VALUES):
        assert expectedValue[VALUE_WITH_CHECKSUM][-EXPECTED_CHECK_DIGIT_LENGTH:] == mod_11_algorithm(expectedValue[VALUE_INITIAL]), f'Check Sum Doesn''t Match Expected Value in Pair: {index}'

def test_mod11AlgorithReturnLength():
    assert len(mod_11_algorithm('199601210128')) == EXPECTED_CHECK_DIGIT_LENGTH, f'Check Digits are Expected to be {EXPECTED_CHECK_DIGIT_LENGTH} Characters Long'

#non-digits should result in a ValueError
def test_mod11AlgorithValueError():
    with pytest.raises(ValueError) as error_info:
        mod_11_algorithm('1996012A0128')

#negative values should result in a ValueError



def test_mod11AlgorithNegativeValue():
    with pytest.raises(ValueError) as error_info:
        mod_11_algorithm('-199601210128')

def test_mod11AlgorithEmptyValue():
    with pytest.raises(IndexError) as error_info:
        mod_11_algorithm('')
