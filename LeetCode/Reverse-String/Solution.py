1class Solution(object):
2    def reverseString(self, s):
3        left=0
4        right=len(s)-1
5        while(left<right):
6            s[left],s[right]=s[right],s[left]
7            left+=1
8            right-=1
9        return s