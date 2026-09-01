1class Solution(object):
2    def reverseStr(self, s, k):
3        s=list(s)
4        for i in range(0,len(s),2*k):
5            if i+k<=s:
6                s[i:i+k]=s[i:i+k][::-1]
7        return "".join(s)
8        