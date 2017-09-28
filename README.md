# DelegatePatternExample

This example project demonstrates basic use of the delegate pattern.

## Getting Started

#### Clone this Repository

```
$ cd <directory where you want to clone this repository>
$ git clone https://github.com/dsoike/DelegatePatternExample.git
```

#### Run the Example

```
$ cd ~/DelegatePatternExample
$ pip install requirements.txt
$ python run_example.py
```

## The Delegate Pattern

In delegation, an object handles a request by delegating to a second object (the delegate).

In this example, the TaskManager delegates the handling of each task to the TaskHandler (a subclass of TaskManagerDelegate). 

See `run_example.py` for details on how an object (TaskManager) and its delegate (TaskHandler) interact.

#### Task `task.py`

A _Task_ object has a _type_ and a _message_. 

#### TaskManager `task_manager.py`

The _TaskManger_ is initialized with a delegate that is of type _TaskManagerDelegate_. The _TaskManagerDelegate_ has defined methods that the _TaskManager_ can call.

The power here is that the _TaskManager_ doesn't care if its delegate is a plain _TaskManagerDelegate_, a _TaskHandler_ (subclass of _TaskManagerDelegate_), or a _SuperCustomTaskHandler_. It just knows that the protocol (or list of methods) defined by _TaskManagerDelegate_ are available.

When a new task is added to the _TaskManager_, it adds the task to its list of tasks, but delegates the handling of that task to its delegate.

#### TaskManagerDelegate `task_manager_delegate.py`

The _TaskManagerDelegate_ defines the protocol (or list of methods) that are available for the _TaskManager_ to delegate to.

#### TaskHandler `task_handler.py`

The _TaskHandler_ is a subclass of _TaskManagerDelegate_. It implements the protocol (overwrites the methods) defined by the _TaskManagerDelegate_.