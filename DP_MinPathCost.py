'''
Min Cost Path | DP-6

Given a cost matrix cost[][] and a position (M, N) in cost[][], write a function that returns 
cost of minimum cost path to reach (M, N) from (0, 0). Each cell of the matrix represents a cost
to traverse through that cell. The total cost of a path to reach (M, N) is the sum of all the costs 
on that path (including both source and destination). You can only traverse down, right and diagonally 
lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1), and (i+1, j+1) 
can be traversed. 
'''
import numpy as np
def  minCost(arr,sp,m,n,cost):
    if m < 0 or n < 0:
        return 99999999
    if m == sp[0] and n == sp[1]:
        return arr[sp[0]][sp[1]]
    if cost[m][n] is None:
        cost[m][n] = min(minCost(arr,sp,m,n-1,cost),minCost(arr,sp,m-1,n,cost),minCost(arr,sp,m-1,n-1,cost))+ arr[m][n]
    print(cost)
    return cost[m][n]

if __name__=="__main__":
    arr = np.array([[1,2,3],[4,8,2],[1,5,3]])
    cost = np.empty(shape=(3,3),dtype='object')
    sp = (0,0)
    m=2
    n=2
    print(minCost(arr,sp,m,n,cost))