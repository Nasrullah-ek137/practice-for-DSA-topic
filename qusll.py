class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty error")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("NO data in queue")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in queue")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count
    
q=Queue()

q.enqueue(100)
q.enqueue(230)
q.enqueue(980)

print(q.dequeue())
print(q.get_front())
print(q.get_rear())
print(q.size())