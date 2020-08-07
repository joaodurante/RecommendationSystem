import json

class DataHelper:
    def getData(self, file):
        with open('./data/{}.json'.format(file), 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)

    def getNodeById(self, data, id):
        for item in data:
            if item.getProperty('id') == id:
                return item