
import math 


#COME BACK TO THIS ONE
#sliding window - find the longest substring with k unique characters  in a given string 
#print longest substring possible that has exactly M unique characters 
#variable window with state 
def longest_substring(word,k):
    max_length = -10000000000000000
    counts = {} #number of occurences within a specific window

    left = 0
    best = 0

    for right, ch in enumerate(word):
        counts[ch] = counts.get(ch,0) + 1

        while len(counts) > k:
            out = word[left]
            counts[out] -= 1
            if counts[out] == 0:
                del counts[out]
            left += 1
        if len(counts) == k:
            best = max(best,right - left + 1)

    return best 

def subarray_sum_to_target(nums,target):

    left = 0
    right = len(nums) - 1

    subarrays = []

    prefix_sum = {0:0}
    cumulative_sum = 0

    for i in range(len(nums)):
        cumulative_sum += nums[i]
        while left < right:
            if cumulative_sum == target:
                subarrays.append(nums[left:right])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
                
            elif cumulative_sum < target:
                left += 1
            else:
                right += 1

#minimum size subarray sum
#given an array of positive integers num and a positive integer target, return the minmal length of a subarray whose sum is greater than or equal to target
def min_size_subarray_sum(nums,target):
    best = float('inf')
    left = 0
    window_sum= 0

    for right in range(len(nums)):
        window_sum += nums[right] #adding the right pointer term to window sum, growing it 
        while window_sum >= target: #while the window sum is too large, we can grow it 
            best = min(best,right - left + 1) #seeing which length is smaller, the current best or the current window length, since it matches the condition
            #add 1 since it is inclusive of the left and right pointers
            window_sum -= nums[left] # removing leftmost item in the hopes that the windpw sum becomes smaller 
            left += 1 # shrinking the window sum 
        
    if best != float('inf'):
        return best 
    else:
        return 0


#lc209, shortest subarray with sum >= target
def min_size_subarray_sum(nums,target):

    left = 0
    min_size = float('inf')
    count = 0
    window_sum = 0


    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target: #keep shrinking from the left hand side 
            
            current_size = end - start + 1
            if current_size < min_size:
                min_size = current_size

            window_sum -= nums[left]
            left += 1

            #no point incrementing end and keeing start the same since this just exnteds the size of the window 
            #and we are looking for min length window
            #add the number of terms between the 'end' pointer and actual end of list
                
    if min_size < float('inf'):
        return min_size
    else:
        return 0            



#subarray with sum exactly equal to target
#ONLY WORKS FOR POSITIVE ELEMENTS IN ARRAY 
def subarray_sum_to_target(nums,target):


    left = 0
    right = 0
    result = []
    window_sum = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            if window_sum == target:
                result.append(nums[left:right+1]) #remember that you have to include one index higher than last idnex!!
            
            window_sum -= nums[left]
            left += 1


    return result


def subarray_sum_to_target(nums,target):

    left = 0
    right = 0
    #both pointers start at 0, we cannot sort the list since the order of the subarray is important
    result = []
    window_sum = 0 #start with a window sum of 0

    for right in range(len(nums)):
        window_sum += nums[right] #add on new element in the sliding window
        if window_sum == target:
            result.append(nums[left:right])
        
        #remove the current leftmost term in the slkiding window
        window_sum -= nums[left]

        #increment left pointer
        left += 1
    
    return result 


if __name__ == '__main__':
    print(longest_substring("aabbcc",1))

    print(subarray_sum_to_target([1,2,3,4],6))

    sub = [1,2,3,4]
    print(sub[0:3])