# Node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack constructor
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node 
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            temp = self.top
            new_node.next = temp
            self.top = new_node
        
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp       
    

# Test
my_Stack = Stack(4) #4
my_Stack.push(5)    #5,4
my_Stack.push(6)    #6,5,4
print("pop: ", my_Stack.pop().value) #5,4

print("Final stack: ")
my_Stack.print_stack() 
