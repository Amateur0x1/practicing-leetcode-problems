#
# @lc app=leetcode.cn id=2490 lang=python3
#
# [2490] 回环句
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sl = sentence.split(' ')
        sl.append(sl[0])
        sl.insert(0, sl[-2])
        print(sl)
        print('-----')
        n = len(sl)
        for i in range(1, n-1):
            h = sl[i][0]
            d = sl[i-1][-1]
            while sl[i][-1] != sl[i+1][0] or sl[i][0] != sl[i-1][-1]:
                return False
        return True
solution = Solution()
sentence = "ab a"
print(solution.isCircularSentence(sentence))

# @lc code=end

