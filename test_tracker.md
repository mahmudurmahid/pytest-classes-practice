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
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
