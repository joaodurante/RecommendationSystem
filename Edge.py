import Unit

class Edge(Unit):
    def __init__(self, entity, properties):
        super().__init__(entity, properties)
        self.inputNode = None
        self.outputNode = None
        self.duplex = False

        self.distance = 1


    def _linkTo(self, node, direction):
        """
            link a node in a direction

            Parameters:
                Node node: node to link
                direction: direction
        """
        if direction <= 0:
            node.inputEdges.append(self)
        elif direction >= 0:
            node.output.append(self)

        node.edges.append(self)
        return True

    def link(self, inputNode, outputNode, duplex):
        """
            link two nodes, optionally make edge bidirectional/duplex
            
            Parameters:
                Node inputNode: input node
                Node outputNode: output Node
                bool duplex: edge is duplex or not
        """
        self.unlink()

        self.inputNode = inputNode
        self.outputNode = outputNode
        self.duplex = True

        if duplex:
            self._linkTo(inputNode, 0)
            self._linkTo(outputNode, 0)
            return self

        self._linkTo(inputNode, 1)
        self._linkTo(outputNode, -1)
        return self

    def setDistance(self, value):
        """
            set distance from transversal

            Parameters:
                value: distance value
        """
        self.distance = value or 0

    
    def setWeight(self, value):
        """
            set weight = 1 / distance

            Parameters:
                value: value
        """
        self.distance = 1 / value

    def findOppositeNode(self, node):
        """ 
            find the opposite node giving a starting node

            Parameters:
                node: starting node
        """
        if self.inputNode == node:
            return self.outputNode
        elif self.outputNode == node:
            return self.inputNode
        else:
            return None

    def unlink(self):
        """ unlink edge, remove connections from nodes """
        inputNode = self.inputNode
        outputNode = self.outputNode

        if not inputNode and not outputNode:
            return None
        
        if self in inputNode.edges:                         
            inputNode.edges.remove(self)                        # remove self reference from inputNode.edges
        if self in outputNode.edges:
            outputNode.edges.remove(self)                       # remove self reference from outputNode.edges
        if self in inputNode.outputEdges:
            inputNode.outputEdges.remove(self)                  # remove self reference from inputNode.outputEdges
        if self in outputNode.inputEdges:                       
            outputNode.inputEdges.remove(self)                  # remove self reference from outputNode.inputEdges

        if self.duplex:                                         # if edge is bidirectional/duplex
            if self in inputNode.inputEdges:
                inputNode.inputEdges.remove(self)               # remove self reference from inputNode.inputEdges
            if self in outputNode.outputEdges:
                outputNode.outputEdges.remove(self)             # remove self reference from outputNode.outputEdges

        self.inputNode = None
        self.outputNode = None
        self.duplex = False
        return True
        
