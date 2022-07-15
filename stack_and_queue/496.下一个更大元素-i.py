#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
# https://leetcode-cn.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (70.71%)
# Likes:    766
# Dislikes: 0
# Total Accepted:    197.8K
# Total Submissions: 276.8K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
# 
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定
# nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出：[-1,3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
# - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# 
# 示例 2：
# 
# 
# 输入：nums1 = [2,4], nums2 = [1,2,3,4].
# 输出：[3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
# - 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 10^4
# nums1和nums2中所有整数 互不相同
# nums1 中的所有整数同样出现在 nums2 中
# 
# 
# 
# 
# 进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？
# 
#
from typing import List


# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 
        解法：单调递减栈 + 哈希表

        主要思路：由于nums1是nums2的子集，所以只要得到nums2中各个元素对应的NGE(Next Greater Element)
        即可，这些元素及其对应的NGE使用哈希表存储，key是nums2的各个元素，value是其对应的NGE；在寻找每个元
        素对应的NGE时，需要从后往前遍历nums2来维护一个单调递减的栈；这里不能用单调递增的栈是因为递增栈在遍历
        时可能会丢失值更大的元素（例如当nums2为[2,5,3,6,8,4,7,1]）.

        回顾暴力解法，在该解法中，首先需要在nums2中逐一定位nums1的各个元素，其时间复杂度为O(n^2)，然后再在
        nums中搜索给定元素对应的NGE，其时间复杂度为O(n)，总共的时间复杂度是O(n^2). 单调栈+哈希表解法改进的
        地方就是，使用单调栈寻找nums2的NGEs，其时间复杂度为O(n2)，通过使用哈希表来存储nums2的NGEs，使得寻找
        nums1的NGEs的时间复杂度变为O(n1)，当然，为此付出的空间复杂度变为O(n2).
        """
        mono_stack = []  # Monotonically decreasing stack
        nges = dict()    # Next Greater Elements
        # nums2最后一个元素肯定没有NGE
        nges[nums2[-1]] = -1
        mono_stack.append(nums2[-1])
        # 从后往前遍历nums2，寻找各个元素对应的NGE
        for i in range(len(nums2)-2, -1, -1):
            cur = nums2[i]
            top = mono_stack[-1]
            # if cur > top:
            if cur < top:
                nges[cur] = top
                while mono_stack and cur < top:
                    mono_stack.pop()
                    if mono_stack:
                        top = mono_stack[-1]
                # if cur <= top:
                #     nges[cur] = top
                # if not mono_stack:
                #     nges[cur] = -1
                # mono_stack.append(cur)
            else:
                nges[cur] = -1
            mono_stack.append(cur)
        # 匹配nums1各个元素对应的NGE
        results = [nges[k] for k in nums1]
        return results


# @lc code=end


if __name__ == "__main__":
    s = Solution()

    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    expected = [-1, 3, -1]
    actual = s.nextGreaterElement(nums1, nums2)
    assert actual == expected

    nums1 = [5, 6, 7, 8]
    nums2 = [2, 5, 3, 6, 8, 4, 7, 1]
    expected = [-1, 8, -1, -1]
    actual = s.nextGreaterElement(nums1, nums2)
    assert actual == expected