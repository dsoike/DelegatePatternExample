import time
from example.task import Task
from example.task_manager import TaskManager
from example.task_handler import TaskHandler

print('\nExample Starting\n')

# initialize the task handler
task_handler = TaskHandler()

# initialize the task manager, passing in the task handler as the delegate
task_manager = TaskManager(task_handler)

# create some tasks
tasks = [
    Task('normal', 'Do a flip.'),
    Task('normal', 'Spin around.'),
    Task('normal', 'Sing a song.'),
    Task('normal', 'Clap your hands.'),
    Task('normal', 'Jump really high.'),
]

# add each task to the task handler
for task in tasks:
    time.sleep(5)
    task_manager.add_task(task)

print('\nExample Completed\n')
