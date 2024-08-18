#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:  # 优化二
                    continue
                right = n - 1
                left = j + 1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp == target:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:  # 跳过重复数字
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:  # 跳过重复数字
                            right -= 1
                    elif temp > target:
                        right -= 1
                    else:
                        left += 1
        return answer                        


# @lc code=end

