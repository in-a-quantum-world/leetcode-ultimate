

#given a string reurn true if it reads the same forwards and backwards after ignoring 
#everything that is not  a letter or diigt, and ignoring the case 

def is_pallindrome(word):
    word = word.lower()
    

    new_word = ""
    for i in word:
        if i.isalnum() == True and i != " ":
            new_word += i 
    print(new_word)


    start = 0
    end = len(new_word) - 1

    
    for i in range(len(new_word)//2):
        if new_word[start] != new_word[end]:
            return False
        start +=1
        end -= 1
    
    return True
        
#lc 647, uses O(n^2) time comexplity
#linear space complexity
def pallindromic_substrings(s):

    #expand from the centre
    n = len(s)
    count = 0

    for centre in range(2*n - 1):
        left = centre / 2  
        right = left + centre%2

        while left >= 0  and right < n and s[right] == s[left]: #checks if there are anyu more sols with same centre 
            #but first adds 1 to count since we found one to enter the while loop
            count += 1
            right += 1
            left -=1
    
    
    return count

#now for a dynamic programming approach!
def pallindromic_substr_dp(s):
    #initialises variables n and count
    n = len(s)
    count = 0

    #create a 2d boolean array dp of size n times n where dp[i][j] indicates whether the substring from i to j is pallindrome
    dp = [[False] *n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True #each individual element is a pallindrome after all so all diagonal elements ar true
        count += 1 

    for i in range(n-1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        count += 1 if dp[i][i + 1] else 0
    
    #iterates over all substrings of length 3 to n, checking if each substr is a pallindrome
    #using dyamic programming and then updating answer accordingly 
    for length in range(3,n+1):
        for i in range(n-length +1):
            j = i + length - 1
            dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
            if dp[i][j] == True:
                count += 1 if dp[i][j] else 0
    
    return count
            
    



#manacher algorithm
#do not think i would havbe thought of this myself!
def manacher_pallindrome_substr(s):
    #manacher's algorithm
    #linear timie and space complexity

    n = len(s)
    #creating a new string by inserting a hashtag between each char
    #of original string to consider boith
    #odd and veen length pallindromes at once

    t = "#"

    for i in s:
        t += i + "#"
    
    n = len(t) #should be double length of s, plus 1

    dp = [0] * n #creating an array of 0s, length n
    centre = 0 #centre of current longest pallindrome
    right = 0 #pointer to track rightmost char
    count = 0

    #iterate over the left pointer  
    for i in range(n):
        mirror = 2*centre - i
        if i < right:
            dp[i] = min(right - i, dp[mirror])
        #attempt to expand pallindrome centred at i
        while a < n and b >= 0 and t[a] == t[b]:
            dp[i] += 1
            a += 1
            b -= 1
        #if pallindrome centrerd at i expands past the right
        #then the centre needs to be adjusted
        #and the right
        if i + dp[i] > right:
            centre = i
            right = i + dp[i]
        
        #cthen count all pallindromes found at index i
        count += (dp[i]+1) // 2
    return count

if __name__== '__main__':
    print(is_pallindrome("RA3d 3ar"))