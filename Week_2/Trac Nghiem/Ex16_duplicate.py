def function_helper(x, data):
    for i in data:
        # Your code here
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1


def my_function(data):

    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)

    return res


<<<<<<< HEAD
if __name__ == "__main__":
    lst = [10, 10, 9, 7, 7]
    assert my_function(lst) == [10, 9, 7]

    lst = [9, 9, 8, 1, 1]
    print(my_function(lst))
=======
lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function(lst))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72
