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


def reverse_stack(stack: list):
    if stack:
        reverse(stack)
        return stack


def reverse(stack: list):
    if not stack:
        return
    bottom = pop_bottom(stack)
    reverse(stack)
    stack.append(bottom)


def pop_bottom(stack: list) -> int:
    if stack:
        top = stack.pop(-1)
        if not stack:  # 此时已经到了栈底
            return top
        else:
            bottom = pop_bottom(stack)
            stack.append(top)
            return bottom


if __name__ == "__main__":
    case1 = [1, 2, 3, 4, 5]
    expected1 = [5, 4, 3, 2, 1]
    actual1 = reverse_stack(stack=case1)
    assert actual1 == expected1
    # print(actual1)

    case2 = []
    expected2 = None
    actual2 = reverse_stack(stack=case2)
    assert actual2 == expected2
    # print(actual2)