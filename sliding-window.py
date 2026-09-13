
import math 
#sliding window - find the longest substring with k unique characters  in a given string 
#print longest substring possible that has exactly M unique characters 

def longest_substring(word,k):
    max_length = -10000000000000000



    window_substr = word[:k]
    if len(window_substr) == len(set(window_substr)):
        max_length = len(window_substr)

    repeated = len(word) - len(set(word))

    for i in range(0,len(word) - repeated)




if __name__ == '__main__':
    print(longest_substring("aabbcc",1))