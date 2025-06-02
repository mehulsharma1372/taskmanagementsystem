"""This module is to ad or make changes in the existing tasks."""

# from task import Task
from user_interface import UserInteraction
import json
import datetime



class TaskManager(UserInteraction):

    def __init__(self):

        self.all_taks = self.from_json()

    def add_task(self):
        input = self.take_input()
        self.all_taks[input["title"]] = input

    def update_task(self, name):
        key = input(print("What do you want to update in", name))
        if key in self.all_taks.keys:
            new_response = input(print("What is the new value."))
            self.all_taks[name][key] = new_response

        else:
            print("No such entri in data")

    def interact(self):

        for _ in range(int(self.times())):

            response = self.ask()

            if response == "A":
                self.add_task()

            elif response == "E":
                print("Ending Session")
                break

            elif response == "V":
                try:
                    name = input(
                        print("Please give the Name of the task you want to view")
                    )
                    print(self.all_taks[name])
                    # print(self.all_taks[print(input("Please give the Name of the task you want to view."))])

                except KeyError:
                    print("No task with this name.")

            elif response == "U":
                update_name = input(
                    print("Please give the task name you want to update:")
                )
                self.update_task(update_name)

            elif response == "D":
                try:
                    delete_name = input(
                        print("Give the name of the task you want to delete.")
                    )
                    del self.all_taks[delete_name]

                except KeyError as k:
                    print("This name is not in the task list.")

        return self.all_taks

    def from_json(slef):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:

            data = {}

        return data
    
    def to_json(self):


        with open("tasks.json", "w") as f:
            json.dump(self.all_taks, f)


s = TaskManager()

print(s.interact())
s.to_json()
