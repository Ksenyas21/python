import math
def double_fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * double_fact(number - 2)
n = float(input('n=',))
m = float(input('m=',))
s = math.sqrt( n+math.sqrt((n-1)+math.sqrt(1)))/double_fact(m)
print("S=",s)