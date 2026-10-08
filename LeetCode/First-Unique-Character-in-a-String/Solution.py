1class Solution(object):
2    def firstUniqChar(self, s):
3        freq={}
4        for i in s:
5            if i in freq:
6                freq[i]+=1
7            else:
8                freq[i]=1
9        for i in range(len(s)):
10            if freq[s[i]] == 1:
11                return i
12                break
13        return -1
14        