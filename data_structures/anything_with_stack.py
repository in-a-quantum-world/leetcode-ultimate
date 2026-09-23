

#lc20 - valid parentheses

def isValid(s):

    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
        
        else:
            if stack == []:
                return False #stack is empty and the current term is a closed bracket so not correct
            
            #we can pop the top of the stack now to check what the previous term was
            top = stack.pop()
            if top == "(" and s[i] != ")":
                return False
            if top == "[" and s[i] != "]":
                return False
            if top == "{" and s[i] != "}":
                return False

    #finished iterating through all chars in the string
    #stack should be empty to indicate all open brackets were popped form thje stack because you found
    #'the corresponding close bracket

    if len(stack) == 0:
        return True 
    else:
        return False 


def smallest_divisor(nums,threshold):

    #use a binary search approach to find the smallest divisor whichis feasible, given the threshold

    #create a function whichh can check if that item is a valid divisor for all terms, given the threshold.

    def condition(divisor):
        return sum