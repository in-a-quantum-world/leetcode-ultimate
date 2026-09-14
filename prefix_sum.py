#lc 560
#version which should work for negative numbers too 

#O(n) time and space complexity
def subarray_sum_to_target_neg(nums,target):
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

#PREFIX SUM INDICATORS!!!
#redundant work, cumulative state, instnant lookup
def prefix_sum(nums,target):

    prefix_sum_array = [0]
    #prefix sum array will be 1 item longer than original array
    #because the first term stored is always 0!

    #O(n) compelxity
    count = 0
    for num in nums:
        count += num 
        prefix_sum_array.append(count)

    
    #use hasmap to look up value in O(1)
    prefix_sum = {0:1}  #value 0 is the first in the prefix sum dict
    result = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        target_val = current_sum - target
        if target_val in prefix_sum:
            result += prefix_sum[target_val] #how many times we have seen this edesired item
            #in the array
        
        prefix_sum[current_sum] = prefix_sum.get(current_sum,0) + 1
    
    return result

#lc560
def prefix_sum2(nums,k):

    prefix_sum = {0:0}
    result = 0
    current_sum = 0

    for x in nums:
        current_sum += x 
        to_find = current_sum - k 
        if to_find in prefix_sum: 
            result += prefix_sum[to_find]
        
        #increment the value associated with key current sum
        if current_sum in prefix_sum.keys():
            prefix_sum[current_sum] += 1
        else:
            prefix_sum[current_sum] = 1

    return result


#lc523 - an inefficient solution but passes 80/103
def continuous_subarray_sum(nums,k):

    #maintains a dict of where a prefix sum was first seen when going through the array
    order = {0:-1}
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        for id in order.keys():
            if (current_sum - id) % k == 0:
                dist = i - orde[id]
                if dist >= 2:
                    return True 
            
            if current_sum not in order:
                order[current_sum] = i
            else:
                order[current_sum] += i
    
    return False

#lc 523 but with better space complexity!!
def better_cont_subarray_sum(nums,k):
    order = {0:-1}
    #try to avoid checking every single id in the order dict
    #and if the difference between the current sum and a different prefix sum is equal to a mult of k

    #start with prefix mod
    prefix_mod = 0

    for i in range(len(nums)):
        prefix_mod = (prefix_mod + nums[i]) % k 
        if prefix_mod in order:
            dist = i - order[prefix_mod]
            if dist >= 2:
                return True  

        if prefix_mod not in order:
                order[prefix_mod] = i
            else:
                order[prefix_mod] += i

    return False

#lc 525
#return max length of a contiguous subarray with equal number of 0 and 1
def contiguous_array(nums,k):

    order = {0:-1}

    rolling_sum = 0

    #use mod and store rolling mod not rolling sum
    for i in range(len(nums)):
        rolling_sum += nums[i]



if __name__ == '__main__':
    print(prefix_sum2([3,1,2,5,4],8))