1class Solution(object):
2    def runningSum(self, nums):
3
4        result=[]
5        total=0
6        for i in nums:
7            total+=i
8            result.append(total)
9        return result
10    
11        