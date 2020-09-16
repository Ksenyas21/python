import numpy as np

def isSortedReverse():
    for j in range(len(a)):
        if all(a[:,j]==sorted(a[:,j], reverse=True)):
            print(j,end=' ')
        else:
            j=j+1
n = int(input('n= ',))
a = np.random.randint(0, 9, size = (n, n))
# a = np.array([[12,6,12,7,1,7],
#               [11,6,9,7,1,6],
#               [8,5,8,7,4,5],
#               [4,2,6,5,3,4],
#               [3,2,5,4,5,3],
#               [1,1,4,3,2,2]])
print('Matrix = ',a)
print("Vector")
isSortedReverse()
