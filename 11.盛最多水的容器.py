#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        right = len(height) - 1
        left = 0
        while left < right:
            maxArea = max(maxArea, (min(height[left], height[right]) * (right - left)))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
# @lc code=end

