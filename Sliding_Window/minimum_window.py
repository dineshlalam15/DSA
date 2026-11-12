"""
MINIMUM WINDOW SUBSTRING: https://leetcode.com/problems/minimum-window-substring/description/

BRUTE FORCE: 
1. Find every possible substring. 
2. Compare frequencies (as duplicates also needs to be considered).
3. Check all the strings having chars of 't' and return the smallest one. 

OPTIMAL WAY: 
1. Two Pointers [left, right].
2. Sliding Window. 
"""

class Solution(object):
    
    def possible_sub_strings(self, s: str): 
        sub_strings = set()
        for i in range(len(s)):
            curr_str = ""
            for j in range(i,len(s)):
                curr_str+= s[j]
                sub_strings.add(curr_str)
        return sub_strings
    
    def calc_frequency(self, s):
        count = {}
        for element in s:
            if element in count: 
                count[element] = count[element]+1
            else:
                count[element] = 1
        return count
    
    def check_count(self, dict1, dict2): 
        for key,value in dict2.items(): 
            if dict1.get(key,0) < value:
                return False
        return True
    
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #Check 1: 
        if len(t) > len(s): 
            return ""
        #Check 2: 
        if t in s:
            return t
        #Check 3: 
        frequency_t = self.calc_frequency(t)
        frequency_s = self.calc_frequency(s)
        for key,value in frequency_t.items(): 
            if frequency_s.get(key,0) < value: 
                return "" 
        
        all_sub_strings = self.possible_sub_strings(s)
        ans_str = s
        for element in all_sub_strings:
            frequency_element = self.calc_frequency(element)
            if self.check_count(frequency_element,frequency_t) and len(element) < len(ans_str):
                ans_str = element   
        return ans_str
    
    
    def optimal_approach(self, s, t): 
        #Check 1: 
        if len(t) > len(s): 
            return ""
        
        #Check 2: 
        if t in s:
            return t
        
        #Check 3: 
        frequency_t = self.calc_frequency(t)
        frequency_s = self.calc_frequency(s)
        for key,value in frequency_t.items(): 
            if frequency_s.get(key,0) < value: 
                return "" 
            
        i = 0
        curr_frequency = {}
        ans_str = s
        for j in range(i, len(s)):
            if s[j] in curr_frequency:
                curr_frequency[s[j]] = curr_frequency[s[j]] + 1
            else: 
                curr_frequency[s[j]] = 1
            while self.check_count(curr_frequency, frequency_t) is True:
                ans_str = s[i:j+1] if len(ans_str) > len(s[i:j+1]) else ans_str
                curr_frequency[s[i]] = curr_frequency[s[i]] - 1
                i+=1 
        return ans_str

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
    print(sol.optimal_approach("aaaaaaaaaaaabbbbbcdd", "abcdd"))