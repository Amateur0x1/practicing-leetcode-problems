#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#

# @lc code=start
class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        for i in range(len(nums)):
            right = n-1
            left = i
            while left < right:
                if nums[left] + nums[right] < target:
                    answer += right - left
                    break
                right -= 1
        return answer
# @lc code=end

