class Stack():
    def __init__(self):
        self.items = []
  
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items == []

    def is_empty(self):
        return self.items == []
  
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_satck(self):
        return self.items



class Node:
    def __init__(self, node=None):
        self.node = node
        self.nextval = None
