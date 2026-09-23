

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
        
#inefficient solution since it checks the height between all possible ones 
def container_max_area(height):
    max_area = 0
    start = 0
    end = 0

    for start in range(0,len(height)-1):
        for end in range(start,len(height)):
            area = (end - start) * min(height[start],height[end])
            if area >= max_area and end < len(height):
                max_area = area
            

    return max_area
    

#new solution to move whichever pointer is at the shorter line
#O(n) time complexity
def better_container(height):
    max_area = 0
    start = 0
    end = len(height) - 1

    while start < end:
        max_area = max(max_area, (end-start)* min(height[start],height[end]))
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return max_area

def squares_of_sorted_array(arr):
    pass

def boats(people,limit):
    people.sort(reverse=True)
    groups = []

    start = 0
    end = len(people) - 1

    while start <= end and end < len(people):
        
        if start != end and people[start] + people[end] <= limit:
            groups.append([people[start],people[end]])
            end -= 1
        else:
            groups.append(people[start])
        start += 1
            
    return groups


#lc42 trapping rain water
#using two preifx-max arrays, O(n) time and O(n) space
def trap(height):

    water = []
    max_left = [0] * n
    min_height = [0] * n

    for i in range(1,len(height)):
        max_left[i] = max(max_left[i-1], height[i])
    
    max_right[len(height) - 1] = height[len(height) - 1]
    for i in range(len(height) - 2, - 2, - 1):
        max_right[i] = max(max_right[i+1], height[i])

    total = 0

    for i in range(len(height)):
        total += min(max_left[i], max_right[i]) - height[i]

    return total

#grouping into buckets based off of mod k 
def divisibleSumPairs(n,k,arr):
    count = [0] * k 
    for x in arr:
        count[x%k] += 1

    pairs = count[0] * (count[0] - 1) // 2
    if k % 2 == 0:
        c = count[k//2]
        pairs += c * (c-1) // 2

    for r in range(1, (k + 1) // 2):                 # r < k - r, each bucket pair once
        pairs += count[r] * count[k - r]
    return pairs


def divsumpairs(n,k,arr):
    count = 0
    arr.sort()

    hashmap = {}

    for i in range(n):
        mod_value = arr[i] % k 
        desired = (k - mod_value) % k 

        if desired in hashmap:
            count += hashmap.get(desired,0)
        
        if mod_value in hashmap:
            hashmap[mod_value] = hashmap.get(mod_value,0) + 1
        
        else:
            hashmap[mod_value] = 1
    

    return count


    



#lc2517 - maximum tastiness of candy basket
#maximise the min, or minimise the max is usually indicative of binary search!
def maximumTastiness(price,k):




if __name__== '__main__':
    print(is_pallindrome("RA3d 3ar"))
    print(better_container([1,8,6,2,5,4,8,3,7]))

    people = [3,2,1,2]
    limit = 3
    print(boats(people,limit))



 