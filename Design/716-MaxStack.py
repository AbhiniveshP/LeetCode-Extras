class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.maxStack = [float('-inf')]

    def push(self, x: int) -> None:

        self.mainStack.append(x)
        self.maxStack.append(max(x, self.maxStack[-1]))

    def pop(self) -> int:

        self.maxStack.pop()
        return self.mainStack.pop()

    def top(self) -> int:

        return self.mainStack[-1]

    def peekMax(self) -> int:

        return self.maxStack[-1]

    def popMax(self) -> int:

        maxElement = self.peekMax()
        tempStack = []

        while (self.top() != maxElement):
            tempStack.append(self.pop())

        self.pop()

        while (len(tempStack) > 0):
            self.push(tempStack.pop())

        return maxElement

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()