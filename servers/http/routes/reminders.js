import {Router} from "express"
import { db } from "../lib/mongodb.js"
import { ObjectId } from "mongodb"

export const remindersRoutes = Router()

// CREATE: Add a new item
remindersRoutes.post("/", async (req, res) => {
  const collection = db.collection('reminders-eloi-buil-cuadrat-3000')

  try {
    const newItem = req.body;

    console.log("NEW ITEM: ", newItem)

    if(!newItem) { return res.status(400).send({ error: {message: 'Request has no body'} });  }
    if(!newItem.title) { return res.status(400).send({ error: {message: 'Title is required'} });  }
    if(!newItem.description) { return res.status(400).send({ error: {message: 'Description is required'} });  }
    if(!newItem.frequency) { return res.status(400).send({ error: {message: 'Frequency is required'} });  }
    if(!["once", "multiple"].find(el => el === newItem.frequency)) { return res.status(400).send({ error: {message: 'Frequency value field is not within "once" or "multiple"'} });  }

    if(newItem.date) newItem.date = new Date(newItem.date)
    if(newItem.expires) newItem.expires = new Date(newItem.expires)
    if(newItem.starts) newItem.starts = new Date(newItem.starts)


    const result = await collection.insertOne(newItem);
    console.log(JSON.stringify(result, null, 2))
    res.status(201).send({id: result.insertedId}); // Return the inserted item
  } catch (err) {
    console.error(err)
    res.status(500).send({ error: {message: 'Failed to add item'} });
  }
});

// READ: Get all items
remindersRoutes.get("/", async (req, res) => {
  const collection = db.collection('reminders-eloi-buil-cuadrat-3000')

  try {
    const items = await collection.find().toArray();
    res.status(200).send(items);
  } catch (err) {
    console.error(err)
    res.status(500).send({ error: {message: 'Failed to get items'} });
  }
});

// READ: Get a single item by ID
remindersRoutes.get("/:id", async (req, res) => {
  const collection = db.collection('reminders-eloi-buil-cuadrat-3000')

  try {
    const { id } = req.params;
    const item = await collection.findOne({ _id: id });
    if (item) {
      res.status(200).send(item);
    } else {
      res.status(404).send({ error: {message: 'Item not found'} });
    }
  } catch (err) {
    console.error(err)
    res.status(500).send({ error: {message: 'Failed to get item'} });
  }
});

// UPDATE: Update an item by ID
remindersRoutes.put("/:id", async (req, res) => {
  const collection = db.collection('reminders-eloi-buil-cuadrat-3000')

  try {
    const { id } = req.params;
    const updatedItem = req.body;
    const result = await collection.updateOne(
      { _id: id },
      { $set: updatedItem }
    );
    if (result.matchedCount > 0) {
      res.status(200).send({ message: 'Item updated' });
    } else {
      res.status(404).send({ error: {message: 'Item not found'} });
    }
  } catch (err) {
    console.error(err)
    res.status(500).send({ error: {message: 'Failed to update item'} });
  }
})

// DELETE: Delete an item by ID
remindersRoutes.delete("/:id", async (req, res) => {
  const collection = db.collection('reminders-eloi-buil-cuadrat-3000')

  try {
    const { id } = req.params;
    const result = await collection.deleteOne({ _id: new ObjectId(id) });
    if (result.deletedCount > 0) {
      res.status(200).send({ message: 'Item deleted' });
    } else {
      res.status(404).send({ error: {message: 'Item not found'} });
    }
  } catch (err) {
    console.error(err)
    res.status(500).send({ error: {message: 'Failed to delete item'} });
  }
})