def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


<<<<<<< HEAD
if __name__ == "__main__":
    my_list = [5, 2, 5, 0, 1]
    max = 1
    min = 0
    assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1
    print(my_function(max=max, min=min, data=my_list))
=======
my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max=max, min=min, data=my_list))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72
