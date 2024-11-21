'''
Use divide and conquer to perfrom quick search

'''

def divid(arr,p,l,r,c=0):
    print(f" Enter p={p},l={l},r={r},arr={arr[p:r+1]}")
    R = r
    if len(arr[p:r+1])==2:
        if arr[p]>arr[r]:
            temp1 = arr[r]
            arr[r] = arr[p]
            arr[p] = temp1
            return
    elif len(arr[p:r+1])<=1:
        return
        
    else:
        while arr[l] < arr[p]:
            l+=1
        while arr[r] > arr[p]:
            r-=1
        print(f"l={l},r={r},arr[{p}]={arr[p]},arr[{l}]={arr[l]},arr[{r}]={arr[r]}")
        if r > l:
            temp = arr[r]
            arr[r] = arr[l]
            arr[l] = temp
            divid(arr,p,l,r)
        if r<l:
            print(f"Here1 r={r},l={l},p={p}")
            temp = arr[r]
            arr[r] = arr[p]
            arr[p] = temp
            temp_r = r
            r = p
            p = temp_r
            print(f"Here2 r={r},l={l},p={p}")     
            #print("Left  Side")
            #divid(arr,r,r+1,p-1)
            print("right side")
            divid(arr,p+1,p+2,R)


if __name__=="__main__":
    arr = [10,5,25,3,35,1,8,67,33]
    print(f"Before sorting: {arr}")
    val = divid(arr,0,1,len(arr)-1)
    print(val)
    print(f"After sorting : {arr}")
        
        