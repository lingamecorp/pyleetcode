#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode.cn/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.95%)
# Likes:    1739
# Dislikes: 0
# Total Accepted:    321.6K
# Total Submissions: 643.6K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回 滑动窗口中的最大值 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], k = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#


from typing import List


# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = 0
        r = l + k - 1
        while r < len(nums):
            c = l
            while c <= r:
                if not q:
                    q.append(nums[c])
                else:
                    if nums[c] > q[-1]:
                        q.append(nums[c])
                c += 1
            # if q:
            res.append(q[-1])
            if q[0] == nums[l]:
                q.popleft()
            l += 1
            r += 1
        return res
# @lc code=end


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    s = Solution()
    res = s.maxSlidingWindow(nums, k)
    assert res == [3,3,5,5,6,7]

    nums = [4, 3, 5, 4, 3, 3, 6, 7]
    k = 3
    # s = Solution()
    res = s.maxSlidingWindow(nums, k)
    assert res == [5, 5, 5, 4, 6, 7]

    nums = [1, -1]
    k = 1
    res = s.maxSlidingWindow(nums, k)
    assert res == [1, -1]
