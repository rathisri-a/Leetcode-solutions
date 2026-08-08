1class Solution(object):
2    def buildArray(self, nums):
3        ans=[]
4        n=len(nums)
5        for i in range(n):
6            ans.append(nums[nums[i]])
7        return ans
8
9        