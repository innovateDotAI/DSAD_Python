'''
Get febinacci number using DP
'''
def fabinacci(n,lookup={}):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n not in lookup:
        lookup[n] = fabinacci(n-1)+fabinacci(n-2)
    print(lookup)
    return lookup[n]
print(fabinacci(27))
    