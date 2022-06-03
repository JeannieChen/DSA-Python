

from multiprocessing.sharedctypes import Value


class Graph:
    def __init__(self):
        self.adj_list = {}  # dict

    def print_graph(self):
        for v in self.adj_list:
            print(v, ":", self.adj_list[v])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
            

# Test
my_gh = Graph()
my_gh.add_vertex('A')
my_gh.add_vertex('B')
my_gh.add_vertex('C')
my_gh.add_edge('A','B')
my_gh.remove_edge('A', 'B')
my_gh.remove_vertex('B')

print("Final graph: ")
my_gh.print_graph()

