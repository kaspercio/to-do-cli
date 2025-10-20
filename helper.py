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
        if not self.list:
            new_id = 1
        else:
            new_id = max(task["id"] for task in self.list) + 1

        
        # create the new task object
        new_task = {
             "id": new_id,
             "title": task,
             "status": "to-do",
             "created_at": strftime("%a, %d %b %Y at %H:%M:%S", localtime()),
             "done_at": None,
        }
        
        # append the dictionary to the list
        self.list.append(new_task)

    def done_task(self, id):
        # for each task in the list
        id = int(id)
        for t in self.list:
            # update time and status if id matches
            if t["id"] == id:
                t["status"] = "Done"
                t["done_at"] = strftime("%a, %d %b %Y at %H:%M:%S", localtime())

    def list_tasks(self, filter):
        filtered_list = []
        if filter == "" or filter == "all":
            print(self.list)
        elif filter == "done":
            for t in self.list:
                if t["status"] == "Done":
                    filtered_list.append(t)
        elif filter == "to-do":
            for t in self.list:
                if t["status"] == "to-do":
                    filtered_list.append(t)
        elif filtered_list > 0:
            print(filtered_list)
            


         
         
