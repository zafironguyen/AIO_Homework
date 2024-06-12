def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


<<<<<<< HEAD
if __name__ == "__main__":
    assert my_function([3, 9, 4, 5]) == [3, 9]
    print(my_function([1, 2, 3, 5, 6]))
=======
assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72
