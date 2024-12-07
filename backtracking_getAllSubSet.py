'''
Print all subsets of a given Set or Array
Given an array Arr[] of size N, print all the subsets of the array.

Subset: A subset of an array is a tuple that can be obtained from 
the array by removing some (possibly all) elements of it

Example:

Input: N = 3, Arr = [1, 2, 3]
Output: {}
               {1}
               {1, 2}
               {1, 2, 3}
               {1, 3}
               {2}
               {2, 3}
               {3}
Explanation: These are all the subsets that can be 
formed from the given array, it can be proven that no other subset
exists other than the given output.
'''

def calcSubset(A, res, subset, index):
    # Add the current subset to the result list
    res.append(subset[:])
    print(f'res={res}')

    # Generate subsets by recursively including and excluding elements
    for i in range(index, len(A)):
        print(f' for loop value of i={i}')
        # Include the current element in the subset
        subset.append(A[i])
        print(f'subset={subset}')

        # Recursively generate subsets with the current element included
        print(f'Calling function calcSubset(A={A}, subset={subset}, index= {i + 1})')
        calcSubset(A, res, subset, i + 1)

        # Exclude the current element from the subset (backtracking)
        print(f"Pop out value from subset = {subset} is {subset.pop()}")
        print(f'calcSubset is finished for  for calcSubset(A={A}, subset={subset}, index= {i + 1})')
        


def subsets(A):
    subset = []
    res = []
    index = 0
    print(f'Calling function calcSubset(A={A}, res={res}, subset={subset}, index={index})')
    calcSubset(A, res, subset, index)
    print(f'outcome of calcSubset({A, res, subset, index}) is {res}')
    return res


# Driver code
if __name__ == "__main__":
    array = [1, 2, 3,4,5,6]
    res = subsets(array)

    # # Print the generated subsets
    # for subset in res:
    #     print(*subset)