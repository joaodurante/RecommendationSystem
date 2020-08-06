# REFERENCE: https://medium.com/@keithwhor/using-graph-theory-to-build-a-simple-recommendation-engine-in-javascript-ec43394b35a3

from Edge import Edge
from Node import Node

### NODES ###
# Persons
joao = Node('Person', {'name': 'Joao'})
carol = Node('Person', {'name': 'Caroline'})
gui = Node('Person', {'name': 'Guilherme'})

# Books
hp = Node('Book', {'name': 'Harry Potter'})
percy = Node('Book', {'name': 'Percy Jackson'})
cityOfPaper = Node('Book', {'name': 'City of Paper'})
whoAreYouAlaska = Node('Book', {'name': 'Who are you Alaska?'})
brasCubas = Node('Book', {'name': 'Bras Cubas'})

# Genres
scifi = Node('Genre', {'name': 'sci-fi'})
romance = Node('Genre', {'name': 'romance'})

### EDGES ###
# Purchased
purchased = []
purchased.append(Edge('purchased', []).link(joao, hp, False))
purchased.append(Edge('purchased', []).link(joao, percy, False))
purchased.append(Edge('purchased', []).link(carol, cityOfPaper, False))
purchased.append(Edge('purchased', []).link(carol, whoAreYouAlaska, False))

# Interested
interested = []
interested.append(Edge('interested', []).link(joao, scifi, False))
interested.append(Edge('interested', []).link(carol, scifi, False))
interested.append(Edge('interested', []).link(carol, romance, False))
interested.append(Edge('interested', []).link(gui, romance, False))

# Belongs to the genre
belongs = []
belongs.append(Edge('belongs', []).link(hp, scifi, False))
belongs.append(Edge('belongs', []).link(percy, scifi, False))
belongs.append(Edge('belongs', []).link(cityOfPaper, romance, False))
belongs.append(Edge('belongs', []).link(whoAreYouAlaska, romance, False))
belongs.append(Edge('belongs', []).link(brasCubas, romance, False))
