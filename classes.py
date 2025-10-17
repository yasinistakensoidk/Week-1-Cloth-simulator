class particle():
    def __init__(self, x, y, index, parents=[], children=[], siblings=[], depth=0, velocity = (0, 0), acceleration = (0, 0)):
       # initialising the neccessary varibales
       self. parents = parents
       self.children = children
       self.siblings = siblings
       self.index = index
       self.depth =  depth
       self.position = (x, y)
       self.velocity = velocity
       self.accelaration = acceleration    

    def move(self):
        # if loses parent, siblings become parents

        #need to make it so that anchors dont do this otherwise we cascade badly
        if len(self.parents)==0: # if it loses its parents
            self.parents=self.siblings.copy() # siblings become parents
            self.siblings=self.children.copy() # children become siblings
            self.children=[] #loses children
            # {ADD FEATURE} make it so that the particle moves in a cirular path like a pedulum and makes the parent swing

        # if loses child, no impact (could have it bounce up but we can add that later)
        # if loses sibling, no impact (could have it swing a bit)
        # if particle below moves down, move current particle down depending on chain length (anchor-->tip)
        # if parent moves down, move current down by same amount
        # if parent moves up, move current up depending on chain length
        pass

    def locate(self,Nodes, parents, siblings, children): # {OPTIMISE} dont need dijkstras, depth is just min(Parent_Depth)+1
        # dijkstras to find the quikest path to an anchor to determine its depth, then we store the path to the nearest anchor in a stack
        queue = []
        stack_Full = []
        stack_Path = []
        noAnchor = True
        while noAnchor: # we need to go to the 
            # We need to analyse all the nodes connected to the first node in the queue:
            # if we find that a node originates from the first particle then we can throw it either into parents, siblings, or children
            pass
            #explore all parents of said node


        self.depth = d