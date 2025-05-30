"""This module contains Class Task and is responsible for taking all the data and returning task in string format."""

class Task:

    def __init__(self, title_id, title, description, status, created_at, updated_at ):

        self.title_id = title_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def task_info(self):

        print ("Here are the task details:""\n" , self.title, "\n" , self.description, "\n" , self.status, "\n", self.created_at, "\n")
        

# c = Task(34,56,3434,76,45,87)

# c.task_info()