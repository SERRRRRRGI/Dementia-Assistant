from api_helper import api_helper
from function_calling.function_parent_class import OpenAIFunction

description = {
    "name": "get_reminder",
    "description": "Get a reminder that already exists.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {
                "type": "number",
                "description": "ID of the reminder to delete."
            }
        },
        "required": ["id"],
        "additionalProperties": False,
    },
}

class GetReminderById(OpenAIFunction):

    @staticmethod
    def getName():
        return description["name"]

    def __init__(self):
        self.description = description
        self.meanwhile = ["Mmm...", "Un momenteeet..."]

    def apply(self, obj):
        id=obj["id"]

        results = api_helper.reminders_db.get_reminder(id=id)

        return results