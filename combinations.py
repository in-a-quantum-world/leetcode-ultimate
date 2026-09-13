
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






if __name__ == '__main__':
    print(combinations(4,3))