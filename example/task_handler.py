from .task_manager_delegate import TaskManagerDelegate
from .task import Task


class TaskHandler(TaskManagerDelegate):

    def handle_task(self, task):
        # type: (Task) -> None

        print('TaskHandler is handling task with type=' + task.type + ' message=' + task.message)
