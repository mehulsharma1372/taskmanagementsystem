"""This module is to ad or make changes in the existing tasks."""

# from task import Task
from user_interface import UserInteraction


class TaskManager(UserInteraction):

    def __init__(self):

        self.all_taks = {}

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
                    name = input(print("Please give the Name of the task you want to view"))
                    print(self.all_taks[name])
                    # print(self.all_taks[print(input("Please give the Name of the task you want to view."))])

                except KeyError:
                    print("No task with this name.")

            elif response == "U":
                update_name = input(print("Please give the task name you want to update:"))
                self.update_task(update_name)
            


        return self.all_taks

s = TaskManager()

print(s.interact())