import math
import random


# Exercise 1
def exercise1(tp, fp, fn):
    if type(tp) is not int:
        return print('tp must be int')
    if type(fp) is not int:
        return print('fp must be int')
    if type(fn) is not int:
        return print('fn must be int')
    if tp <= 0 or fp <= 0 or fn <= 0:
        return print('tp and fp and fn must be greater than zero')
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f'precision is : {precision}\n'
          f'recall is : {recall}\n'
          f'f1_score is : {f1_score}')


# exercise1(tp=2, fp=3, fn=4)
# exercise1(tp="a", fp=3, fn=4)
# exercise1(tp=2, fp="a", fn=4)
# exercise1(tp=2, fp=3, fn="a")
# exercise1(tp=2, fp=3, fn=0)
# exercise1(tp=2.1, fp=3, fn=0)


# Exercise 2
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


# exercise2()


#  Exercise 3
def exercise3():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        return print('number of samples must be an integer number')
    num_samples = int(num_samples)
    loss_name = input("Input loss name: ")
    match loss_name:
        case 'MAE':
            total = 0
            for i in range(num_samples):
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = abs(target - predict)
                total += loss
                print(f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}')
            return print(f'final MAE: {total / num_samples}')
        case 'MSE':
            total = 0
            for i in range(num_samples):
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = (target - predict) ** 2
                total += loss
                print(f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}')
            return print(f'final MSE: {total / num_samples}')
        case 'RMSE':
            total = 0
            for i in range(num_samples):
                predict = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss = (target - predict) ** 2
                total += loss
                print(f'loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}')
            return print(f'final RMSE: {math.sqrt(total / num_samples)}')
        case _:
            return print("Invalid regression loss function")


# exercise3()


# Exercise 4:
def factorial(x):
    if x > 0:
        return x * factorial(x - 1)
    else:
        return 1


def approx_sin(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (-1) ** i * (x ** (2 * i + 1) / factorial(2 * i + 1))
    return print(answer)


def approx_cos(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (-1) ** i * (x ** (2 * i) / factorial(2 * i))
    return print(answer)


def approx_sinh(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (x ** (2 * i + 1) / factorial(2 * i + 1))
    return print(answer)


def approx_cosh(x, n):
    if n <= 0:
        return print('n should be greater than 0')
    answer = 0
    for i in range(n + 1):
        answer += (x ** (2 * i) / factorial(2 * i))
    return print(answer)


# approx_sin(x=3.14,n=10)
# approx_cos(x=3.14,n=10)
# approx_sinh(x=3.14,n=10)
# approx_cosh(x=3.14,n=10)


# Exercise 5
def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    loss = (y_root - y_hat_root) ** p
    return print(loss)


md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1)
md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1)
md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1)
md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1)
