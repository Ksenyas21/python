import math
def double_fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * double_fact(number - 2)


def func(n):
    if n == 1:
        return 1
    else:
        return math.sqrt(n + func(n - 1))
n = float(input('n=', ))
m = float(input('m=', ))
s = func(n) / double_fact(m)
print("S=", s)

