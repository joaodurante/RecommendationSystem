from helpers.DataHelper import DataHelper
import json
import networkx as nx

dataHelper = DataHelper()
users = dataHelper.getNodeData('users')
books = dataHelper.getNodeData('books')
genres = dataHelper.getNodeData('genres')

purchaseds = dataHelper.getEdgeData('purchased')
belongs = dataHelper.getEdgeData('belongs')
interesteds = dataHelper.getEdgeData('interested')
distances = dataHelper.getConfig('distance')
graph = nx.Graph()


graph.add_nodes_from(users, entity='user')
graph.add_nodes_from(books, entity='book')
graph.add_nodes_from(genres, entity='genre')


graph.add_edges_from([
    (i['outputId'], graph.nod) for i in purchaseds
])

