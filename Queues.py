# Node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Queue constructor
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node 
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.last
            temp.next = new_node
            self.last = new_node
        
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp    


# Test
my_Queue = Queue(4) #4
my_Queue.enqueue(5)    #4,5
my_Queue.enqueue(6)    #4,5,6
print("dequeue: ", my_Queue.dequeue().value) #5,6

print("Final queue: ")
my_Queue.print_queue() 
