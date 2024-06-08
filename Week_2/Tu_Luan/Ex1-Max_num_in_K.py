def max_num_in_K(num_list:list, k:int):
    answer = []
    for i in range(len(num_list)-k +1):
        answer.append(max(num_list[i: i+k]))
    return answer


num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
print(max_num_in_K(num_list,k=3))