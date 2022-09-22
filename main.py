import unittest

# q9
def two_number_sum(int_list, target_sum):
    output = []
    for i in range(len(int_list)):
        target_int = target_sum - int_list[i]
        for n in range(i+1, len(int_list)):
            if target_int == int_list[n]:
                output.extend([int_list[i], int_list[n]])
    return output


