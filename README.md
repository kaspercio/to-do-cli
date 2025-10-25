# To Do CLI
A simple To Do list CLI with CRUD operations written in Python.

## How it works
The script manipulates a JSON file that contains array of JSON objects. 
This is done by writing a list of dictionaries into Python, manipulating the data within, and rewriting the data back into the JSON file. 

## Features
Add tasks to a list
Remove tasks from a list
Read the list of tasks
Track which tasks are completed or to do
Read specific tasks from the list

## Installation
Run the following in your terminal to install the cli with pip package manager.
```pip install git+https://github.com/YOUR_USERNAME/todo-cli.git```

## Usage

### Data
Data is stored in a JSON file in the following format:

```
[
    {
        "id": 1,
        "title": "take a walk",
        "status": "to-do",
        "created_at": "Fri, 24 Oct 2025 at 11:24:57",
        "done_at": null
    },
    {
        "id": 3,
        "title": "clean the kitchen",
        "status": "to-do",
        "created_at": "Fri, 24 Oct 2025 at 12:13:40",
        "done_at": null
    }
]
```

### Commands
To pass commands to the cli, do todo and pass arguments first for the operation parameter (add, delete, desc) then specify an attribute (Task ID, Task title, or Task status).

todo
|
|-- ```add YOUR TASK TITLE```
    Creates a dictionary with id, title, status, date created and date done. e.g. todo add "Check emails".
|-- ```delete YOUR TASK ID```
    Deletes dictionary with specified task id from the list.
|-- ```desc YOUR TASK ID```
    Returns the dictionary with specified task id from the list.
|-- ```done YOUR TASK ID```
    Updates dictionary with specified task id with Done status.
|-- ```list TASK STATUS```
    Returns a list of dictionaries with matching task status, if no status argument is given returns the whole list.

## Requirements
Python 3.10.12

## Author
kaspercio
