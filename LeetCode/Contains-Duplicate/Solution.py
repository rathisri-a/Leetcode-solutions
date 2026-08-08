1class Solution(object):
2    def containsDuplicate(self, nums):
3        n=set()
4        for i in nums:
5            if i in n:
6                return True
7            n.add(i)
8        return False
9        