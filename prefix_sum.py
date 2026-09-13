#lc 560
#version which should work for negative numbers too 
def subarray_sum_to_target_neg(nums,target)
    #prefix sum keeps a running total of the sum of all items in the list
    #you can subtract these prefices to find the sum between a start and end pointer

    #start with a dictionary where you store how manu times you have seen a 
    seen = {0:1} #prefix sum of 0 exists before checking anything
    prefix = 0
    count = 0
    for x in nums:
        prefix += x 
        count += seen.get(prefix - k,0) #there may be several earlier positions with that prefix 
        #and each one of these is a different subarray
        seen[prefix] = seen.get(prefix,0) + 1 #adding 1 to what we have already seen
    
    return count