const ug = require('ug')
const DataHelper = require('./helpers/DataHelper')

class GraphService {
    constructor() {
        this.graph = new ug.Graph()
        this.dh = new DataHelper()

        // load the graph
        this._loadGraph()
    }

    /**
     * try to load graph if graph file exists, if not load data from .json files then create graph units
     */
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
                this._saveGraph('graphfile.ugd')
            }
        })
    }

    /**
     * create graph nodes using recorded data
     */
    _createNodes = () => {
        this.users.forEach(obj => this.graph.createNode('user', obj))                       // create users nodes
        this.books.forEach(obj => this.graph.createNode('book', obj))                       // create books nodes
        this.genres.forEach(obj => this.graph.createNode('genre', obj))                     // create genres nodes
    }

    /**
     * create graph edges using recorded data
     */
    _createEdges = () => {
        // create purchased edges
        this.purchased.forEach(obj => {
            this.graph.createEdge('purchased')
                .link(
                    this.graph.nodes('user').query().filter({ id: obj.userId }).first(),
                    this.graph.nodes('book').query().filter({ id: obj.bookId }).first(),
                    false
                ).setDistance(1)
        })
        
        // create interested edges
        this.interested.forEach(obj => {
            this.graph.createEdge('interested')
                .link(
                    this.graph.nodes('user').query().filter({ id: obj.userId }).first(),
                    this.graph.nodes('genre').query().filter({ id: obj.genreId }).first(),
                    true
                ).setDistance(2)
        })
        
        // create belongs edges
        this.belongs.forEach(obj => {
            this.graph.createEdge('belongs')
                .link(
                    this.graph.nodes('book').query().filter({ id: obj.bookId }).first(),
                    this.graph.nodes('genre').query().filter({ id: obj.genreId }).first(),
                    true
                ).setDistance(2)
        })
    }

    /**
     * save graph file
     * @param {String} filename filename
     */
    _saveGraph = (filename) => {
        this.graph.save(filename, (err) => {
            if(err)
                console.log(err)
        })
    }

    /**
     * get books recommendations based on userId received as param
     * @param userId user id
     * @returns array containing books informations and weights
     */
    getRecommendation = (userId) => {
        const res = []
        const results = this.graph.closest(                                             // get the closest paths from user to books
            this.graph.nodes('user').query().filter({ id: userId }).first(),            // query 'user' nodes using userId received as param
            {
                compare: node => { return node.entity === 'book' },                     // function containing a comparison constraint for the node
                minDepth: 2,                                                            // minimum distance from our target
                direction: 1                                                            // Which direction can we traverse the graph in (-1 incoming nodes, 0 both, 1 outgoing nodes)
            }
        )

        results.map(result => {                                                         // run the Paths array to compute the distances and weights of user and books
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
        return(res)
    }
}

module.exports = GraphService