from .vector_data_retrieval import VectorDataRetrieval
from .get_current_datetime import GetCurerntDatetime
from .function_parent_class import OpenAIFunction
from .get_tdr_conclusions import GetTDRConclusions

from .reminders.create import CreateReminder
from .reminders.update import UpdateReminder
from .reminders.delete import DeleteReminder
from .reminders.get_by_id import GetReminderById
from .reminders.get_all import GetAllReminders

from openai.types.chat import ChatCompletionMessage, ChatCompletionToolParam

from program_settings import verbose

import json
from threading import Thread

class FunctionHandler:
    def __init__(self):
        self.handler_array= [VectorDataRetrieval(), GetCurerntDatetime(), CreateReminder(), UpdateReminder(), DeleteReminder(), GetReminderById(), GetAllReminders(), GetTDRConclusions()]

        self.handlers = dict(zip([handler.getName() for handler in self.handler_array], self.handler_array))

        self.tools_array =  [self._description_to_tools(tool) for tool in self.handlers.values()] 
    
        if verbose: print("Available tools: ", list(self.handlers.keys()), "\n")

    def get_tools_array(self):
        return self.tools_array

    def _description_to_tools(self, function: OpenAIFunction) -> dict[str, str]:
        return {
                "type": "function",
                "function": function.description
            }
    
    def _handle_tool_call(self, index, tool_call: ChatCompletionToolParam, results):
        result = self.handlers[tool_call.function.name].apply(json.loads(tool_call.function.arguments))
        results[index] = result
        return result

    
    def handle(self, message: ChatCompletionMessage):
        if verbose: print("FUNCTION HANDLEING: ", message.tool_calls)

        results = [None] * len(message.tool_calls)
        threads = []

        for index, tool_call in enumerate(message.tool_calls):
            thread = Thread(target=self._handle_tool_call, args=(index, tool_call, results))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        result_messages = [{
            "role": "tool",
            "content": json.dumps(result),
            "tool_call_id": message.tool_calls[index].id
        } for index, result in enumerate(results)]

        if verbose: print("function handling result: ", result_messages)

        return result_messages