import task

class Tasklist():
  """ 
  attributes:
    tasklist - list of tasks
    n - counter
  """

  def __init__(self):
    """Initialize the Tasklist with an empty list of tasks."""
    self.tasklist = []
    with open("tasklist.txt", "r") as file:
      for line in file:
        parts = line.strip().split(",")
        description, date, time = parts
        t = task.Task(description, date, time)
        self.tasklist.append(t)
    self.tasklist.sort()

  def add_task(self, desc, date, time):
    """Add a new task to the task list."""
    t = task.Task(desc, date, time)
    self.tasklist.append(t)
    self.tasklist.sort()

  def get_current_task(self):
    """Get the current task in the list."""
    return f"Current task is: \n{self.tasklist[0]}"

  def mark_complete(self):
    """Mark the current task as complete and move to the next task."""
    current_task = self.tasklist[0]
    self.tasklist.pop(0)
    if len(self.tasklist) > 0:
      print(f"Marking current task as complete: \n{current_task}\nNew current task is: \n{self.tasklist[0]}")
    elif len(self.tasklist) == 0:
      print(f"Marking current task as complete: \n{current_task}")

  def save_file(self):
    """Save the task list to a file."""
    with open("tasklist.txt", "w") as file:
      for t in self.tasklist:
        file.write(repr(t) + '\n')

  def __len__(self):
    """Return the number of tasks in the task list."""
    
    return len(self.tasklist)

  def __iter__(self):
    """Initialize the iterator."""
    self.n = 0
    return self

  def __next__(self):
    """Get the next task in the list."""
    if self.n < len(self.tasklist):
      task = self.tasklist[self.n]
      self.n += 1
      return task
    else:
      raise StopIteration