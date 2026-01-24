# Task Tracker Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TaskTracker:
    def __init__(self):
        # parameters: none
        # side effects: initialises an empty list of tasks 
        pass # No code here yet

    def add_task(self, task):
        # parameters: (str) user adds a single task they want to complete later
        # returns: nothing
        # side effects: adds task to a list of tasks
        pass # No code here yet
    
    def complete_task(self, task):
        # parameters: (str) user completes a task
        # returns: completed task message or list of tasks still to do
        # side effects: removes task from list of tasks
        pass # No code here yet
    
    def task_list(self):
       # parameters: none
       # returns: (list) tasks yet to be completed
       # side effects: none
       pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a new task tracker
#task_list returns an empty list
"""
tracker = TaskTracker()
tracker.task_list()  # => []

"""
Given a new task tracker
#add_task adds a task to the task list
"""
tracker = TaskTracker()
tracker.add_task("Buy milk")
tracker.task_list()  # => ["Buy milk"]

"""
Given a task tracker with multiple tasks
#task_list returns all tasks in the order they were added
"""
tracker = TaskTracker()
tracker.add_task("Buy milk")
tracker.add_task("Walk the dog")
tracker.add_task("Read book")
tracker.task_list()  # => ["Buy milk", "Walk the dog", "Read book"]

"""
Given a task tracker with one task
#complete_task removes the task and returns a completion message
"""
tracker = TaskTracker()
tracker.add_task("Buy milk")
tracker.complete_task("Buy milk")
# => "Task completed: Buy milk"
tracker.task_list()  # => []

"""
Given a task tracker with multiple tasks
#complete_task removes the specified task and returns remaining tasks
"""
tracker = TaskTracker()
tracker.add_task("Buy milk")
tracker.add_task("Walk the dog")
result = tracker.complete_task("Buy milk")
# => ["Walk the dog"]
tracker.task_list()  # => ["Walk the dog"]

"""
Given a task tracker with multiple tasks
#complete_task only removes the completed task
"""
tracker = TaskTracker()
tracker.add_task("Buy milk")
tracker.add_task("Walk the dog")
tracker.complete_task("Walk the dog")
tracker.task_list()  # => ["Buy milk"]

"""
Given a task tracker
#add_task allows an empty string task
"""
tracker = TaskTracker()
tracker.add_task("")
tracker.task_list()  # => [""]

"""
Given a task tracker without the specified task
#complete_task raises an exception
"""
tracker = TaskTracker()
tracker.add_task("Buy milk")
tracker.complete_task("Walk the dog")
# raises an error with the message "Task not found."

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
