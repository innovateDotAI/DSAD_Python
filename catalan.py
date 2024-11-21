'''
Program for nth Catalan Number

Catalan numbers are defined as a mathematical sequence that consists of positive integers, 
which can be used to find the number of possibilities of various combinations. 

The nth term in the sequence denoted Cn, is found in the following formula: 
(2n)!/((n+1)!n!)
The first few Catalan numbers for n = 0, 1, 2, 3, … are : 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …  
'''
def catalan(n,lookup={}):
    if n==0 or n==1:
        return 1
    if n not in lookup:
        lookup[n] = (4*n-2)/(n+1)*catalan(n-1)
    return lookup[n]
if __name__=="__main__":
    print(catalan(100))