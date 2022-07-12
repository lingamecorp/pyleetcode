# 链接：https://www.nowcoder.com/questionTerminal/ba7d7f5d1edf4d1690d66e12e951f6ea
# 来源：牛客网
#
# 一个栈依次压入1,2,3,4,5那么从栈顶到栈底分别为5,4,3,2,1。将这个栈转置后，从栈顶到栈底为1,2,3,4,5，也就是实现了栈中元素的逆序，请设计一个算法实现逆序栈的操作，但是只能用递归函数来实现，而不能用另外的数据结构。
#
# 给定一个栈Stack以及栈的大小top，请返回逆序后的栈。
#
# 测试样例：
# [1,2,3,4,5],5
# 返回：[5,4,3,2,1]


from audioop import reverse


def reverse_stack(stack: list, size: int) -> list:
    if not stack or len(stack) != size:
        return
    return [i for i in _reverse(stack=stack)]


def _reverse(stack: list):
    if stack:
        val = stack.pop(-1)
        yield from _reverse(stack)
        yield val


if __name__ == "__main__":
    case1 = [1, 2, 3, 4, 5]
    size = len(case1)
    expected1 = case1.copy()
    actual1 = reverse_stack(stack=case1, size=size)
    assert actual1 == expected1

    case2 = []
    size = 0
    expected2 = None
    actual2 = reverse_stack(stack=case2, size=size)
    assert actual2 == expected2