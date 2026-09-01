1class Solution(object):
2    def reverseWords(self, s):
3        word=s.split()
4        return " ".join(word[::-1])
5        