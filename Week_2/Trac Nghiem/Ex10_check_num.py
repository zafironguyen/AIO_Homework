def check_num(integers, number=1):
    return any(True if i == number else False for i in integers)


<<<<<<< HEAD
if __name__ == "__main__":
    my_list = [1, 3, 9, 4]
    assert check_num(my_list, -1) == False

    my_list = [1, 2, 3, 4]
    print(check_num(my_list, 2))
=======
my_list = [1, 3, 9, 4]
assert check_num(my_list, -1) == False


my_list = [1, 2, 3, 4]
print(check_num(my_list, 2))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72
