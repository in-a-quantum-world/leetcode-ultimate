

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
        


if __name__== '__main__':
    print(is_pallindrome("RA3d 3ar"))