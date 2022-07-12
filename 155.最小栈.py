#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode.cn/problems/min-stack/description/
#
# algorithms
# Medium (58.32%)
# Likes:    1347
# Dislikes: 0
# Total Accepted:    399.4K
# Total Submissions: 684.8K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 实现 MinStack 类:
# 
# 
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 <= val <= 2^31 - 1
# pop、top 和 getMin 操作总是在 非空栈 上调用
# push, pop, top, and getMin最多被调用 3 * 10^4 次
# 
# 
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.main = []
        self.aux = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if len(self.aux) == 0:
            self.aux.append(val)
        else:
            if val <= self.aux[-1]:
                self.aux.append(val)
            # else:
            #     self.aux.append(self.aux[-1])

    def pop(self) -> None:
        if len(self.main) > 0:
            top = self.main.pop(-1)
            if top == self.aux[-1]:
                self.aux.pop(-1)

    def top(self) -> int:
        if len(self.main) > 0:
            return self.main[-1]

    def getMin(self) -> int:
        if len(self.aux) > 0:
            return self.aux[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

