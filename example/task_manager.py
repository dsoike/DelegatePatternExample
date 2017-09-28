from typing import List
from .task_manager_delegate import TaskManagerDelegate
from .task import Task


class TaskManager(object):

    def __init__(self, delegate):
        # type: (TaskManagerDelegate) -> None

        self._delegate = delegate
        self._tasks = []  # type: List[Task]

    def add_task(self, task):
        # type: (Task) -> None

        self._tasks.append(task)
        self._delegate.handle_task(task)
