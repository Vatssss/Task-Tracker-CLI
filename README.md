# 🧾 Task Tracker CLI

A **Command-Line Task Tracker** that allows you to **add, update, delete, and manage tasks** directly from your terminal.
This project helps you practice **file handling**, **user input processing**, and **building a CLI app** using **Python** — without any external libraries.

---

## 🚀 Features

* Add new tasks
* Update or delete existing tasks
* Mark tasks as **in progress** or **done**
* List all tasks or filter by status
* Data persistence using a **JSON file**
* Handles errors and edge cases gracefully

---

## 🧠 Project Overview

The **Task Tracker** is a simple CLI tool for tracking your to-do items, progress, and completed tasks.
It runs entirely through the command line and stores data locally in `tasks.json`.

Each task includes:

* `id` — Unique identifier for the task
* `description` — Short task summary
* `status` — Current task state (`todo`, `in-progress`, `done`)
* `createdAt` — Timestamp of task creation
* `updatedAt` — Timestamp of last modification

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required

---

## 📦 Installation & Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **Run the script:**

   ```bash
   python task-cli.py <command> <arguments>
   ```

3. The app will automatically create a `tasks.json` file in the current directory (if it doesn’t exist).

---

## ⚙️ Command Usage

### ➕ Add a new task

```bash
python task-cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### ✏️ Update a task

```bash
python task-cli.py update 1 "Buy groceries and cook dinner"
# Output: (ID:1) updated successfully
```

### ❌ Delete a task

```bash
python task-cli.py delete 1
# Output: Task deleted successfully.
```

### 🔄 Mark task as in-progress

```bash
python task-cli.py mark-in-progress 1
# Output: Task (ID:1) marked in progress.
```

### ✅ Mark task as done

```bash
python task-cli.py mark-done 1
# Output: Task (ID:1) marked as done.
```

### 📋 List all tasks

```bash
python task-cli.py list
```

### 🗂️ List tasks by status

```bash
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done
```

---

## 🧪 Example Output

```bash
ID: 1, Description: Buy groceries, Status: todo, Created At: 2025-10-08T12:32:45, Updated At: 2025-10-08T12:32:45
ID: 2, Description: Write report, Status: in-progress, Created At: 2025-10-08T13:01:15, Updated At: 2025-10-08T14:10:33
```

---

## 🧩 File Structure

```
📂 task-tracker-cli
 ├── task-cli.py           # Main CLI script
 ├── tasks.json            # Task data storage
 └── README.md             # Project documentation
```

---

## 🧑‍💻 Implementation Details

* Uses **Python’s built-in modules**: `os`, `json`, `sys`, and `datetime`.
* Stores all tasks in a local **JSON file** (`tasks.json`).
* Uses **positional arguments** for command-line input.
* Each command updates the JSON file immediately.
* Handles invalid inputs and missing files gracefully.

---

## 🧪 Example Development Steps

1. Set up your development environment (VSCode, PyCharm, etc.).
2. Create your project directory and initialize Git.
3. Implement commands one by one:

   * `add` → `list` → `update` → `delete` → `mark-in-progress` → `mark-done`.
4. Test each command to ensure correct JSON updates.
5. Clean and refactor your code before final submission.

---

## 📄 Sample `tasks.json` Output

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2025-10-08T12:32:45",
        "updatedAt": "2025-10-08T12:32:45"
    },
    {
        "id": 2,
        "description": "Write report",
        "status": "in-progress",
        "createdAt": "2025-10-08T13:01:15",
        "updatedAt": "2025-10-08T14:10:33"
    }
]
```

---

## 🧫 Future Improvements

* Add task priority levels
* Add task due dates and reminders
* Add search and filtering options
* Add color-coded terminal outputs

---

## 🏁 Conclusion

The **Task Tracker CLI** is a minimal yet powerful project that strengthens your understanding of:

* File handling with JSON
* Command-line input processing
* Building real-world CLI tools without frameworks

---

## 👨‍💻 Author

**Vatsal Saxena**
📧 [vatsalsaxena1@gmail.com](mailto:vatsalsaxena1@gmail.com)
🔗 [GitHub](https://github.com/Vatssss) • [LinkedIn](https://www.linkedin.com/in/vatsal-saxena-10mar04/)
* Project Idea URL: [https://roadmap.sh/projects/task-tracker](url) 
