class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head 
        count = 0 # tracks which index curr is pointing at 

        while curr != None:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1

        return -1
            

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
  

    def remove(self, index: int) -> bool:
        if self.head is None:  # empty list
            return False

        if index == 0:
            # remove head
            self.head = self.head.next
            if self.head is None:  # list became empty
                self.tail = None
            return True

        # find node at position index-1 (prev)
        prev = self.head
        i = 0
        while i < index - 1 and prev is not None:
            prev = prev.next
            i += 1

        # index out of bounds if prev is None or there's no node to remove
        if prev is None or prev.next is None:
            return False

        # if removing the tail, update tail
        if prev.next == self.tail:
            self.tail = prev

        # bypass the node
        prev.next = prev.next.next
        return True

        

    def getValues(self) -> List[int]:
        values: List[int] = []
        curr = self.head
        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        return values
        
