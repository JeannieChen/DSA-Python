

# HT constructor
import enum


class HashTable:
    def __init__(self, size):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash+ord(letter)*23) % len(self.data_map)
            # remainder: 0-6
        return my_hash
    
    def print_hash(self):
        for i,val in enumerate(self.data_map):
            print(i, ': ', val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        li = self.data_map[index]
        if li is not None:
            for i in range(len(li)):
                if li[i][0] == key:
                    return li[i][1]
        return None
    
    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            li = self.data_map[i]
            if li is not None:
                for j in range(len(li)):
                    keys.append(li[j][0])
        return keys


# Test
my_ht = HashTable(size=7)
my_ht.set_item('Jeanie', 713)
my_ht.set_item('Eric', 312)
print("Find value:", my_ht.get_item('Eric'))
print("Find value:", my_ht.get_item('Mia'))
print("All keys: ", my_ht.keys())

print("Final HT: ")
my_ht.print_hash()