
#lc 10, regex matching with '.' and '*' symbls allowed
def match(text,pattern):
    

    #two pointrers  into string s 
    #point

    if not pattern:
            return not text

        pattern = p
        text = s

        #dynamic programming aproach
        memory = {} #cache the immediate resu;lts
        #which si to check if text[i:] and pattern[j:] match

        def dp(i,j):
            if (i,j) not in memory:
                if j == len(pattern):
                    ans = i == len(text)
                
                else:
                    first_match = i < len(text) and pattern[j] in {text[i],"."}

                    if j + 1 < len(pattern) and pattern[j+1] == "*":
                        ans = dp(i,j+2) or first_match and dp(i+1,j)
                    else:
                        ans = first_match and dp(i+1,j+1)


                memory[i,j] = ans

            return memory[i,j]

        return dp(0,0)


#lc44 wildcard matching
#with regex again