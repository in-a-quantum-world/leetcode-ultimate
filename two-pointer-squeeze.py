def two_pointer_squeeze(nums,target):
    nums.sort()
    low = 0
    high = len(nums) - 1

    valid_pairs = []

    for i in range(len(nums)):
        while low < high:
            s = nums[low] + nums[high]
            if s == target:
                valid_pairs.append([nums[low],nums[high]])
                #here squeeze the pointers so increment low and decrement high
                high -=1
                low += 1

                while low < high and nums[low] == nums[low-1]: #to prevent teh case that the low pointer previously and after incrementation is pointing to the same value
                    low += 1
                while low < high and nums[high] == nums[high+1]: #prevent high pointer from pointing to same value again, so decrement it
                    high -= 1
            
            elif s < target:
                low += 1
            else:
                high -= 1

    return valid_pairs 

def two_pointer_squeeze_skeleton(nums, target):
    nums.sort()
    low= 0
    high = len(nums) - 1

    count = 0

    while low < high:
        s = nums[low]+nums[high]
        if s == target:
            count += 1
            low += 1
            high -= 1

            while low < high and nums[low] == nums[low+1]:
                low += 1
            while low < high and nums[high] == nums[high-1]:
                high -= 1
            
        elif target < s:
            low += 1
        else:
            high -= 1

    return count 


def pairs_sum_less_than_target(nums,target):

    nums.sort()
    low = 0
    high = len(nums) - 1

    valid = []
    count = 0

    for i in range(len(nums)):
        if nums[low] + nums[high] < target:
            valid.append([nums[low],nums[high]])
            #squeeze
            #you know that low can be paired with high, high-1, high-2,... 
            #so this can be added to the total number of valid sum < target
            count += high - low
            low += 1

        else:
            high -= 1
    

    return valid

def closest_pair_sum_to_target(nums,target):
    nums.sort()
    low = 0
    high = len(nums)-1

    best = float(inf)

    while low < high:
        s = nums[low] + nums[high]
        best = min(best,abs(s-target))
        if s < target:
            low += 1
        elif s > target:
            high -= 1
        else:
            return best
    return best 

if __name__ == '__main__':
    nums = [1,4,3,-2,6,0,5,-8,6]
    target = 4
    print(two_pointer_squeeze(nums,target))



