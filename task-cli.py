import os
import json
import sys
from datetime import datetime

# Setting up Data Storage

TASK_FILE = "tasks.json"

# check if tasks.json exists
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as f:
        json.dump([], f)
    print("Created a tasks.json file")
else:
    print("From tasks.json")

# loading list from json file to python for manipulation
with open(TASK_FILE, "r") as f:
    tasks = json.load(f)

# CLI argument handling using sys.argv
if len(sys.argv) < 2:
    print("Invalid Command")
    sys.exit()
else:
    command = sys.argv[1]
    args = sys.argv[2:]

# # Adding a new task
# task-cli add "Buy groceries"
# # Output: Task added successfully (ID: 1)
if command == "add":
    if args:
        description = args[0]
        
        # finding max existing ID
        if not tasks:
            maxId = 0
        else:
            maxId = max(task['id'] for task in tasks)
            
        # creating new ID
        newId = maxId + 1
        
        # date-time 
        timeNow = datetime.now().isoformat(sep="T", timespec="seconds")
        
        # creating new task as a dictionary
        newTask = {
            'id' : newId,
            'description' : description,
            'status' : "todo",
            'createdAt' : timeNow,
            'updatedAt' : timeNow
        }
        
        # appending new task into the tasks list
        tasks.append(newTask)
        
        # updating the json file with new tasks list
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
        
        # output
        print(f"Task added successfully (ID:{newId})")
    
    # Invalid inputs
    else:
        print("Task description required.")

# # Updating and deleting tasks
# task-cli update 1 "Buy groceries and cook dinner"
# task-cli delete 1
if command == "update":
    if len(args) >= 2:
        taskId = args[0]
        newDescription = args[1]
        
        # checking for the task with the given taskID
        for task in tasks:
            if int(taskId) == task['id']:
                task['description'] = newDescription
                task['updatedAt'] = datetime.now().isoformat(sep="T", timespec="seconds")
        
        # updating the json file with updated tasks list
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
            
        # output
        print(f"(ID:{taskId}) updated successfully")
        
    # Invalid inputs
    else:
        print("Task ID and new description required.")

if command == "delete":
    if args:
        delId = int(args[0])
        
        # create a new task list excluding the delId task
        tasks = [task for task in tasks if task['id'] != delId]
        
        # updating the json file with new tasks list
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
            
        # output
        print("Task deleted successfully.")
    
    # Invalid inputs
    else:
        print("Task ID required.")

# # Marking a task as in progress or done
# task-cli mark-in-progress 1
# task-cli mark-done 1
if command == "mark-in-progress":
    if args:
        markId = int(args[0])
        for task in tasks:
            if markId == task['id']:
                task['status'] = "in-progress"
                task['updatedAt'] = datetime.now().isoformat(sep="T", timespec="seconds")
        
        # updating the json file with updated status
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
        
        # output   
        print(f"Task (ID:{markId}) marked in progress.")

    # Invalid inputs
    else:
        print("Task ID required.")

if command == "mark-done":
    if args:
        markId = int(args[0])
        for task in tasks:
            if markId == task['id']:
                task['status'] = "done"
                task['updatedAt'] = datetime.now().isoformat(sep="T", timespec="seconds")
        
        # updating the json file with updated status
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
        
        # output 
        print(f"Task (ID:{markId}) marked as done.")
        
    # Invalid inputs   
    else:
        print("Task ID required.")

# # Listing all tasks
# task-cli list

# # Listing tasks by status
# task-cli list done
# task-cli list todo
# task-cli list in-progress

if command == "list":
    if args:
        filters = args[0]
        filteredTasks = [task for task in tasks if task['status']==filters]
    else:
        filteredTasks = tasks
    
    if not filteredTasks:
        print("No tasks found.")
    else:
        for task in filteredTasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")