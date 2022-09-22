# 4. Coding Question
from main import square_list

#There are three requirements of the function:
#1. that the length of the input and output lists are the same
#2. that the output list is in ascending order
#3. that the output list actually contains the squares of the numbers
# Therefore I will be writing a test for each requirement and then a final test with the example intput and output.

#Testing that the length of the output list is the same length of the input list
def test_square_list_length():
    list = [i for i in range(6)]
    expected = len(list)
    actual = len(square_list(list))
    assert actual == expected

#Testing that the output list is in ascending order (accounting where two are equal!)
def test_square_list_asc():
    list = [3,4,6,7,8,10,13,17,21,21, 26,54,333]
    actual = square_list(list)
    for i in range(len(actual)-1):
        assert actual[i] <= actual[i+1]



#Testing that all the squares of the input list are in the output list
def test_square_list_output2():
    list = [3,5,2,9]
    expected = [9,25,4,81]
    actual = square_list(list)
    for i in expected:
        assert i in actual

#Testing that we get the example output (where 65 is actually.. 64) for the example input
def test_square_list_output():
    list = [1,2,3,5,6,8,9]
    expected = [1,4,9,25,36,64,81]
    actual = square_list(list)
    assert actual == expected