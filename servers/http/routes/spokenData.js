import {Router} from "express"
import { openaiHelper } from "../lib/openai.js"
import { db } from "../lib/mongodb.js"

export const spokenDataRoutes = Router()

spokenDataRoutes.post("/document", async (req, res) => {
  const spokenDataCollection = db.collection('spoken-data-eloi-buil-cuadrat-3000')
  const confidentialDataCollection = db.collection('confidential-data-eloi-buil-cuadrat-3000')

  if (!req?.body) {
    return res.status(400).json({error: { message: "Request has no body"}})
  }
  console.log(req.body)
  
  const {text, date, speaker, confidential, inConversation} = req.body

  const embedding = await openaiHelper.generateEmbedding(text)

  console.log("embedding: ", embedding)

  const doc = { speaker, text, date: new Date(date), embedding, inConversation }
  
  try {
    await spokenDataCollection.insertOne(doc)

    if(confidential && Object.keys(confidential).length) {
      const keys = Object.keys(confidential)
      const confidentialDocs = keys.map((key) => {
        return {
          key,
          value: confidential[key]
        }
      })

      await confidentialDataCollection.insertMany(confidentialDocs)
    }
  } catch (e) {
    console.error(e)
    return res.status(500).json({error: { message: "Failed to save document"}})
  }

  res.status(201).json({
    message: "Document saved successfully",
    data: doc,
  })
})

spokenDataRoutes.post("/search", async (req, res) => {
  const collection = db.collection('spoken-data-eloi-buil-cuadrat-3000')
  if (!req.body) return res.status(400).json({error: { message: "Request has no body"}})

  const text = req.body?.text
  const date = req.body?.date
  const speaker = req.body?.speaker

  if (!text &&!date &&!speaker) return res.status(400).json({error: { message: "No search criteria provided"}})

  let filter = {}

  if (speaker) filter['speaker'] = speaker
  if (date) {
    filter.date = {}
    if (date?.lte) filter.date['$lte'] = new Date(date.lte)
    if (date?.gte) filter.date['$gte'] = new Date(date.gte)
  }

  let query = [,{
    '$project': {
      '_id': 0,
      'date': 1,
      'speaker': 1,
      'text': 1,
      'score': {
        '$meta': 'vectorSearchScore'
      }
    }
  }]

  if (text) {
    const embedding = await openaiHelper.generateEmbedding(text)

    query[0] = {
      '$vectorSearch': {
        'index': 'default',
        'path': 'embedding',
        'queryVector': embedding,
        'numCandidates': 250,
        'limit': 7,
        'filter': filter
      }
    }
    
  } else {
    query[0] = {
      '$match': filter
    }
  }

  console.log(JSON.stringify(query, null, 2))

  const result = await collection.aggregate(query).toArray()

  res.status(200).json(result)

})