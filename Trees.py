# Node constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# BST constructor
class BST:
    def __init__(self):
        self.root = None 
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root  
        while True:
            if new_node.value == temp.value: # If value exists
                return False
            if new_node.value < temp.value:  # Go left
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:                            # Go right
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value: # Go left
                temp = temp.left
            elif value > temp.value: # Go right
                temp = temp.right
            else:
                return True
            
        return False
    
    def min_val(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        
        return current_node


                


# Test
my_tree = BST()
my_tree.insert(5)
my_tree.insert(9)
my_tree.insert(3)
my_tree.insert(8)
my_tree.insert(4)


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(3))
print(my_tree.contains(7))
print("Min:" , my_tree.min_val(my_tree.root).value)
