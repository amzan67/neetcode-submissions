class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:
        self.val = val 
        self.minstack.append(self.val)
        return self.minstack
    def pop(self) -> None:
        self.minstack.pop()
        return self.minstack

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return min(self.minstack)
    