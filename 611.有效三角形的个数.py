#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(2, n):
            right = i - 1
            left = 0
            while right > left:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans
solution = Solution()
print(solution.triangleNumber([2,2,3,4]))

# @lc code=end

