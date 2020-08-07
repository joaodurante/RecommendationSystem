# REFERENCE: https://medium.com/@keithwhor/using-graph-theory-to-build-a-simple-recommendation-engine-in-javascript-ec43394b35a3

from Edge import Edge
from Node import Node
from helpers.DataHelper import DataHelper
import json

dataHelper = DataHelper()
users = dataHelper.getUsers()
books = dataHelper.getBooks()
genres = dataHelper.getGenres()
view = dataHelper.getViews()
purchaseds = dataHelper.getPurchased()
belongs = dataHelper.getBelongs()

### NODES ##
# Persons #
# joao = Node('Person', {'name': 'Joao'})
# carol = Node('Person', {'name': 'Caroline'})
# gui = Node('Person', {'name': 'Guilherme'})
usersNodes = [ Node('user', user) for user in users ]

# Books
# hp = Node('Book', {'name': 'Harry Potter'})
# percy = Node('Book', {'name': 'Percy Jackson'})
# cityOfPaper = Node('Book', {'name': 'City of Paper'})
# whoAreYouAlaska = Node('Book', {'name': 'Who are you Alaska?'})
# brasCubas = Node('Book', {'name': 'Bras Cubas'})
booksNodes = [ Node('book', book) for book in books ]

# Genres
# scifi = Node('Genre', {'name': 'sci-fi'})
# romance = Node('Genre', {'name': 'romance'})
genresNodes = [ Node('genre', genre) for genre in genres ]

### EDGES ###
# Purchased
# purchased = []
# purchased.append(Edge('purchased', []).link(joao, hp, False))
# purchased.append(Edge('purchased', []).link(joao, percy, False))
# purchased.append(Edge('purchased', []).link(carol, cityOfPaper, False))
# purchased.append(Edge('purchased', []).link(carol, whoAreYouAlaska, False))
purchasedEdges = [ Edge('purchased', []).link(
    dataHelper.getNodeById(purchaseds, purchased.userId), dataHelper.getNodeById(purchaseds, purchased.bookId), False
) for purchased in purchaseds ]

# Interested
# interested = []
# interested.append(Edge('interested', []).link(joao, scifi, False))
# interested.append(Edge('interested', []).link(carol, scifi, False))
# interested.append(Edge('interested', []).link(carol, romance, False))
# interested.append(Edge('interested', []).link(gui, romance, False))


# Belongs to the genre
# belongs = []
# belongs.append(Edge('belongs', []).link(hp, scifi, False))
# belongs.append(Edge('belongs', []).link(percy, scifi, False))
# belongs.append(Edge('belongs', []).link(cityOfPaper, romance, False))
# belongs.append(Edge('belongs', []).link(whoAreYouAlaska, romance, False))
# belongs.append(Edge('belongs', []).link(brasCubas, romance, False))
