import unittest
from helper import TaskManager

class TestAddMethod(unittest.TestCase):
    def test_search(self):
        # sample JSON list
        tasks = [
            {
        "id": 1,
        "title": "walk the dog",
        "status": "Done",
        "created_at": "Mon, 20 Oct 2025 at 15:19:28",
        "done_at": None
    },
    {
        "id": 2,
        "title": "ride the bike",
        "status": "Done",
        "created_at": "Wed, 22 Oct 2025 at 12:04:04",
        "done_at": "Wed, 22 Oct 2025 at 12:14:48"
    },
    {
        "id": 4,
        "title": "do laundry",
        "status": "to-do",
        "created_at": "Wed, 22 Oct 2025 at 13:00:56",
        "done_at": None
    },
    {
        "id": 5,
        "title": "walk the dog",
        "status": "Done",
        "created_at": "Wed, 22 Oct 2025 at 13:01:28",
        "done_at": "Wed, 22 Oct 2025 at 13:34:29"
    },
    {
        "id": 6,
        "title": "take a hike",
        "status": "to-do",
        "created_at": "Wed, 22 Oct 2025 at 13:46:33",
        "done_at": None
    }
        ]
        
        manager = TaskManager(tasks)
        
        result = manager.binary_search(2)
        
        self.assertDictEqual(
        result, {
        "id": 2,
        "title": "ride the bike",
        "status": "Done",
        "created_at": "Wed, 22 Oct 2025 at 12:04:04",
        "done_at": "Wed, 22 Oct 2025 at 12:14:48"
    }, "machine broke"
    )