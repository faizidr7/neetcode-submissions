class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        copy = self.stack.copy()

        return copy.pop()

    def getMin(self) -> int:

        current_min = self.stack[0]
        for i in self.stack:
            if i < current_min:
                current_min = i
        return current_min
        
            

        
