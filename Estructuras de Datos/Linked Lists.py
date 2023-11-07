# Date    September 5, 2022
# Hour    9:00 a.m.

class Node:
    def __init__(self, data, next=None):
        if type(data) != tuple:
            return "Data must be a tuple!"
        self.data = data
        self.next = next
    def __repr__(self):
        string = ""
        for item in self.data:
            if item != self.data[-1]:
                string += str(item) + " "
            else:
                string += str(item)
        return string

class LinkedList:
    def __init__(self, data):
        if type(data) != tuple:
            return "Data must be a tuple!"
        self.nodes = []
        self.nodes.append(Node(data))
    def __repr__(self):
        string = ""
        for node in self.nodes:
            if node != self.nodes[-1]:
                string += str(node) + " -> "
            else:
                string += str(node)
        return string
    def add_node(self, data):
        self.nodes.append(Node(data))
        self.nodes[-2].next = self.nodes[-1]

# This is very basic but is just for fun
# Time    9:42