const express = require('express')
const GraphService = require('./GraphService')

const router = express.Router()
const gs = new GraphService()


router.get('/favicon.ico', (req, res) => res.status(204))

router.get('/:id', (req, res) => {
    try {
        res.json(gs.getRecommendation(parseInt(req.params.id)))
    } catch(e) {
        res.status(500).json(e)
    }
})

module.exports = router