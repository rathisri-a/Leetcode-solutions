1class Solution(object):
2    def moveZeroes(self, nums):
3        j=0
4        for i in range (len(nums)):
5            if nums[i]!=0:
6                nums[i],nums[j]=nums[j],nums[i]
7                j+=1
8        