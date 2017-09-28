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

In this example, the TaskManager delegates the handling of each task to the TaskHandler.

#### Task

The `task.py` file defines a _Task_ object, which has a _type_ and a _message_. 

#### TaskManager

The `task_manager.py` file defines the _TaskManager_. A _TaskManger_ is initialized with a delegate that is of type _TaskManagerDelegate_. The _TaskManagerDelegate_ has defined methods that the _TaskManager_ can call.

The power here is that the _TaskManager_ doesn't care if its delegate is a plain _TaskManagerDelegate_, a _TaskHandler_, or a _SuperCustomTaskHandler_. It just knows that the protocol (or list of methods) defined by _TaskManagerDelegate_ are available.

When a new task is added to the _TaskManager_, it adds the task to its list of tasks, but delegates the handling of that task to its delegate.

#### TaskManagerDelegate

The `task_manager_delegate.py` file defines the _TaskManagerDelegate_. The _TaskManagerDelegate_ defines the protocol that a subclass should overwrite.

#### TaskHandler

The `task_handler.py` file defines the _TaskHandler_. The _TaskHandler_ is a subclass of _TaskManagerDelegate_. It must implement the protocol defined by the _TaskManagerDelegate_.