const ug = require('ug')
const DataHelper = require('./DataHelper')

class GraphService {
    constructor() {
        this.graph = new ug.Graph()
        this.dh = new DataHelper()

        // load graph file if exists else create it
        this._loadGraph()
    }

    _loadGraph = () => {
        this.graph.load('./graphfile.ugd', (err) => {
            if(err) {
                // get data from files
                this.users = this.dh.getUsers()
                this.books = this.dh.getBooks()
                this.genres = this.dh.getGenres()
                this.purchased = this.dh.getPurchased()
                this.interested = this.dh.getInterested()
                this.belongs = this.dh.getBelongs()

                // create nodes
                this._createNodes()

                // create edges
                this._createEdges()

                // save graph file
                this._saveGraph()
            }
        })
    }

    _createNodes = () => {
        this.users.forEach(obj => this.graph.createNode('user', obj))
        this.books.forEach(obj => this.graph.createNode('book', obj))
        this.genres.forEach(obj => this.graph.createNode('genre', obj))
    }

    _createEdges = () => {
        this.purchased.forEach(obj => {
            this.graph.createEdge('purchased')
                .link(
                    this.graph.nodes('user').query().filter({ id: obj.userId }).first(),
                    this.graph.nodes('book').query().filter({ id: obj.bookId }).first(),
                    false
                ).setDistance(1)
        })
        
        this.interested.forEach(obj => {
            this.graph.createEdge('interested')
                .link(
                    this.graph.nodes('user').query().filter({ id: obj.userId }).first(),
                    this.graph.nodes('genre').query().filter({ id: obj.genreId }).first(),
                    true
                ).setDistance(2)
        })
        
        this.belongs.forEach(obj => {
            this.graph.createEdge('belongs')
                .link(
                    this.graph.nodes('book').query().filter({ id: obj.bookId }).first(),
                    this.graph.nodes('genre').query().filter({ id: obj.genreId }).first(),
                    true
                ).setDistance(2)
        })
    }

    _saveGraph = () => {
        this.graph.save('graphfile.ugd', (err) => {
            if(err)
                console.log(err)
        })
    }

    getRecommendation = (userId) => {
        const res = []

        const results = this.graph.closest(
            this.graph.nodes('user').query().filter({ id: userId }).first(), 
            {
                compare: node => { return node.entity === 'book' },                     // function containing a comparison constraint for the node
                minDepth: 2,                                                            // minimum distance from our target
                direction: 1                                                            // Which direction can we traverse the graph in (-1 incoming nodes, 0 both, 1 outgoing nodes)
            }
        )
        
        results.map(result => {
            let totalDistance = 0
        
            result._raw.map(unit => {
                if(unit.hasOwnProperty('distance')) {
                    totalDistance += unit.distance
                }
            })
        
            res.push({
                name: result._raw.pop().get('name'),
                totalDistance: totalDistance,
                totalWeight: 1 / totalDistance
            })
        })
        console.log(res)
    }
}

module.exports = GraphService