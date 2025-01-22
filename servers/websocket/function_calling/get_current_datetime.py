from datetime import datetime
from function_calling.function_parent_class import OpenAIFunction

description = {
    "name": "get_current_datetime",
    "description": "Returns the current date (weekday, day, month and year) and hour (hours, minutes and seconds).",
}


class GetCurerntDatetime(OpenAIFunction):

    @staticmethod
    def getName():
        return description["name"]
    
    def _get_weekday(self):
        return ["Diumenge", "Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte"][int(datetime.now().strftime("%w"))]

    def __init__(self):
        self.description = description
        self.meanwhile = ["Mmm...", "Deixam pensar..."]

    def apply(self, query):
        date = datetime.now().strftime("%d-%m-%Y%H:%M:%S")
        
        return f"´{self._get_weekday()}, {date}"