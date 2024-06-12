def factorial(x):
    var = 1
    while x > 1:
        var *= x
        x -= 1
    return var


<<<<<<< HEAD
if __name__ == "__main__":
    assert factorial(8) == 40320
    print(factorial(4))
=======
assert factorial(8) == 40320
print(factorial(4))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72
