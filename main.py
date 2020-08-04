# REFERENCE: https://medium.com/@keithwhor/using-graph-theory-to-build-a-simple-recommendation-engine-in-javascript-ec43394b35a3

from Edge import Edge
from Node import Node

### NODES ###
# Persons
joao = Node('Person', {'name': 'Joao'})
carol = Node('Person', {'name': 'Caroline'})

# Books
hp = Node('Book', {'name': 'Harry Potter'})
percy = Node('Book', {'name': 'Percy Jackson'})
cityOfPaper = Node('Book', {'name': 'City of Paper'})

# Genres
scifi = Node('Genre', {'name': 'sci-fi'})
romance = Node('Genre', {'name': 'romance'})

### EDGES ###
# Purchased
purchased = Edge('purchased', [])
purchased.link(joao, hp, False)
purchased.link(joao, percy, False)
purchased.link(carol, cityOfPaper, False)

# Interested
interested = Edge('interested', [])
interested.link(joao, scifi, False)
interested.link(carol, romance, False)

# Belongs to the genre
belongs = Edge('belongs', [])
belongs.link(hp, scifi, False)
belongs.link(percy, scifi, False)
belongs.link(cityOfPaper, romance, False)

