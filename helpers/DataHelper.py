import json

class DataHelper:
    def getData(self, file):
        """
            get data from a json file

            Parameters:
                file: filename
        """

        with open('./data/{}.json'.format(file), 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)

    def getConfig(self, config):
        """
            get config values from config.json

            Parameters:
                file: property name
        """

        with open('./config.json', 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)[config]
            except Exception as e:
                print(e)

    def getNodeById(self, nodes, id):
        """
            get Node using it's ID

            Parameters:
                nodes: list of Node
                id: id
        """
        for item in nodes:
            if item.getProperty('id') == id:
                return item

    def printConection(self, edges, propertyName):
        """
            print edges connections

            Parameters:
                edges: list of Edge
                propertyName: Node property that will be printed
        """
        for i in edges:
            print('{} ({})  --->    {}  --->    {} ({})'.format(
                i.inputNode.getProperty(propertyName),
                i.inputNode.entity,
                i.entity,
                i.outputNode.getProperty(propertyName),
                i.outputNode.entity
            ))