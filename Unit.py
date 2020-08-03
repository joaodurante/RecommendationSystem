class Unit:         # noqa
    def __init__(self, entity, properties):
        self.entity = entity
        self.properties = properties

    def loadProperties(self, properties):
        self.properties = properties

    def setProperty(self, propertyName, propertyValue):
        self.properties['propertyName'] = propertyValue

    def unsetProperty(self, propertyName):
        if propertyName in self.properties:
            del self.properties[propertyName]
            return True
        else:
            return False

    def hasProperty(self, propertyName):
        if propertyName in self.properties:
            return True
        else:
            return False

    def getProperty(self, propertyName):
        if propertyName in self.properties:
            return self.properties[propertyName]
        else:
            return None