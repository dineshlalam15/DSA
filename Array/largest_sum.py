"""
Maximum Sub Array Sum 
Brute Force: O(n^2), O(1) 
    Checks all the subarray's possible for the arr. 
    
"""

def brute(arr):
    #Check
    if len(arr) == 0:
        return 0
    max_sum = arr[0]
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

def max_subarr_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum = arr[0]
    curr_sum = 0
    for element in arr:
        curr_sum += element
        
        if max_sum < curr_sum: 
            curr_sum = 0
        
arr = [-12,3,-8,-17,-1,2,3]
print(brute(arr))
    