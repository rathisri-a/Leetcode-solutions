1class Solution(object):
2    def missingNumber(self, nums):
3        total=0
4        for i in range(1,len(nums)+1):
5            total+=i
6        missing=total-sum(nums)
7        return missing
8        