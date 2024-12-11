S = '123456789'
le = 2
def getString(S,le):
    if len(S)> le:
        s1 = S[-le:]
        print(s1)
        S = S[:-le]
        getString(S,le)
    else:
        print(S)
if __name__=='__main__':
    S = '123456789'
    le = 4
    getString(S,le)
    
    