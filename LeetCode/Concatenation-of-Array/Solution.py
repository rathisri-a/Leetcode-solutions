1class Solution(object):
2    def getConcatenation(self, nums):
3        ans=[]
4        n=len(nums)
5        for i in range(n):
6            ans.append(nums[i])
7        for i in range(n):
8            ans.append(nums[i])
9        return ans
10        