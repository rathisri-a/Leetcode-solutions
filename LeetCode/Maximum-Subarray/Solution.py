1class Solution(object):
2    def maxSubArray(self, nums):
3        m=nums[0]
4        c=0
5        for i in nums:
6            if c<0:
7                c=0
8            c+=i
9            if c>m:
10                m=c
11        return m
12        