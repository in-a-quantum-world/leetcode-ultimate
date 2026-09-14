#using a backtracking method
#unfortunately the time complexity for this is O(n . n!) which is massive

#build the answer one element at a time, so eat each step you have a partial permutation and a st of elements which yu have npt yet used 
# for every unused element, chose it and then use recursion to fill in the rest of the elements.

#then do the same but the next choice should start from the same partial state
import collections

def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            print("current path is: ",path)
            result.append(path[:]) #taking the inside of whatever is in path, and then adding that to the result
            return
        
        for i in range(len(nums)):
            if used[i] == True:
                continue
            used[i] = True  #marking the current element as used, essentially choosing it 

            path.append(nums[i])
            print("path: ",path)
            backtrack() #recurses so we can end up filling the entire list 
            path.pop() #this unchooses the term we just added on, so that we can look at all the otherpossible permutations 
            used[i] = False


    backtrack()
    return result


#lc31
#next permutation is next lexicograohgically greater permuation of its integer 
#this is an inefficient solution since you are checking if the itme is already in the final reuslt
#which it will be if there are duplicate numbers anyway.
def next_permutation():
    
        n = len(nums)
        used = [False] * n #stores whether each item was used in permutation or not, then undoes this 
        sequence = []
        final = []

        def permute():

            if len(sequence) == len(nums):
                if sequence[:] not in final:
                    final.append(sequence[:])
                return 

            for i in range(n):
                if used[i] == True:
                    continue 
                used[i] = True
                sequence.append(nums[i])
                permute()

                #undo everything!
                sequence.pop()
                used[i] = False
        
        permute()
        return final

#using counter to keep track of unique terms

def permuteUnique(self, nums):
        results = []

        def backtrack(comb,counter):
            if len(comb) == len(nums):
                results.append(comb[:])
                return

            for num in counter:
                if counter[num] > 0:
                    #add to current combination
                    comb.append(num)
                    counter[num] -= 1 #one less of thjat number left to use

                    backtrack(comb,counter)

                    #undoing the changes that were made since we are backtracking
                    counter[num] += 1
                    comb.pop()

        print("counter nums is: ",Counter(nums))
        backtrack([],Counter(nums))


#simple path sokution implementation of lc47
def permuteUniquePath(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(nums, path, res):
            if not nums and path not in res:
                res.append(path)
                
            for i in range(len(nums)):
                subArr = nums[:i] + nums[i+1:]
                dfs(subArr, path+[nums[i]], res)
            
        dfs(nums, [], res)
        
        return res


def permuteUnique(self, nums):
        
        results = []
        def bt(start):
            if start == len(nums):
                results.append(nums[:])
                return
            
            
            lookup = set()
            
            for i in range(start,len(nums)):
                if nums[i] not in lookup:
                    nums[start], nums[i]=  nums[i],nums[start]
                    bt(start+1)
                    nums[start], nums[i]=  nums[i],nums[start]
                    lookup.add(nums[i])
        
        bt(0)
        return results

print(permute([1,2,3]))

