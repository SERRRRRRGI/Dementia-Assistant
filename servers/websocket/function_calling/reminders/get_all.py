from api_helper import api_helper
from function_calling.function_parent_class import OpenAIFunction

description = {
    "name": "get_all_reminders",
    "description": "Get all existing reminders.",
}

class GetAllReminders(OpenAIFunction):

    @staticmethod
    def getName():
        return description["name"]

    def __init__(self):
        self.description = description
        self.meanwhile = ["Mmm...", "Un momenteeet..."]

    def apply(self, _):

        results = api_helper.reminders_db.get_all_reminders()

        return results