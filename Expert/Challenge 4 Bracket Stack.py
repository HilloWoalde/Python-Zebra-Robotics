class Stack:
    #items = []
    def __init__(self, items):
        self.items = items
        for i in items:
            self.items.append(i)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if (self.is_empty() == False):
            a = self.items(len(self.items)-1)
            self.items.pop(len(self.items)-1)
            return(a)
    def is_empty(self):
        return(self.items == [])
string=input("Input a string of left and right brackets\n")
brackets = []
for i in string:
    if i == ")" or i == "(":
        brackets.append(i)
bstack = Stack(brackets)
lefts = 0
rights = 0
for i in range(0, len(bstack.items)):
    a = bstack.pop()
    if a == "(":
        lefts += 1
    elif a == ")":
        rights += 1
if lefts == rights:
    print("There are an equal number of left and right brackets")
else:
    print("There are an unequal number of left and right brackets")