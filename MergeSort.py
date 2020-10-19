import numpy as np

def merge(A,p,q,r):
    print(A[p:q], A[q+1:r])

    n1 = q - p + 1
    n2 = r - q
    L = np.empty(n1+1)
    R = np.empty(n2+1)

    for i in range (0,n1):
        L[i] = A[p + i]
    L[n1] = float("inf")

    for j in range (0,n2):
        R[j] = A[q + j + 1]
    R[n2] = float("inf")

    i=0
    j=0

    for k in range (p,r+1):
        if(L[i]<=R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return A

def mergeSort(A,p,r):
    for x in range (p,r+1):
        print(A[x], end=" ")
    print(" ")
    if p < r:
        q = int((p + r) / 2)
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)


array1 = np.array([12,3,3412,441,2,12,3123,1,231,23,122,3,67])
print(array1)
array2 = mergeSort(array1,0,12)
print(array1)