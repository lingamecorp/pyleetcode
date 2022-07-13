# 栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，
# 但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。
# 当栈为空时，peek 返回 -1。

# 示例1:

#  输入：
# ["SortedStack", "push", "push", "peek", "pop", "peek"]
# [[], [1], [2], [], [], []]
#  输出：
# [null,null,null,1,null,2]
# 示例2:

#  输入： 
# ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
# [[], [], [], [1], [], []]
#  输出：
# [null,null,null,null,null,true]
# 说明:

# 栈中的元素数目在[0, 5000]范围内。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sort-of-stacks-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from collections import deque


class SortedStack:

    def __init__(self):
        self.main = deque()
        self.aux = deque()

    def push(self, val: int) -> None:
        if not self.main:
            self.main.append(val)
        else:
            top = self.main[-1]
            while self.main and val > top:
                self.aux.append(self.main.pop())
                if self.main:
                    top = self.main[-1]
            self.main.append(val)
            while self.aux:
                self.main.append(self.aux.pop())

    def pop(self) -> None:
        if self.main:
            return self.main.pop()

    def peek(self) -> int:
        if self.main:
            return self.main[-1]
        return -1

    def isEmpty(self) -> bool:
        if not self.main:
            return True
        return False