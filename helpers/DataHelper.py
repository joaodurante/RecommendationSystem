import json

class DataHelper:
    def getUsers(self):
        with open('./data/users.json', 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)

    def getBooks(self):
        with open('./data/books.json', 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)

    def getGenres(self):
        with open('./data/genres.json', 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)

    def getPurchased(self):
        with open('./data/purchased.json', 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)

    def getViews(self):
        with open('./data/view.json', 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)
    
    def getBelongs(self):
        with open('./data/belongs.json', 'r') as json_file:
            try:
                data = json_file.read()
                return json.loads(data)['data']
            except Exception as e:
                print(e)

    def getNodeById(self, data, id):
        for item in data:
            if item.id == id:
                return item