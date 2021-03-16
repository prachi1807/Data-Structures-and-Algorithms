# Stack implementation using list
class Stack:
    
    def __init__(self):
        self.stack = []
        self.top = -1
        
    def push(self, value):
        self.stack.append(value)
        self.top += 1
        
    def pop(self):
        if self.top!=-1:
            self.top -= 1
            return self.stack.pop()
        return -1
    
    def printStack(self):
        print(self.stack)
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.pop()
stack.pop()

stack.printStack()
