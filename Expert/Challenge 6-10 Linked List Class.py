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

    def reverse_recursively(self, node):
        if node is None or node.next is None:
            return node

        new_head = self.reverse_recursively(node.next)

        node.next.next = node
        node.next = None

        return new_head

    def reverse(self):
        self.head = self.reverse_recursively(self.head)

linked_list = LinkedList()
linked_list.iiao(1)
linked_list.iiao(3)
linked_list.iiao(14)
linked_list.iiao(9)
linked_list.printLL()

linked_list.reverse()
linked_list.printLL()
linked_list.reverse()
linked_list.printLL()