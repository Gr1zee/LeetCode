class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.minstack) or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.minstack and val == self.minstack[-1]:
                self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)
minStack.getMin()
minStack.top()
minStack.pop()
minStack.getMin()
