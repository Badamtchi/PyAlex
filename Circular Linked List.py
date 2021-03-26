class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.nxt = n
        self.prv = p

    def __str__(self):
        return ('(%s)' % self.data)
