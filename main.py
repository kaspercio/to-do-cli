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

        # write json to python dict
        with open("to-do.json", "r") as f:
                json_dict = json.load(f)
                manager = TaskManager(json_dict)
        

        # create json file if not already exists
        if not cdjson.is_file():
               with open("to-do.json", "w") as f:
                        print(f"to-do.json initialised at {cdjson}")

        # adding tasks
        if sys.argv[1] == "add":
                
                # add task to dict
                manager.add_task(sys.argv[2])

        elif sys.argv[1] == "done":
               
               # mark the task as Done
               manager.done_task(sys.argv[2])



        # write dict as json to file
        manager.write_json()


if __name__ == "__main__":
    checklist = []
    main()
