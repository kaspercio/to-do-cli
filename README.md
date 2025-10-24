# To Do CLI
A simple To Do list CLI with CRUD operations written in Python.

## Features
Add tasks to a list
Remove tasks from a list
Read the list of tasks
Track which tasks are completed or to do
Read specific tasks from the list

## Installation

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
todo
|
|-- ```add YOUR TASK TITLE```
    e.g. add "Check emails"
|-- ```delete YOUR TASK ID```
|-- ```desc YOUR TASK ID```
|-- ```done YOUR TASK ID```
|-- ```list TASK STATUS```

## Requirements
Python 3.10.12

## Author
kaspercio
