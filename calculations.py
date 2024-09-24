def count_pairs(A):
    freq = {} #Taking freq as empty dictionary 
    
    #count the frequency of each Element
    for i in A:
        if i in freq:
            freq[i] += 1 
        else:
            freq[i] = 1 
    good_pairs = 0
    #Calculate the number of good pairs
    for count in freq.values():
        good_pairs += count * (count - 1) // 2
    
    return good_pairs
    
T = int(input("Enter TestCases Number: ")) # Read the Number of Test Cases
#process each test case
for _ in range(T):
    N = int(input("Enter Array_length:")) # Length of Array 
    A = list(map(int, input().split())) # Array Elements
    #Ouput the number of good pairs
    print(count_pairs(A))
