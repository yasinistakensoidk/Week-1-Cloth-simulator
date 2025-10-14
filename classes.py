class particle():
    def __init__(self, parents, children, depth):
       self. parents = parents
       self.children = children
       self.depth =  depth
       self.velocity = (0, 0)
       self.accelaration = (0, 0)
    
    def move(self):
        pass

    def position(self,parents, children): # dijkstras to find the quikest path to an anchor
        pass