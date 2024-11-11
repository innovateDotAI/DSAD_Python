'''
Given 3 numbers {1, 3, 5}, The task is to tell the total number of ways we can form a number N using 
the sum of the given three numbers. (allowing repetitions and different arrangements).


The total number of ways to form 6 is: 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1
'''

def state(n,lookup={}):
    if n<0:
        return 0
    if n == 0:
        return 1
    if n not in lookup:
        lookup[n] = state(n-1)+state(n-3)+state(n-5)
    return lookup[n]
print(state(200))