1class Solution(object):
2    def countDigits(self, num):
3        count=0
4        for i in str(num):
5            if num%int(i)==0:
6                count+=1
7        return count
8
9        