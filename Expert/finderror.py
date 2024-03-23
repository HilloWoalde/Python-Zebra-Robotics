class _Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None # Initially pointing to nothing

class LinkedList:
    def __init__(self) -> None:
        self._first = None

    def print_items(self) -> None:
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def __len__ (self):
        counter = 0
        if self._first is not None:
            curr = self._first
            while curr is not None:
                counter += 1
                if curr.next is not None:
                    curr = curr.next
                else:
                    return counter
        return counter

    def contains(self, item):
        curr = self._first
        while curr.next is not None:
            if item == curr.item:
                return True
            curr = curr.next
        return False

    def append(self, item):
        curr = _Node(item)
        print(self.__len__())
        if len(self) == 0:
            self._first = _Node(curr)
        elif self.__len__() == 1:
            self._first.next = _Node(item)
        else:
            curr_two = self._first
            while curr_two is not None:
                curr_two = curr_two.next
                curr_two.next = curr

llist = LinkedList()
llist.append('a')
llist.append('b')
llist.append('g')
llist.append('d')
llist.append('y')
print("Node Data")
llist.print_items()
llist.contains("a")
llist.contains("y")
llist.contains("g")
llist.print_items()
print("\nSize of linked list :", end=" ")
print(llist.__len__())