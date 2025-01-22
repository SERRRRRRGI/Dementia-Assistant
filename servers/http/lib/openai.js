import { config } from "../config.js"
import OpenAI from "openai"

const openai = new OpenAI({apiKey: config.OPENAI_API_KEY})

class OpenAIHelper {
  constructor(openai) {
    this.openai = openai
  }

  async generateEmbedding(text) {
    const response = await openai.embeddings.create({
      model: "text-embedding-3-small",
      input: text,
      encoding_format: "float",
    });
  
    return response.data[0].embedding
  }
}

export const openaiHelper = new OpenAIHelper(openai)