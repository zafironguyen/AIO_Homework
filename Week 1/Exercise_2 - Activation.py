import math


def is_num(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def exercise2():
    x = input("Input x: ")
    if not is_num(x):
        return print("x must be a number")
    x = float(x)
    func_name = str(input("Input activation Function (sigmoid|relu|elu) : "))
    match func_name:
        case 'sigmoid':
            return print(f"sigmoid: f({x}) = {1 / (1 + math.e ** (-x))}")
        case 'relu':
            if x <= 0:
                relu_x = 0
            else:
                relu_x = x
            return print(f"relu: f({x}) = {relu_x}")
        case 'elu':
            a = 0.01
            if x <= 0:
                elu_x = a * (math.e ** x - 1)
            else:
                elu_x = x
            return print(f"elu: f({x}) = {elu_x}")
        case _:
            return print(f"{func_name} is not supported")

exercise2()