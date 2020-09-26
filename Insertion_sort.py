import numpy as np

array1 = np.array([1,2,1,12,32,3,43,2,31,3,12,3,124,23])
for j in range(1, (array1.size)):
    key = array1[j]
    i = j
    while(i>=0 and key<array1[i-1]):
        array1[i] = array1[i-1]
        i-=1
    array1[i] = key
for x in array1:
    print(x)