print("Enter the number:")
n = int(input())
def func(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return func(n-2)+func(n-1)
print("Fabinaci value :",func(n))