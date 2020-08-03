from Unit import Unit

class Node(Unit):
    """
        Parameters:
            String entity: entity type (person for example)
            Dic properties: entity properties
    """
    def __init__(self, entity, properties):
        super().__init__(entity, properties)
        self.edges = []
        self.inputEdges = []
        self.outputEdges = []

    def unlink(self):
        edges = self.edges

        for i in edges:
            i.unlink()

    
