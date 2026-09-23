#using a backtracking method
#unfortunately the time complexity for this is O(n . n!) which is massive

#build the answer one element at a time, so eat each step you have a partial permutation and a st of elements which yu have npt yet used 
# for every unused element, chose it and then use recursion to fill in the rest of the elements.

#then do the same but the next choice should start from the same partial state

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


print(permute([1,2,3]))

