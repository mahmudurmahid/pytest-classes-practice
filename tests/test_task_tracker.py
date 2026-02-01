from lib.task_tracker import TaskTracker

"""
task_list method: when the tracker is new,
it returns an empty list
"""
def test_task_tracker_task_list_returns_empty_for_new_tracker():
    tracker = TaskTracker()
    
    result = tracker.task_list()
    assert result == []

"""
add_task method: when a new task is added,
the task list includes the task
"""
def test_task_tracker_add_task_adds_task_to_list():
    tracker = TaskTracker()
    tracker.add_task("Buy milk")
    
    result = tracker.task_list()
    assert result == ["Buy milk"]

"""
task_list method: when multiple tasks are added,
it returns all tasks in the order they were added
"""
def test_task_tracker_task_list_returns_tasks_in_order():
    tracker = TaskTracker()
    tracker.add_task("Buy milk")
    tracker.add_task("Walk the dog")
    tracker.add_task("Read book")
    
    result = tracker.task_list()
    assert result == ["Buy milk", "Walk the dog", "Read book"]

"""
complete_task method: when a single task is completed,
it removes the task and returns a completion message
"""
def test_task_tracker_complete_task_removes_task_and_returns_message():
    tracker = TaskTracker()
    tracker.add_task("Buy milk")
    
    result = tracker.complete_task("Buy milk")
    assert result == "Task completed: Buy milk"
    assert tracker.task_list() == []

"""
complete_task method: when multiple tasks exist,
it removes the specified task and leaves the others
"""
def test_task_tracker_complete_task_removes_only_specified_task():
    tracker = TaskTracker()
    tracker.add_task("Buy milk")
    tracker.add_task("Walk the dog")
    
    result = tracker.complete_task("Buy milk")
    assert result == ["Walk the dog"]
    assert tracker.task_list() == ["Walk the dog"]

"""
complete_task method: completing one task does not remove other tasks
"""
def test_task_tracker_complete_task_only_removes_completed_task():
    tracker = TaskTracker()
    tracker.add_task("Buy milk")
    tracker.add_task("Walk the dog")
    
    tracker.complete_task("Walk the dog")
    assert tracker.task_list() == ["Buy milk"]

"""
add_task method: allows adding an empty string task
"""
def test_task_tracker_add_task_allows_empty_string():
    tracker = TaskTracker()
    tracker.add_task("")
    
    result = tracker.task_list()
    assert result == [""]

"""
complete_task method: when the task does not exist,
it raises a ValueError
"""
def test_task_tracker_complete_task_raises_exception_for_missing_task():
    tracker = TaskTracker()
    tracker.add_task("Buy milk")
    
    with pytest.raises(ValueError, match="Task not found: Walk the dog"):
        tracker.complete_task("Walk the dog")