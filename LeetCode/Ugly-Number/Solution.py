1class Solution(object):
2    def isUgly(self, n):
3        original=n
4        if n<=0:
5            return False
6        else:
7            for i in[2,3,5]:
8                while n%i==0:
9                    n=n//i
10            if n==1:
11                return True
12            else:
13                return False
14        