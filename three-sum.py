
# given=n an integer array nums, return all the triplet 
# [nums[i],nums[j],nums[k]] such that i != j != k
# and the three terms sum to 0
# no duplicate triplets allowed!

#this solution has complexity O(n^2)
def three_sum(nums):
    nums.sort()
    triplets = []

    #two pointer squeeze technique - iterate i through the array and then use two other pointers whose items sum to 0

    for i in range(len(nums)):
        #check if the value at the first index is positive or negative to determine whether there are actually any numbers fit for a sol
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            #this will generate duplicate solutions
            #so just continue
            continue

        low= i+1
        high = n-1
        for j in range(i,len(nums)):
            new_nums = nums[i+1:]  
            if nums[i] + nums[low] + nums[high] == 0:
                triplets.append([nums[i],nums[low],nums[high]])
                #then squeeze low and high
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low-1]:
                    low += 1
                while low < high and nums[high] == nums[high+1]:
                    high -= 1
            
            elif sum < 0:
                low += 1
            else:
                high -= 1
                

    return triplets

def three_sum_2(nums):

    nums.sort()
    triplets = []
    low = 0
    high = len(nums) - 1

    for i in range(len(nums)-2):
        #using two pointer squeeze method whilst fixing the first pointer (chosen element for triplet)
        if nums[i] > 0:
            break
            #this means that the smallest number itself is greater than zero, so impossible for sum of three to be equal to zero
        
        elif i>0 and nums[i] == nums[i+1]: #skips duplicate first elements
            continue
        
        low = i+1
        high = len(nums) - 1

        while low < high:
            if nums[high] + nums[low] + nums[i] == 0:
                triplets.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1

                while low < high and nums[low] == nums[low+1]: #current low is same as what next low would be, increment 
                    low += 1
                while low < high and nums[high] == nums[high-1]: #currnt high is same as what next high would be so adjust
                    high -= 1
                
            elif nums[high] + nums[low] > -nums[i]:
                high -= 1
            else:
                low += 1
    
    return triplets


if __name__ == '__main__':
    m = 2
    d = 4
    s = [1,2,3,4,5,6,7]
    q1(s,d,m)


    s = [1,2,3,4,2]
    k = 1
    print(pairs(s,k))
    print("done")

    a= [1,3,5]
    b = [2,3]
    c = [2,3]

    print(triple_sum_pointers(a,b,c))