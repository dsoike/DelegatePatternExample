from .task import Task


class TaskManagerDelegate(object):

    def handle_task(self, task):
        # type: (Task) -> None
        raise NotImplementedError
