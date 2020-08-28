const express = require('express')
const GraphService = require('./GraphService')
const DataHelper = require('./helpers/DataHelper')

const users = new DataHelper().getUsers()
const router = express.Router()
const gs = new GraphService()


router.get('/favicon.ico', (req, res) => res.status(204))

// default endpoint to get books recommendations
router.get('/:username', (req, res) => {
    try {
        const user = users.find(item => item.name == req.params.username)            // get user id using username received in req.params
        res.json(gs.getRecommendation(parseInt(user.id)))
    } catch(e) {
        console.log(e)
        res.status(500).json(e)
    }
})

module.exports = router