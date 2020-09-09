#Долган Ксенія
#Варіант 7

import math
x = float(input('x=',))
a = float(input('a=',))
e = float(input('e=',))
k = 1
s = math.sin(x)**k+math.cos(a)**k/math.factorial(1*k-1)
if x >= 0 and a >= 0:
    while math.fabs(s) < e:
        s += s
        k = k+1

print('summa =',s , 'amount arg = ', k)
