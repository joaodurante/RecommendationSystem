const users = require('./data/users.json')
const books = require('./data/books.json')
const genres = require('./data/genres.json')
const purchased = require('./data/purchased.json')
const interested = require('./data/interested.json')
const belongs = require('./data/belongs.json')

class DataHelper {
    getUsers() {
        return users.data
    }

    getBooks() {
        return books.data
    }

    getGenres() {
        return genres.data
    }

    getPurchased() {
        return purchased.data
    }

    getInterested() {
        return interested.data
    }

    getBelongs() {
        return belongs.data
    }
}

module.exports = { DataHelper }