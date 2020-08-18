const ug = require('ug')
const { DataHelper } = require('./DataHelper')

const graph = new ug.Graph()
const dh = new DataHelper()

const users = dh.getUsers()
const books = dh.getBooks()
const genres = dh.getGenres()
const purchased = dh.getPurchased()
const interested = dh.getInterested()
const belongs = dh.getBelongs()


users.forEach(obj => graph.createNode('user', obj))
books.forEach(obj => graph.createNode('book', obj))
genres.forEach(obj => graph.createNode('genre', obj))

purchased.forEach(obj => {
    graph.createEdge('purchased')
        .link(
            graph.nodes('user').query().filter({ id: obj.outputId }).first(),
            graph.nodes('book').query().filter({ id: obj.inputId }).first()
        ).setDistance(1)
})

interested.forEach(obj => {
    graph.createEdge('interested')
        .link(
            graph.nodes('user').query().filter({ id: obj.outputId }).first(),
            graph.nodes('genre').query().filter({ id: obj.inputId }).first()
        ).setDistance(2)
})

belongs.forEach(obj => {
    graph.createEdge('belongs')
        .link(
            graph.nodes('book').query().filter({ id: obj.outputId }).first(),
            graph.nodes('genre').query().filter({ id: obj.inputId }).first(),
            true
        ).setDistance(2)
})

graph.save('./graph.ugd', () => {
    console.log('saved')
})

let results = graph.closest(
    graph.nodes('user').query().filter({ id: 1 }).first(), 
    {
        compare: node => { return node.entity === 'book' },
        minDepth: 2,
        count: 100
    }
)

let resultNodes = results.map(path => {
    console.log(path)
    // faz calculos
})