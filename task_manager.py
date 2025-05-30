"""This module is to ad or make changes in the existing tasks."""
from task import Task


class TaskManager(Task):

    def __init__(self):
        super().__init__(self.title_id, self.title, self.description, self.status, self.created_at, self.updated_at)
        self.all_taks = {}


    def add_task(self, input):

        self.all_taks[input["title"]] = input

    


    