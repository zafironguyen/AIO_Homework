def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list)-k + 1):
        result.append(max(num_list[i: i+k]))
    return result

<<<<<<< HEAD

if __name__ == "__main__":
    assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3

    print(max_kernel(num_list, k))
=======

assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

print(max_kernel(num_list, k))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72
