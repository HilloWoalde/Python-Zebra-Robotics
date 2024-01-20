class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    def __lt__(self, other):
        if self.data < other:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.data > other:
            return True
        else:
            return False
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return self.data
class LinkedList:
    def __init__(self):
        self.head = None
        self.index = -1
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next = new_node
            else:
                print("Index not present")
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
    def remove_first_node(self):
        if(self.head == None):
            return
        self.head = self.head.next
        self.head.prev = None
    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None
    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
    def remove_node(self, data):
        current_node = self.head
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print(None)
    def __str__(self):
        self.printLL()
    def __repr__(self):
        self.printLL()
    def insertInAscendingOrder(self, data):
        new_node = Node(data)

        if (self.head is None) or (data < self.head.data):
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.data < data:
            current_node = current_node.next

        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

    def removeLargest(self):
        if self.head is None:
            print("List is empty. Cannot remove the largest element.")
            return

        prev_node = None
        current_node = self.head
        largest_node = self.head

        while current_node.next:
            if current_node.next.data > largest_node.data:
                largest_node = current_node.next
                prev_node = current_node
            current_node = current_node.next

        if prev_node is None:
            self.head = largest_node.next
        else:
            prev_node.next = largest_node.next

        print(f"Removed the largest element: {largest_node.data}")
    
    def insertInDecendingOrder(self, data):
        new_node = Node(data)

        if (self.head is None) or (data > self.head.data):
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.data > data:
            current_node = current_node.next

        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

    def sort(self):
        current_node = self.head
        newLL = LinkedList()
        for i in range (0, self.sizeOfLL()):
            newLL.insertInAscendingOrder(current_node)
            current_node = current_node.next
        self.head = newLL.head
    
    def og_reverse_sort(self):
        current_node = self.head
        newLL = LinkedList()
        for i in range (0, self.sizeOfLL()):
            newLL.insertInDecendingOrder(current_node)
            current_node = current_node.next
        self.head = newLL.head

    def reverse_sort(self):
        current_node=self.head
        newLL=LinkedList()
        for i in range(0, self.sizeOfLL()):
            newLL.insertAtBegin(current_node)
            current_node = current_node.next
        self.head=newLL.head

    def iiao(self, data):
        self.insertInAscendingOrder(data)
        self.sort()
    
    def iido(self, data):
        self.insertInDecendingOrder(data)
        #self.og_reverse_sort()

    def __getitem__(self, index):
        current_node=self.head
        for i in range(0, index):
            current_node=current_node.next
            if current_node==None:
                break
        return(str(current_node))
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index >= self.sizeOfLL():
            self.index= -1
            raise StopIteration
        else:
            return self.__getitem__(self.index)

llist = LinkedList()
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)
print("Node Data")
llist.printLL()
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)
print("\nLinked list after removing a node:")
llist.printLL()
print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()
print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())
linked_list = LinkedList()
linked_list.iiao(1)
linked_list.iiao(3)
linked_list.iiao(9)
linked_list.iiao(14) 


linked_list.printLL()  # Output: 1 -> 3 -> 9 -> 14 -> None

linked_list.iiao(4)
linked_list.printLL()  # Output: 1 -> 3 -> 4 -> 9 -> 14 -> None

linked_list.removeLargest()
linked_list.printLL()

linked_list.iiao(5)
linked_list.printLL()

linked_list.insertAtBegin(8)
linked_list.printLL()
linked_list.iiao(7)
linked_list.printLL()
linked_list.insertAtIndex(4, 3)
linked_list.printLL()
linked_list.sort()
linked_list.printLL()

linked_list.insertAtEnd(8)
linked_list.printLL()
linked_list.iido(7)
linked_list.printLL()
linked_list.insertAtIndex(3, 4)
linked_list.printLL()
linked_list.reverse_sort()
linked_list.printLL()

print("4: " + linked_list[3])
print("7: " + linked_list[6])
print("1: " + linked_list[0])
print("3: " + linked_list[2])
print("8: " + linked_list[7]) 

for i in linked_list:
    print(i)