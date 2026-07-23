class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class Deque:  
    def __init__(self):
        self.left = None # front of queue
        self.right = None # back of queue


    def isEmpty(self) -> bool:
        return self.left is None and self.right is None
        

    def append(self, value: int) -> None:

        newNode = ListNode(value)

        # queue is non empty
        if self.right:
            newNode.prev = self.right
            self.right.next = newNode
            self.right = self.right.next
        # queue is empty
        else:
            self.left = self.right = newNode

    def appendleft(self, value: int) -> None:

        newNode = ListNode(value)

        # queue is empty
        if not self.left:
            self.left = self.right = newNode
            return
        # queue is non empty
        newNode.next = self.left
        self.left.prev = newNode
        self.left = self.left.prev
        

    def pop(self) -> int:

        # queue is empty
        if not self.right:
            return -1

        val = self.right.val

        # only one node
        if self.left == self.right:
            self.left = None
            self.right = None
        else:
            self.right = self.right.prev
            self.right.next = None

        return val

    def popleft(self) -> int:

        # queue is empty
        if not self.left:
            return -1
        
        val = self.left.val

        # only one node
        if self.left == self.right:
            self.left = None
            self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None

        return val
        
