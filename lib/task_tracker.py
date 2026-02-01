class TaskTracker:
    def __init__(self):
        # parameters: none
        # side effects: initialises an empty list of tasks 
        self.tasks = []

    def add_task(self, task):
        # parameters: (str) user adds a single task they want to complete later
        # returns: nothing
        # side effects: adds task to a list of tasks
        self.tasks.append(task)
    
    def complete_task(self, task):
        # parameters: (str) user completes a task
        # returns: completed task message or list of tasks still to do
        # side effects: removes task from list of tasks
        if task not in self.tasks:
            raise ValueError(f"Task not found: {task}")
        
        self.tasks.remove(task)

        if len(self.tasks) == 0:
            return f"Task completed: {task}"
        return self.tasks
    
    def task_list(self):
        # parameters: none
        # returns: (list) tasks yet to be completed
        # side effects: none
        return self.tasks