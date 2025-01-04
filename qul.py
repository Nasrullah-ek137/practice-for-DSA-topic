class Queue:

    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("queue underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue underflow")
        
    def size(self):
        return len(self.items)
    
q=Queue()

q.enqueue(10)
q.enqueue(30)
q.enqueue(50)

print(q.dequeue())
print(q.get_front())
print(q.get_rear())
print(q.size())
