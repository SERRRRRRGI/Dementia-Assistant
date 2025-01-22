import express, {Router} from "express"
import morgan from "morgan"

import { authMiddleware } from "./middleware/auth.js"
import { spokenDataRoutes } from "./routes/spokenData.js"
import { remindersRoutes } from "./routes/reminders.js"

const app = express()

const baseLevelRouter = Router()
 
const apiRouter = Router()

apiRouter.use(express.json())
apiRouter.use(authMiddleware)
apiRouter.use("/spokenData", spokenDataRoutes)
apiRouter.use("/reminders", remindersRoutes)

baseLevelRouter.use("/api", apiRouter)
baseLevelRouter.get("/", (req, res) => res.status(200).send("online"))

app.use(baseLevelRouter)
app.use(morgan())

export default app