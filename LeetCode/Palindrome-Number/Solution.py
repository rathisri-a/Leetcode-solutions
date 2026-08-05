1class Solution(object):
2    def isPalindrome(self, x):
3        if x<0:
4            print("False")
5        s=str(x)
6        rev=s[::-1]
7        return s==rev
8        
9        