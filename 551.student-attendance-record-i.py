#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and 'LLL' not in s
# @lc code=end

