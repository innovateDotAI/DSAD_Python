while True:
    import numpy as np
    print("Enter the number:")
    n = int(input())
    print("n=",n)
    # Memo table initialization
    MAX = 100
    fab_table = np.ones_like(np.arange(MAX, dtype=float))*(-1)
    print(fab_table)

    def fab(n):
        if fab_table[n] != -1:
            return fab_table[n]
        else:            
            if n <=1:
                fab_table[n] = n
                return fab_table[n]
            else:
                fab_table[n] = fab(n-1)+fab(n-2)
                return fab_table[n]

            

    print("Fabinaci value=",fab(n))