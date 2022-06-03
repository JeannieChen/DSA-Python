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

    def traverse(self, current_node, results):
        if current_node.left is not None:
            self.traverse(current_node.left, results)
        if current_node.right is not None:
            self.traverse(current_node.right, results)
        results.append(current_node.value)
        return results

    def DFS_postorder(self):
        results = []
        return self.traverse(self.root, results)




# Test
my_tree = BST()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)



print("Final Tree: ")
print(my_tree.DFS_postorder())

