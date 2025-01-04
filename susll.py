# Stack using singly linked list

from sll import *

class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1

    def peek(self):
        if not self.is_empty():
            return self.mylist
        
    def size(self):
        return self.item_count
    
s=Stack()

s.push(100)
s.push(34)
s.push(900)

print(s.peek())
print(s.pop())
print(s.size())