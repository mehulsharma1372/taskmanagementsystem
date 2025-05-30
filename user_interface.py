"""This module contains the user interaction."""

from task import Task
from task_manager import TaskManager


class UserInteraction():

    # def __init__(self, title_id, title, description, status, created_at, updated_at):
    #     super().__init__(title_id, title, description, status, created_at, updated_at)
    #     self.input_data = {}

    def __init__(self):
        self.input_data = {}

    def take_input(self, num):
        self.input_data["title_id"] = num
        self.input_data["title"]  = input(print("Name of the task:"))
        self.input_data["description"] = input(print("Description of the task:"))
        self.input_data["satus"]  = input(print("Status(Complete/Pending):"))


c = UserInteraction()

c.take_input("1")
print(c.input_data)
