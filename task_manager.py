"""This module is to ad or make changes in the existing tasks."""

from task import Task
from user_interface import UserInteraction


class TaskManager(Task, UserInteraction):

    def __init__(self):

        self.all_taks = {}

    def add_task(self):
        input = self.take_input
        self.all_taks[input["title"]] = input

    def interact(self):
            
        for _ in range(int(self.times())):

            if self.ask() == "A":
                self.add_task()

            elif self.ask() == "U":
                pass

            elif self.ask() == "E":
                
