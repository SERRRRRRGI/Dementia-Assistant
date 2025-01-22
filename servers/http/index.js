import http from "node:http"
import {config} from "./config.js"
import app from "./expressServer.js"

const server = http.createServer(app)

server.listen(config.PORT, () => {
  console.log(`
Dementia Assistant server initialized successfully!

Listening on port ${config.PORT}
`)
})