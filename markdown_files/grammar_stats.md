# GrammarStats Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user, I want to check if a text has proper sentence capitalization and punctuation so that I can ensure my sentences follow basic grammar rules

As a user, I want to see the percentage of texts that passed the grammar check so that I can monitor my overall grammar quality

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class GrammarStats:
    def __init__(self):
        """
        paramaters - none
        returns - none
        side-effects - none
        """
        pass

    def check(self, text):
        """
        parameters - string of text
        returns - a boolean value that states True if the text begins with a capital letter and ends with a sentence-ending punctuation mark, false otherwise
        side-effects - none
        """
        pass

    def percentage_good(self):
        """
        parameters - none
        returns - the percentage of texts checked so far that passed the check defined in the `check` method. The number 55 represents 55%
        side-effects - none
        """
        pass

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
