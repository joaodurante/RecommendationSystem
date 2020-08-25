const server = require('express')
const bodyParser = require('body-parser')
const routes = require('./routes')


const app = new server()
app.use(routes)

app.listen(8000, () => {
    console.log(`Server is listening at port 8000`)
})

