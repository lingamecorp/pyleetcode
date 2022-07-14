#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
# https://leetcode.cn/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (65.61%)
# Likes:    660
# Dislikes: 0
# Total Accepted:    151.4K
# Total Submissions: 230.8K
# Testcase Example:  '[1,2,1]'
#
# 给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的
# 下一个更大元素 。
# 
# 数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1
# 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数； 
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [1,2,3,4,3]
# 输出: [2,3,4,-1,4]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 10^4
# -10^9 <= nums[j] <= 10^9
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """ 
        本题思路：循环数组模拟双倍后的数组 + 单调递减栈从后往前遍历
        """
        mono_stack = []  # Monotonically decreasing stack
        nges = [-1] * len(nums)  # Next Greater Elements
        n = len(nums)
        for i in range(2*n-1, -1, -1):  # 通过循环数组来模拟双倍后的数组
            j = i % n
            while mono_stack and nums[j] >= mono_stack[-1]:  # 因为要找的是更大的元素，所以这里必须是大于等于
                mono_stack.pop()
            if not mono_stack:
                nges[j] = -1
            else:
                nges[j] = mono_stack[-1]
            mono_stack.append(nums[j])
        return nges
# @lc code=end
