# Node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# LL constructor
class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:  # if self.head is None
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1: 
            self.head = None
            self.tail = None

        else:
            prev = temp.prev
            self.tail = prev

            self.tail.next = None
            temp.prev = None
            self.length -= 1
            
            if self.length == 0:
                self.head = None
                self.tail = None

        return temp.value
     
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value       
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1 - index):
                temp = temp.prev
        
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            prev = self.get(index-1)
            post = prev.next

            prev.next = new_node
            new_node.next = post

            post.prev = new_node
            new_node.prev = prev

            self.length += 1
            return True
   
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        temp = self.get(index)
        prev = temp.prev
        post = temp.next

        temp.prev = None
        temp.next = None

        prev.next = post
        post.prev = prev

        self.length -= 1
        return True


# Test
my_DLL = DLL(2) #2
my_DLL.append(3) #2,3
my_DLL.append(4) #2,3,4
print("pop: ", my_DLL.pop())   #2,3
my_DLL.prepend(1)       #1,2,3
print("pop 1st: ", my_DLL.pop_first()) #2,3
my_DLL.prepend(1)       #1,2,3
print("get: ", my_DLL.get(1).value) #1,2,3
my_DLL.set_value(1,1)  #1,1,3
my_DLL.insert(2,4) #1,1,4,3
my_DLL.remove(0)   #1,4,3

print("Final List: ")
my_DLL.print_list() 

