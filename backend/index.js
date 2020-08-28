const server = require('express')
const routes = require('./routes')
const cors = require('cors')


// create server instance
const app = new server()

// allow cors
app.use(cors())

// load routes
app.use(routes)

// start to listen at port 8000
app.listen(8000, () => {
    console.log(`Server is listening at port 8000`)
})