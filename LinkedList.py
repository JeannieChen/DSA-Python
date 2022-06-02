
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# Node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LL constructor
class LL:
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

        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1: 
            temp = self.head
            self.head = None
            self.tail = None

        else:
            pre = self.head
            temp = self.head
            while(temp.next): # if it's pointing to a node
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
        
        self.length -= 1
        return temp.value
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp.value       
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
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
            temp = self.get(index-1)
            post = temp.next
            temp.next = new_node
            new_node.next = post
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail # head -> tail
        self.tail = head      # tail -> head

        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

# Test
my_LL = LL(2) #2
my_LL.append(3) #2,3
my_LL.append(4) #2,3,4

print("pop: ", my_LL.pop())   #2,3
my_LL.prepend(1)       #1,2,3
print("pop 1st: ", my_LL.pop_first()) #2,3
print("get: ", my_LL.get(0).value) #2,3
my_LL.set_value(0,1)  #1,3

my_LL.insert(2,4) #1,3,4
my_LL.remove(0)   #3,4
my_LL.append(1)   #3,4,1
my_LL.reverse()   #1,4,3

print("Final List: ")
my_LL.print_list() #1,4,3
