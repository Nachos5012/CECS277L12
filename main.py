# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 04/20/2024
# Module 12 - iterator
# Purpose - to create the tasklist class and use it to create a tasklist
import check_input
import tasklist

def main_menu():
  """
  Display the main menu options.

  Returns:
    choice: int
      the user's choice from the menu
  task:
  -TasklistTasks to complete: {}
  1. Display current task
  2. Display all tasks
  3. Mark current task complete
  4. Add new task
  5. Search by date
  6. Save and quit
  """
  
  print("1. Display current task\n2. Display all tasks\n3. Mark current task complete\n4. Add new task\n5. Search by date\n6. Save and quit")
  choice = check_input.get_int_range("Enter choice: ", 1, 6)
  return choice

def get_date():
  """Prompt the user to enter a date and return it."""
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  year = check_input.get_int_range("Enter year: ", 2000, 2100)
  return f"{month:02}/{day:02}/{year}"

def get_time():
  """Prompt the user to enter a time and return it."""
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)
  return f"{hour:02}:{minute:02}"

def main():
  """Main Function"""
  task_list = tasklist.Tasklist()
  while True:
    print("-Tasklist-")
    print(f"Tasks to complete: {len(task_list)}")
    choice = main_menu()
    if choice == 1:
      print(task_list.get_current_task())
      
    elif choice == 2:
      print("Tasks:")
      for i,task in enumerate(task_list, start=1):
        print(f"{i}. {task}")

    elif choice == 3:
      task_list.mark_complete()

    elif choice == 4:
      desc = input("Enter a task: ")
      print("Enter due date:")
      date = get_date()
      print("Enter time")
      time = get_time()
      task_list.add_task(desc, date, time)

    elif choice == 5:
      print("Enter date to search")
      date = get_date()
      print(f"Tasks due on {date}:")
      i = 1
      for task in task_list:
        if task.date == date:
          print(f"{i}. {task}")
          i += 1

    elif choice == 6:
      print("Saving List...")
      task_list.save_file()
      break

    if len(task_list) == 0:
      print("All tasks are complete!")
      break
    print()


main()
    

  



