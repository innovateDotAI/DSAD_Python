S = '123456789'
le = 2
def getString(S,le,ss):
    if len(S)> le:
        s1 = S[-le:]
        print(s1)
        ss.append(s1)
        S = S[:-le]
        getString(S,le,ss)
    else:
        print(S)
        ss.append(S)
def sumString(ss,sl):
    for t in range(len(ss)):
        sum=0
        try:
            sum = int(ss[t+1]) + int(ss[t+2])
            tup = (sum,int(ss[t]))
            sl.append(tup)
        except:
            pass
        
if __name__=='__main__':
    S = '123456789'
    le = 2
    ss=[]
    getString(S,le,ss)
    print(ss)
    sl=[]
    sumString(ss,sl)
    print(sl)
    
    