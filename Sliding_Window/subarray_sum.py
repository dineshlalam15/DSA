"""
Minimum Size Subarray Sum: "https://leetcode.com/problems/minimum-size-subarray-sum/description/"
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        #Check 1: 
        if len(nums) == 0:
            return 0
        
        #Check 2: 
        if self.calc_sum(nums) < target:
            return 0
        
        i = 0
        sum = 0
        ans = len(nums)
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target: 
                # ans = min(ans, len(nums[i:j+1]))
                ans = min(ans, j-i+1)
                sum -= nums[i]
                i+=1
        return ans
    
    def calc_sum(self, nums):
        sum = 0
        for element in nums:
            sum += element
        return sum
    
if __name__ == "__main__":
    s = Solution()
    target = 11
    nums = [1,2,3,4,5]
    print(s.minSubArrayLen(target,nums))
