
#finding all valid combinations containing k numbers of all numbers between 1 and n
def combinations(n,k):
    result = []

    sequence = []

    def backtrack(start):
        if len(sequence) == k:
            
            result.append(sequence[:]) #appends contents of sequence to the result, as opposed to the entire list 
            return 
        
        for i in range(1,n+1):
            path.append(i)
            backtrack(i+1)
            path.pop()

        return
    
    backtrack(1)
    return result


#lc39, find all lists of unique combinations of candidates
#wjere the chosen numbers sum to target
#combinations can be in any order and you can choose as many of each elemnt

#CAREFU - in backtracking, pt, used[], remaining are states that you must restre back to nromal after recursing 

def lc39(candidates,target):
    candidates.sort()
    path = []
    result = []

    def backtrack(start,remaining):
        if remaining == 0:
            result.append(path[:])
            return
        
        path.append(candidates[i])
        backtrack(i,remaining - candidates[i])
        path.pop()
    

    backtrack(0,target)
    return result

if __name__ == '__main__':
    print(combinations(4,3))