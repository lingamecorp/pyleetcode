#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
# https://leetcode.cn/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (68.85%)
# Likes:    699
# Dislikes: 0
# Total Accepted:    256.2K
# Total Submissions: 372.1K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
# 
# 实现 MyQueue 类：
# 
# 
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 
# 
# 说明：
# 
# 
# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty
# 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 1, 1, false]
# 
# 解释：
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
# 
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= x <= 9
# 最多调用 100 次 push、pop、peek 和 empty
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
# 
# 
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.s4push = []  # stack for push
        self.s4pop = []   # stack for pop

    def push(self, x: int) -> None:
        self.s4push.append(x)

    def _reverse(self) -> None:
        if not self.s4pop and self.s4push:
            while self.s4push:
                x = self.s4push.pop(-1)
                self.s4pop.append(x)

    def pop(self) -> int:
        self._reverse()
        if self.s4pop:
            return self.s4pop.pop(-1)

    def peek(self) -> int:
        self._reverse()
        if self.s4pop:
            return self.s4pop[-1]

    def empty(self) -> bool:
        if not self.s4push and not self.s4pop:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

