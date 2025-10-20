import json
from time import localtime, strftime

class TaskManager:
    
    def __init__(self, list):
        self.list = list

    def write_json(self):
        with open("to-do.json", "w") as f:
                json.dump(self.list, f, indent=4)

    def add_task(self, task):
        
        # initialise id of new task
        id = len(self.list) + 1
        
        # create the new task object
        new_task = {
             "id": id,
             "title": task,
             "status": "to-do",
             "created_at": strftime("%a, %d %b %Y at %H:%M:%S", localtime()),
             "done_at": None,
        }
        
        # append the dictionary to the list
        self.list.append(new_task)

    def done_task(self, id):
        # for each task in the list
        for t in self.list:
            id = int(id)
            # update time and status if id matches
            if t["id"] == id:
                t["status"] = "Done"
                t["done_at"] = strftime("%a, %d %b %Y at %H:%M:%S", localtime())
         
         
