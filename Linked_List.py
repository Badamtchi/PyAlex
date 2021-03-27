class Node:

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.nxt = n
        self.prv = p
    
    def __str__(self):
        print('(%s)' % self.data)

class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    
    def add(self, d):
        node = Node(d, self.root)
        self.root = node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.nxt
        return None
    
    def remove(self, d):
        this_node = self.root
        node_prev = None

        while this_node is not None:
            if this_node.data == d:
                if node_prev is not None:
                    node_prev.nxt = this_node.nxt
                else:
                    self.root = this_node.nex
                self.size -= 1
                return True
            else:
                node_prev = this_node
                this_node = this_node.nxt
            return False
    
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='-->')
            this_node = this_node.nxt
        print('None')
