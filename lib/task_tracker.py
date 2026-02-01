class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def complete_task(self, task):
        if task not in self.tasks:
            raise ValueError(f"Task not found: {task}")
        
        self.tasks.remove(task)

        if len(self.tasks) == 0:
            return f"Task completed: {task}"
        return self.tasks
    
    def task_list(self):
        return self.tasks