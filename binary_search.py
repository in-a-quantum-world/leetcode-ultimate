

#finding an item in an array that was sorted and then pivoted about a point

def rotated_search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        #locate pivot
        #locating pivot is linear?? first term whch is smaller so breaks desc order
        pivot = 0 #pivot initialised at index 0
        pre_pivot = 0

        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i
                pre_pivot = i-1
        
        print(pivot,pre_pivot)

        #then do binary search depending on which side of pivot it is 
        #binary search is O(log n)

        if target <= nums[pre_pivot] and target >= nums[0]:
            print("bhefore pivot")
            #binary search on this sublist
            sublist = nums[0:pre_pivot]
            left = 0
            right = pre_pivot

            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1




        elif target >= nums[pivot] and target <= nums[len(nums)-1]:
            print("after pivotr")
            #binary search on this sublist
            sublist = nums[pivot:len(nums)-1]
            left = pivot
            right = len(nums) - 1

            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    left = mid + 1   
                else:
                    right = mid - 1

        
        
        return -1


#alternative and better solution to finding te pivot in the array
#so we can still get O(log n) time complexity for the solution


def better_rotated_search(nums,target):

    n = len(nums)
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1

    
    #separate doing binary search over the right and left sublists

    def bin_search(left_bound,right_bound,target):
        left = left_bound
        right = right_bound

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    #do bin search opver elements on the pivot element's left
    answer = bin_search(0,left-1,target)
    if answer != -1:
        return answer
    
    bin_search(left,len(nums)-1,target)
    
#lc81 search in rotated sorted array II
#just returns whether it is in array or not,m exact same
#just another opportunity to practife ig 