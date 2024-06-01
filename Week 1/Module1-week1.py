import math


def calc_elu(x):
    if x > 0:
        return x
    else:
        return 0.01 * (math.e ** x - 1)


assert round(calc_elu(1)) == 1
print(round(calc_elu(-1), 2))


def calc_ae(y, y_hat):
    return abs(y - y_hat)


y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))


def calc_se(y, y_hat):
    return (y - y_hat) ** 2


y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))


def factorial(x):
    if x > 0:
        return x * factorial(x - 1)
    else:
        return 1


def approx_cos(x, n):
    answer = 0
    for i in range(n + 1):
        answer += (-1) ** i * (x ** (2 * i) / factorial(2 * i))
    return answer


assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))


def approx_sin(x, n):
    answer = 0
    for i in range(n + 1):
        answer += (-1) ** i * (x ** (2 * i + 1) / factorial(2 * i + 1))
    return answer


assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))


def approx_sinh(x, n):
    answer = 0
    for i in range(n + 1):
        answer += (x ** (2 * i + 1) / factorial(2 * i + 1))
    return answer


assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))

def approx_cosh(x, n):
    answer = 0
    for i in range(n + 1):
        answer += (x ** (2 * i) / factorial(2 * i))
    return answer


assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))

