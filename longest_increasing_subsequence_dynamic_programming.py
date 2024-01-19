#s = [3,4,-1,0,6,2,3]
s = [10,9,2,5,3,7,101,18]
l = len(s)
print(l)
LIS_arr = [1]*l # Initialization of subsequence for each digit
print(LIS_arr)
trace_arr = [-1]*l # Index value of sequeunce. -1 means not updated
print(trace_arr)
for i in list(range(1,len(s))):
    for j in list(range(i)):
        if s[j]< s[i]:
            LIS_arr[i] = max(LIS_arr[j]+1,LIS_arr[i])
            trace_arr[i] = j
        print("i=",i,"j=",j)
print("Maximum length of increasing subsequence=",max(LIS_arr))
print("LIS_arr=",LIS_arr)
print("trace_arr=",trace_arr)
t = LIS_arr.index(max(LIS_arr))
print("Max initial valu=(t):",t)
seq = [None]*max(LIS_arr)
print(seq)
indx = max(LIS_arr)
while trace_arr[t] !=-1:
    indx = indx-1
    seq[indx]=s[t]
    t = trace_arr[t]
seq[indx-1]=s[t]
print("Valid increasing order subsequence=",seq)
    

