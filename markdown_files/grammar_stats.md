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
"""
Given a text that starts with a capital letter and ends with a period
#check returns True
"""
stats = GrammarStats()
stats.check("Hello world.")  # => True

"""
Given a text that starts with a lowercase letter and ends with a period
#check returns False
"""
stats = GrammarStats()
stats.check("hello world.")  # => False

"""
Given a text that starts with a capital letter but does not end with a punctuation mark
#check returns False
"""
stats = GrammarStats()
stats.check("Hello world")  # => False

"""
Given a text that starts with a capital letter and ends with an exclamation mark
#check returns True
"""
stats = GrammarStats()
stats.check("Wow!")  # => True

"""
Given multiple texts checked, some passing and some failing
#percentage_good returns the percentage of texts that passed
"""
stats = GrammarStats()
stats.check("Hello.")       # passes
stats.check("hello.")       # fails
stats.check("How are you?") # passes
stats.percentage_good()     # => 66

"""
Given no texts checked
#percentage_good returns 0
"""
stats = GrammarStats()
stats.percentage_good()     # => 0

"""
Given all texts fail the check
#percentage_good returns 0
"""
stats = GrammarStats()
stats.check("hello")   # fails
stats.check("world")   # fails
stats.percentage_good() # => 0

"""
Given all texts pass the check
#percentage_good returns 100
"""
stats = GrammarStats()
stats.check("Hello.") # passes
stats.check("Wow!")   # passes
stats.percentage_good() # => 100

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
