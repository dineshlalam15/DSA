"""
Character Replacement: "https://leetcode.com/problems/longest-repeating-character-replacement/"
"""

class Solution: 
    
    def calc_freq(self, frequency, s):
        if s in frequency:
            frequency[s] = frequency[s] + 1
        else:
            frequency[s] = 1
                
    def max_frequency(self, frequency):
        max_value = 0
        for key,value in frequency.items():
            if value > max_value:
                max_value = value
        return max_value
                
    def characterReplacement(self, s, k):
        #Check1: 
        if len(s) == 1:
            return len(s)
        
        #Check2: 
        if k == 0:
            curr_count = 1
            max_count = 1
            for i in range(0,len(s)-1):
                if s[i] == s[i+1]:
                    curr_count += 1
                    max_count = max(curr_count,max_count)
                else: 
                    curr_count = 1
            return max_count
            
        i = 0
        ans = 0
        curr_freq = {}
        for j in range(i,len(s)):
            self.calc_freq(curr_freq, s[j])
            max_freq = self.max_frequency(curr_freq)
            if (j-i+1) - max_freq > k:
                curr_freq[s[i]] = curr_freq[s[i]] - 1
                i += 1
            ans = max(ans, j-i+1)
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("AAAA",2))