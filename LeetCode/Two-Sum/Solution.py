1class Solution(object):
2    def twoSum(self, nums, target):
3        n=len(nums)
4        for i in range(n):
5            for j in range(i+1,n):
6                if nums[i]+nums[j]==target:
7                    return [i,j]
8        