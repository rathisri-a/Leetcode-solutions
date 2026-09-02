1class Solution(object):
2    def numberOfEmployeesWhoMetTarget(self, hours, target):
3        count=0
4        for i in hours:
5            if i>=target:
6                count+=1
7        return count
8            
9        