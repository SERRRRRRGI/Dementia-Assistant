from api_helper import api_helper
from function_calling.function_parent_class import OpenAIFunction

description = {
    "name": "internal_data_search",
    "description": "Search through all the things that have been said throughout all the conversations that the device has witnessed. Call this when you need context about things that have been said in the past outside the current conversation. At least one of the parameters must be specified.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "A question to be answered or a similar text to the one that you want to search for in the internal data. Ex: Which is somebody's favourite color? If not provided, the search will just be constrained by the other 2 parameters."
            },
            "date": {
                "type": "object",
                "properties": {
                    "lte": {
                        "type": "string",
                        "format": "date",
                        "description": "The date from which stops searching for the text. If not provided, the search will stop from the latest available data."
                    },
                    "gte": {
                        "type": "string",
                        "format": "date",
                        "description": "The date from which starts searching for the text. If not provided, the search will start from the earliest available data."
                    }
                }
            },
            "speaker": {
                "type": "string",
                "description": "The name of the person who has spoken. If not provided, the search will include all the people who have spoken."
            },
        },
        "additionalProperties": False,
    },
}

class VectorDataRetrieval(OpenAIFunction):

    @staticmethod
    def getName():
        return description["name"]

    def __init__(self):
        self.description = description
        self.meanwhile = ["Mmm...", "Deixam pensar..."]

    def apply(self, query):
        # Implementation to retrieve data from the vector database based on the query
        # Returns a list of relevant documents
        results = api_helper.spoken_data_db.search_document(query=query)

        return results