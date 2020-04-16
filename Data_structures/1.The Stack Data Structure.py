class Stack:
    def __init__(self):
        self.item=[]

    def push(self,value):
        self.item.append(value)
    
    def pop(self,value):
        self.item.pop(value)

    def get_stack(self):
        return self.item

    def is_empty(self):
        return self.item == []
    
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            return "Empty Stack"

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.get_stack())
print(s.is_empty())
print(s.peek())