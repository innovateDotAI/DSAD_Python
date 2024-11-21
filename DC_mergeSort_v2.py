'''
Use divide and conquer to sort given array using merge sort
'''
def mc(arr,left,mid,right):
    LEFT = left
    print(f"Left={left}, Mid={mid}, Right={right}")
    #Get value in temp array
    L = [0]*(mid-left+1)
    R = [0]*(right-mid)
    i = 0
    j = 0
    while i < len(L):
        L[i] = arr[left]
        i+=1
        left+=1
    while j < len(R):
        print(f'mid={mid},right={right}')
        R[j] = arr[mid+1]
        j+=1
        mid+=1
    i= 0
    j = 0
    k = LEFT
    print(f"L = {L}, R = {R}")
    while i < min(len(L),len(R)) and j < min(len(L),len(R)):
        print(f" start of loop while i={i} and j={j} len(L) = {len(L)}, len(R)={len(R)},k={k}")
        if L[i] < R[j]:
            arr[k] = L[i]
            i+=1
            k+=1
        elif L[i] > R[j]:
            arr[k] = R[j]
            j+=1
            k+=1
        else:
            arr[i] = L[i]
            arr[i+1] = R[j]
            i+=1
            j+=1
            k+=2
        print(f" end of loop of while i={i} and j={j} len(L) = {len(L)}, len(R)={len(R)},k={k}")
    print(f" after while i={i},j={j},k={k}")
    if i >= len(L):
        while j<len(R):
            print(f"R[{j}]={R[j]}")
            arr[k] = R[j]
            j+=1
            k+=1
    if j >= len(R):
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
    print(arr)
def md(arr,left,right):
    if left < right:
        mid = (left+right) // 2
        md(arr,left,mid)
        md(arr,mid+1,right)
        mc(arr,left,mid,right)


if __name__=="__main__":  
    
    arr = [10,15,5,10,25,4,-10,30]
    print(f"before sorting = {arr}")
    md(arr,0,len(arr)-1)
    print(f"After Sorting is {arr}")

