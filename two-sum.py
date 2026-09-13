
##Q1- find a subarray of integers where the sum of integers is equal to d, and the length of the subarray is equal to m



def q1(s,d,m):
    count = 0

    #starting at index 1, all m length windows until you start at index len(s)-m
    for i in range(1,len(s)-m+1):
        window_sum = sum(s[i:i+m+1])
        if window_sum == d:
            count += 1
    
    return count 

def q1_method2(s,d,m):
    count = 0
    #finding initial window 
    winodw_sum = sum(s[:m]) #sums all terms from index 0 to m includisve 
    if window_sum == d:
        count += 1

    #starting at index 1, all m length windows until you start at index len(s)-m
    for i in range(1,len(s)-m+1):
        #do not recalculate the window length from scratch each time, just add new term and remove old term
        window_sum += s[i+m-1] - s[i-1]
        if window_sum == d:
            count += 1


#question 2 - sliding window, can you find a subarray of any length which is equal to n?
def q2(s,n):
    #variable size sliding window
    #window will grow on the right and shrink on the left 
    left = 0
    window_sum = 0
    for right in range(len(s)):
        window_sum += s[right] #adding on the current term which is at the right pointer 
        while left <= right and window_sum < target:
            window_sum -= s[left] #drop the term which is leftmost

            left += 1 #increment the left pointer by 1 each time 
            if window_sum == n:
                count += 1
    
    return count 

#pairs - count the number of pairs of integers with exactly the difference k 
#O(n) time, O(n) space 
def pairs(s,k):
    count = 0
    s.sort()

    left = 0

    for left in range(0,len(s)-1):
        for right in range(left,len(s)):
            diff = abs(s[right]- s[left])
            if diff == k:
                count += 1
                right += 1  # moves onto the next item so grows the window size 
            elif diff < k:
                right += 1 #next term could provide a large enough difference 
            else:
                left += 1 #difference is too large, increase the left pointer to hopefully get smaller difference 
    

    return count 

def pairs_more_efficient(s,k):
    s.sort()
    count = 0
    left = 0
    right = 0

    #not using nested loop, instead two pointers in the same firection

    while right < len(s):
        diff = s[right] - s[left]
        if diff == k:
            count += 1

# 3 arrays a b c of different sizes, find the number of distinct triplets
# where each triplet term is a member of eachr espective set
# that satisfy the critera p <= q and q >= r

def triple_sum(a,b,c):
    a=sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))



    #long winded way
    cond2 =False
    cond1 =False

    triplets = []

    for p in a:
        cond2 =False
        cond1 =False
        for q in b:
            
            for r in c:
                if r <=q and p <= q:
                    triplets.append([p,q,r])

    return len(triplets)


#time complexity of the initial sort is O(n log n)
#time complexity of the actual 
#outer scan runs for |b| times and the inner while loop is not actually nested
#since pointer a only ever moves forward and stops at len(a) and same for pointer c
#so the total number of scans is |a| + |b| + |c| = n (as n represents size of dataset)

#so dominating time complexity is O(n log n)
def triple_sum_pointers(a,b,c):

    count = 0

    pointer_a = 0
    pointer_b = 0
    pointer_c = 0

    #deduplicating the arrays first as this returns a sorted list 
    #as triplets hve to be distinct, you need to make sure all the elements in each array is distinct
    #so use arr = sorted(set(arr)) to do so 

    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c) )
    

    for q in b:
        #check the pointer in range first and then check that the item is less than q
        while pointer_a < len(a) and a[pointer_a] <= q:
            pointer_a += 1
        while pointer_c < len(c) and c[pointer_c] <= q:
            pointer_c += 1
        
        count += pointer_a * pointer_c
        print("count so far: ",count)

    return count



if __name__ == '__main__':
    m = 2
    d = 4
    s = [1,2,3,4,5,6,7]
    q1(s,d,m)


    s = [1,2,3,4,2]
    k = 1
    print(pairs(s,k))
    print("done")

    a= [1,3,5]
    b = [2,3]
    c = [2,3]

    print(triple_sum_pointers(a,b,c))