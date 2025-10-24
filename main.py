import sys
import json
from pathlib import Path
import os
from helper import TaskManager


def main():

        
        # find and designate file path for json file
        cwd = os.getcwd()
        cdjson = cwd + "/to-do.json"
        cdjson = Path(cdjson)

        # create json file if not already exists
        if not cdjson.is_file():
               with open("to-do.json", "w") as f:
                        json.dump([], f, indent=4)
                        print(f"to-do.json initialised at {cdjson}")

        # write json to python dict
        with open("to-do.json", "r") as f:
                json_dict = json.load(f)
                manager = TaskManager(json_dict)
                if len(json_dict) == 0 and sys.argv[1] != "add":
                        return print("Remember to add a task first.")
        

        # adding tasks
        if sys.argv[1] == "add":
                if len(sys.argv) < 3:
                        return print("Make sure to specify a task.")
                else:
                        # add task to dict
                        manager.add_task(sys.argv[2])

        elif sys.argv[1] == "done":
               if len(sys.argv) < 3:
                        return print("Make sure to specify a task.")
               else:
                        # mark the task as Done
                        manager.done_task(sys.argv[2])

        # list all tasks
        elif sys.argv[1] == "list":
                if len(sys.argv) < 3:
                        manager.list_tasks("all")
                else:
                        manager.list_tasks(sys.argv[2])

        # delete a task
        elif sys.argv[1] == "delete":
                manager.delete_task(sys.argv[2])

        elif sys.argv[1] == "desc":
                manager.desc_task(sys.argv[2])

        # write dict as json to file
        manager.write_json()


if __name__ == "__main__":
    checklist = []
    main()
