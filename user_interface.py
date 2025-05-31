"""This module contains the user interaction."""

# from task import Task
# from task_manager import TaskManager


class UserInteraction():

    def __init__(self):
        pass

    def take_input(self):
        input_data = {}
        # input_data["title_id"] = num
        input_data["title"] = input(print("Name of the task:"))
        input_data["description"] = input(print("Description of the task:"))
        input_data["status"] = input(print("Status(Complete/Pending):"))
        print(input_data)
        return input_data
    
    def times(self):
        return input(print("How many datum you want to add or modify."))
        

    def ask(self):

        return input(print("Press A to add, U to update and V to view. To end, press E"))

        



