class Stack:
    #items = []
    def __init__(self, items=[]):
        self.items = []
        for i in items:
            self.push(i)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if (self.is_empty() == False):
            return(self.items.pop(len(self.items)-1))
    def is_empty(self):
        return(self.items == [])
string = input("Input a string of left and right brackets\n")
bstack = Stack()
a=0
for i in string:
    if i == "(":
        bstack.push(i)
    elif i == ")":
        bstack.pop()
if bstack.is_empty():
    print("There are an equal number of left and right brackets")
else:
    print("There are an unequal number of left and right brackets")
