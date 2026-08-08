1class Solution(object):
2    def maxArea(self, height):
3        left=0
4        right=len(height)-1
5        max_water=0
6        while left<right:
7            h=min(height[left],height[right])
8            width=right-left
9            cur_water=h*width
10            if max_water<cur_water:
11                max_water=cur_water
12            if height[left]<height[right]:
13                left+=1
14            else:
15                right-=1
16        return max_water