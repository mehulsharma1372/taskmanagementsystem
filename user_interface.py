"""This module contains the user interaction."""

from task import Task
from task_manager import TaskManager


class UserInteraction(Task):

    def __init__(self):
        pass

    def take_input(self, num):
        input_data = {}
        self.input_data["title_id"] = num
        self.input_data["title"] = input(print("Name of the task:"))
        self.input_data["description"] = input(print("Description of the task:"))
        self.input_data["satus"] = input(print("Status(Complete/Pending):"))
        return input_data
    
    def times(self):
        return input(print("How many datum you want to add or modify."))
        

    def ask(self):

        return input(print("Press A to add, U to update and V to view. To end, press E"))

        


c = UserInteraction()

c.take_input("1")
print(c.input_data)
