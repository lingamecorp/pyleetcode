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
# -10^9 <= nums[i] <= 10^9
# 
# 
#


from typing import List


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono_stack = []  # Monotonically decreasing stack
        # nges = {k: -1 for k in nums}    # Next Greater Elements
        nges = [-1] * len(nums)
        # 第一轮遍历，使用递减栈从后往前遍历nums，寻找各个元素对应的NGE
        mono_stack.append(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            cur = nums[i]
            top = mono_stack[-1]
            if cur > top:
                while mono_stack and cur > top:
                    mono_stack.pop()
                    if mono_stack:
                        top = mono_stack[-1]
                if cur < top:
                    nges[i] = top
                if not mono_stack:
                    nges[i] = -1
                # mono_stack.append(cur)
            if cur < top:
                nges[i] = top
            mono_stack.append(cur)
        # 第二轮遍历，使用递增栈从前往后遍历nums，为第一轮没有找到NGE的元素重新搜索NGE
        mono_stack.clear()
        mono_stack.append(nums[0])
        for i in range(1, len(nums)):
            cur = nums[i]
            top = mono_stack[-1]
            if cur < top and nges[i] == -1:
                nges[i] = top
            if cur > top:
                mono_stack.append(cur)
        return nges
# @lc code=end
