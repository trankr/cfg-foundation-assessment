# 3. Coding Question
def square_list(int_list):
    square_list = [int**2 for int in int_list]
    return sorted(square_list)




# 9. Coding Question
def two_number_sum(int_list, target_sum):
    output = []
    for i in range(len(int_list)):
        target_int = target_sum - int_list[i]
        for n in range(i+1, len(int_list)):
            if target_int == int_list[n]:
                output.extend([int_list[i], int_list[n]])
    return output


