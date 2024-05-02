class Task():
  """ 
  attributes:
    description: string description of the task
    date: due date of the task. Is formatted as MM/DD/YYYY
    time: time the task is due (formatted as HH:MM)
    
  """

  def __init__(self, description, date, time):
    self.description = description
    self.date = date
    self.time = time

  def __str__(self):
    """Return a formatted string of the task."""
    return f"{self.description} - \nDue: {self.date} at {self.time}"

  def __repr__(self):
    """Return a string representation of the task."""
    return f"{self.description},{self.date},{self.time}"

  def __lt__(self, other):
    """Compare two tasks based on their dates and times."""
    if self.date[6:10] == other.date[6:10]:
      if self.date[0:2] == other.date[0:2]:
        if self.date[3:5] == other.date[3:5]:
          if self.time[0:2] == other.time[0:2]:
            if self.time[3:5] == other.time[3:5]:
              return self.description < other.description
            else:
              return self.time[3:5] < other.time[3:5]
          else:
            return self.time[0:2] < other.time[0:2]
        else:
          return self.date[3:5] < other.date[3:5]
      else:
        return self.date[0:2] < other.date[0:2]
    else:
      return self.date[6:10] < other.date[6:10]
