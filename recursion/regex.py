
#lc 10, regex matching with '.' and '*' symbls allowed
def match(text,pattern):
    

    #two pointrers  into string s 
    #point
    #the banse case is thsta the pattern is fully consumed
    #so match only if text is also fully consumed
    if not pattern:
            return not text

        pattern = p
        text = s

        #checking if the first cgaracter of text matches the first char of pattern
        #the period cna mastch anything otherwise it must be the sae letter

        first_match = bool(text) and pattern[0] in (text[0],'.')

        #then check if the next pattern char is a star
        has_star = len(pattern)> 1 and pattern[1] == "*"

        if has_star == True:
            #zero or more of the preceding element permitted
            #either we treat x* as matching zero chatavyers amd tjem ski[p this pattern in the text
            #keeping the text unchanged
            skip = self.isMatch(text,pattern[2:])

            #orwe treat this as matching one or more characters
            #meaning we take one char from tjhe text and kep the pattern
            consume = first_match and self.isMatch(text[1:],pattern)
            return skip or consume
        else:

            #there is no star meaning you can just match one chgaraccter amnd move forward
            #in bot the string and the pattern
            return first_match and self.isMatch(text[1:],pattern[1:])      


    
#lc44 wildcard matching
#with regex again