#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode.cn/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (47.95%)
# Likes:    775
# Dislikes: 0
# Total Accepted:    93.7K
# Total Submissions: 195.5K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "bcabc"
# 输出："abc"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 由小写英文字母组成
# 
# 
# 
# 
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = defaultdict(lambda: 0)
        used = defaultdict(lambda: False)
        stack = []  # 单调递增栈
        for c in s:
            freq[c] += 1
        for c in s:
            freq[c] -= 1
            while not used[c] and stack and c < stack[-1] and freq[stack[-1]] > 0:
                top = stack.pop()
                used[top] = False
            if not used[c]:
                stack.append(c)
                used[c] = True
        return "".join(stack)
# @lc code=end

