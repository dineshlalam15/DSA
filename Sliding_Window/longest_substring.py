"""
Exists or not? can check using a Dictionary/HashMap. 
LeetCode URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

def longest_substring(s: str): 
    if len(s) == 0:
        return 0
    
    max_len = 0
    i = 0
    frequencies = {}
    for j in range(len(s)):
        """
        while under a for but still O(N) as max iterations possble is O(2N),
        when j reaches end and i also reaches end. 
        """
        while s[j] in frequencies and i <= j: 
            frequencies.pop(s[i])
            i+=1
        max_len = max(max_len, j-i+1)
        frequencies[s[j]] = 1
    return max_len


def longest_substring_optimal(s: str): 
    #Check: 
    if len(s) == 0:
        return 0
    element_exists = {}
    max_len = 0
    i = 0 #left pointer
    for j in len(s): #right pointer
        if s[j] in element_exists and element_exists[s[j]] >= i:
            i = element_exists[s[j]] + 1
        
        max_len = max(max_len, j-i+1)
        element_exists[s[j]] = j #Storing the position (index) of the element. 
        """
        Instead of keeping it as 1, we are storing the index of the element.
        So that, we needn't iterate (while loop) to check until the character arrives and pop. 
        We can directly see if element is already there & if present, we can move our i pointer directly to that position. 
        """


s = "abccbaapacb"
print(longest_substring(s))