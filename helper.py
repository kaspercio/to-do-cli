import json

class TaskManager:
    
    def __init__(self, diction):
        self.diction = diction

    def write_json(self):
        with open("to-do.json", "w") as f:
                json.dump(self.diction, f, indent=4)

    def add_task(self, task):
        self.diction[task] = "In progress"

    def done_task(self, task):
        del self.diction[task]
        self.diction[task] = "Done"
         
         
