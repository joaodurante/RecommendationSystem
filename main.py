# REFERENCE: https://medium.com/@keithwhor/using-graph-theory-to-build-a-simple-recommendation-engine-in-javascript-ec43394b35a3

from Edge import Edge
from Node import Node
from helpers.DataHelper import DataHelper
import json

dataHelper = DataHelper()
users = dataHelper.getData('users')
books = dataHelper.getData('books')
genres = dataHelper.getData('genres')
views = dataHelper.getData('view')
purchaseds = dataHelper.getData('purchased')
belongs = dataHelper.getData('belongs')
interesteds = dataHelper.getData('interested')
distances = dataHelper.getConfig('distance')


### NODES ###
# Persons #
usersNodes = [ Node('user', user) for user in users ]

# Books
booksNodes = [ Node('book', book) for book in books ]

# Genres
genresNodes = [ Node('genre', genre) for genre in genres ]


### EDGES ###
# Purchased
purchasedEdges = [ Edge('purchased', []).link(
    dataHelper.getNodeById(usersNodes, purchased['userId']), dataHelper.getNodeById(booksNodes, purchased['bookId']), False
) for purchased in purchaseds ]

# Interested
interestedEdges = [ Edge('interested', []).link(
    dataHelper.getNodeById(usersNodes, interested['userId']), dataHelper.getNodeById(genresNodes, interested['genreId']), False
) for interested in interesteds ]

# Belongs to the genre
belongsEdges = [ Edge('belongs', []).link(
    dataHelper.getNodeById(booksNodes, belong['bookId']), dataHelper.getNodeById(genresNodes, belong['genreId']), False
) for belong in belongs ]

# View
viewEdges = [ Edge('view', []).link(
    dataHelper.getNodeById(usersNodes, view['userId']), dataHelper.getNodeById(booksNodes, view['bookId']), False
) for view in views ]


### SETTING EDGES DISTANCES ###
# Purchased
for i in purchasedEdges:
    i.setDistance(distances['purchased'])

# Interested
for i in interestedEdges:
    i.setDistance(distances['interested'])

# Belongs
for i in belongsEdges:
    i.setDistance(distances['belongs'])

# View
for i in viewEdges:
    i.setDistance(distances['view'])

### PRINT ###
print("---- PURCHASED CONNECTIONS ----")
dataHelper.printConection(purchasedEdges, 'name')

print("\n\n---- INTERESTED CONNECTIONS ----")
dataHelper.printConection(interestedEdges, 'name')

print("\n\n---- BELONGS CONNECTIONS ----")
dataHelper.printConection(belongsEdges, 'name')

print("\n\n---- VIEW CONNECTIONS ----")
dataHelper.printConection(viewEdges, 'name')