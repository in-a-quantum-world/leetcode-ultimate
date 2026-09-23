#merge intervals 
#given an array of intervals where each interval is represented by [start,end] merge all overlapping intervals 


#for every interval compare with all others to check if they overlap
#merge all overlapping intervals and mark these as visited
#O(n^2) complexity O(n) 


#sort the intervals based off of the start value of the itnerval pair 
#merge sort 

#result array - which should cotnain the first interval

#iterate over the pairs from the second interval onwards

def merge_interval(intervals):
    intervals.sort() #O(n log n), uses python's timsort 

    result = []
    result.append(intervals[0])

    for i in range(1,len(intervals) - 1):
        if intervals[i][0] <= result[len(result) - 1][1]:
            #merge
            start = min(intervals[i][0], result[len(result)-1][0])
            end = max(intervals[i][1], result[len(result)-1][1])
        
        else:
            result.append(intervals[i])


    return result  


def subarray_div_by_k(array,k):

    prefix_mod = {0:1} 
    valid = []
    running_mod

    for i in range(len(nums)):
        running_mod = (running_mod + nums[i]) % k 

        if running_mod in prefix_mod:



#given a sorted array and then rotated about a pivot
#find a desired index 

def rotated_array(arr,target):
    pass 





#max item in the sliding window of fixed length k
def sliding_window_max(arr,k):
    #arr is unsorted 

    #brute force solition 



#find two pairs, with indices i and j, i<j such that the 
def sum_to_target(nums,k):
    count = 0

    nums.sort() #O(n log n)  
    #this introduces O(n) auxiliary space 
    left = 0
    right = len(nums) - 1

    while left < right: #overall time complexity O(n)
        if nums[left] + nums[right] == target:

            count += 1

            while left < right and nums[left] == nums[left-1]: #worst case time complexity O(n)
                left += 1
            while left < right and nums[right] == nums[right+1]: #worst case time complexity O(n) 
                right -= 1

        elif nums[i] + nums[j] > target:
            right -= 1
        else:
            left += 1

    return count 

def max_substring(s):

    
        
        





    


