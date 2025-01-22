from api_helper import api_helper
from function_calling.function_parent_class import OpenAIFunction

description = {
    "name": "update_reminder",
    "description": "Update a reminder that already exists. Pass the fields you want to update with their new value.",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {
                "type": "number",
                "description": "ID of the reminder to update."
            },
            "frequency": {
                "type": "string",
                "enum": ["once", "multiple"],
                "description": "Once if the event will just happen once, multiple for a dayly or weekly reminder."
            },
            "title": {
                "type": "string",
                "description": "Title of the reminder."
            },
            "description": {
                "type": "string",
                "description": "Description of the reminder accurate enough for the user to know what has to be done."
            },
            "date": {
                "type": "string",
                "format": "date",
                "description": "Only for frequency=once. Date of the reminder (day and hour)."
            },
            "starts": {
                "type": "string",
                "format": "date",
                "description": "Only for frequency=multiple. Date in which the reminder starts to take effect. If not provided it starts to take effect emidiately."
            },
            "expires": {
                "type": "string",
                "format": "date",
                "description": "Only for frequency=multiple. Date in which the reminder expires. If not provided it never expires."
            },
            "weekdays": {
                "type": "array",
                "description": "Array representing each weekday starting from Sunday and ending on Saturday.Each day must contain an object specifying when the reminder appears or false, if that they the reminder doesn't have to appear.",
                 "oneOf": [
                        {
                            "type": "array",
                            "description": "The hours the reminder appears.",
                            "items": {
                                "type": "string",
                                "format": "time",
                                "description": "The time the reminder appears. The format must be hour, minutes, and seconds."
                            },
                            "maxItems": 40,
                            "minItems": 1
                        },
                        {
                            "type": "boolean",
                            "enum": [False],
                            "description": "Set to false if no reminder should appear on this day."
                        }
                    ],
                "minItems": 7,
                "maxItems": 7
            },
            "doneDuration": {
                "type": "string",
                "format": "time",
                "description": "Only for frequency=multiple. The time that the done state lasts after completing a task."
            },
            "tellBeforeDuration": {
                "type": "string",
                "format": "time",
                "description": "Amount of time before the reminder's actual time that the user will be first notified"
            },
            "nextReminding": {
                "type": "string",
                "format": "date",
                "description": "Next time that the user will be reminded of the reminder. It can be changet each time the user is reminded."
            }
        },
    },
    "required": ["id"],
    "additionalProperties": False,
}

class UpdateReminder(OpenAIFunction):

    @staticmethod
    def getName():
        return description["name"]

    def __init__(self):
        self.description = description
        self.meanwhile = ["Mmm...", "Un momenteeet..."]

    def apply(self, object):
        id = int(object.pop("id"))
        results = api_helper.reminders_db.update_reminder(id=id, update_fields=object)

        return results