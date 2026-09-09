class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = float("inf")
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minNum:
            self.minStack.append(val)
            self.minNum = val
    
    def pop(self) -> None:
        value = self.stack.pop()

        if value is self.minNum:
            self.minStack.pop()

            if self.minStack:
                self.minNum = self.minStack[-1]
            else:
                self.minNum = float("inf")

    def top(self) -> int:
        #copy = self.stack.copy()
        #return copy.pop()

        return self.stack[-1]

    def getMin(self) -> int:

        if self.stack is None:
            return None
        if self.minNum == float("inf"):
            return None

        return self.minNum


        
        
            

        
