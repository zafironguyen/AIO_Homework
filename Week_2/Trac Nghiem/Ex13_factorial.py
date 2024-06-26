def factorial(x):
    var = 1
    while x > 1:
        var *= x
        x -= 1
    return var


if __name__ == "__main__":
    assert factorial(8) == 40320
    print(factorial(4))
