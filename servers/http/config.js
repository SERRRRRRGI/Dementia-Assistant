import dotenv from "dotenv"
dotenv.config()

export const config = {
  PORT: process.env.PORT || 8080,
  DANGEROUSLY_SET_AUTHENTICATION_STRING: process.env.AUTH_STRING,
  OPENAI_API_KEY: process.env.OPENAI_API_KEY,
  MONGODB_URI: process.env.MONGODB_URI,
  MONGODB_DB_NAME: process.env.MONGODB_DB_NAME
}