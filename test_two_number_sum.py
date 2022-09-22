from main import two_number_sum
import unittest
import pytest


def test_correct_sum1():
    int_list = [4, 6, 7, 2, 19]
    target_sum = 9
    expected = [7,2]
    assert two_number_sum(int_list, target_sum) == expected

def test_correct_nosum():
    int_list = [2,3,5,7,12]
    target_sum = 3
    expected = []
    assert two_number_sum(int_list, target_sum) == expected

def test_correct_twosums():
    int_list = [5,6,12,7,3,10,64,46,23,8,33]
    target_sum = 56
    expected = [10, 46, 23, 33]
    assert two_number_sum(int_list, target_sum) == expected

def test_corect_duplicate():
    int_list = [3,5,7,12,76,3,4,1]
    target_sum = 8
    expected = [3,5,5,3,7,1]
    assert two_number_sum(int_list, target_sum) == expected




