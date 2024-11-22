'''
Subset Sum Problem

Given an array arr[] of non-negative integers and a value sum, the task is to 
check if there is a subset of the given array whose sum is equal to the given sum.
'''
import numpy as np
def isSubset(arr,n,sum,lookup):
    if sum == 0 and n>=0:
        return True
    if sum !=0 and n==0:
        return False
    if sum <0 and n>0:
        return False
    if lookup[sum-1][n-1] is None:
        lookup[sum-1][n-1]= (isSubset(arr,n-1,sum-arr[n-1],lookup) or isSubset(arr,n-1,sum,lookup))
    return lookup[sum-1][n-1]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum = 30
    n = len(arr)
    lookup = np.empty(shape=(sum,n),dtype='object')
    print(isSubset(arr,n,sum,lookup))
    print(lookup)