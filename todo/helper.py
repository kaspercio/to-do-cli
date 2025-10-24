import json
from time import localtime, strftime, time
import time

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
        print("New task {0} {1} has been added to the list.".format(new_task["id"], new_task["title"]))
    
    # mark specific task as done
    def done_task(self, id):
        t = self.binary_search(id)
        t["status"] = "Done"
        t["done_at"] = strftime("%a, %d %b %Y at %H:%M:%S", localtime())
        print("Task {0} {1} is {2} at {3}".format(t["title"], t["id"], t["status"], t["done_at"]))
    
    # print a list of dictionaries of specified status
    def list_tasks(self, filter):
        filtered_list = []
        if filter == "" or filter == "all":
            print(*self.list, sep='\n')
        elif filter == "done":
            for t in self.list:
                if t["status"] == "Done":
                    filtered_list.append(t)
        elif filter == "to-do":
            for t in self.list:
                if t["status"] == "to-do":
                    filtered_list.append(t)
        elif filtered_list > 0:
            print("The following are {0}: {1}".format(t["status"], filtered_list))
    
    # remove specific task from list
    def delete_task(self, id):
        t = self.binary_search(id)
        temp_1 = id
        temp_2 = t["title"]
        self.list.remove(t)
        print(f"Task {temp_1}: {temp_2} has been removed.")
        print(f"Your new list: {self.list}")
    
    # print the id and dictionary of task
    def desc_task(self, id):
        t = self.binary_search(id)   
        print(f"Here is task {id}: {t}")
    
    # find task from a list of dictionaries
    def binary_search(self, id):
        id = int(id)
        mid = len(self.list) // 2
        start = time.time()
        while(self.list[mid]["id"] != id and time.time() - start < 0.15):
            if self.list[mid]["id"] > id:
                mid = mid // 2
            else:
                mid = mid + (len(self.list) - mid) // 2
        
        if self.list[mid]["id"] == id:
                return self.list[mid]
        else:
            return print(f"Timeout: Task {id} likely does not exist.")


            


         
         
