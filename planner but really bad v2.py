import tkinter as tk
from tkinter import messagebox

class Planner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, deadline):
        self.tasks.append({"task": task, "deadline": deadline})

    def view_tasks(self):
        if not self.tasks:
            return "No tasks in the planner."
        tasks_list = "Tasks in the planner:\n"
        for i, task in enumerate(self.tasks, 1):
            tasks_list += f"{i}. {task['task']} (Deadline: {task['deadline']})\n"
        return tasks_list

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            return f"Task '{removed_task['task']}' removed from the planner."
        else:
            return "Invalid task number."

class PlannerApp:
    def __init__(self, root):
        self.planner = Planner()
        self.root = root
        self.root.title("Planner App")

        self.task_label = tk.Label(root, text="Task")
        self.task_label.grid(row=0, column=0)
        self.task_entry = tk.Entry(root)
        self.task_entry.grid(row=0, column=1)

        self.deadline_label = tk.Label(root, text="Deadline (YYYY-MM-DD)")
        self.deadline_label.grid(row=1, column=0)
        self.deadline_entry = tk.Entry(root)
        self.deadline_entry.grid(row=1, column=1)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=2, column=0)

        self.view_tasks_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_tasks_button.grid(row=2, column=1)

        self.remove_task_label = tk.Label(root, text="Task Number to Remove")
        self.remove_task_label.grid(row=3, column=0)
        self.remove_task_entry = tk.Entry(root)
        self.remove_task_entry.grid(row=3, column=1)

        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=4, column=0, columnspan=2)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=5, column=0, columnspan=2)

    def add_task(self):
        task = self.task_entry.get()
        deadline = self.deadline_entry.get()
        self.planner.add_task(task, deadline)
        messagebox.showinfo("Success", f"Task '{task}' added with deadline {deadline}.")
        self.clear_entries()

    def view_tasks(self):
        tasks = self.planner.view_tasks()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, tasks)

    def remove_task(self):
        try:
            task_number = int(self.remove_task_entry.get())
            result = self.planner.remove_task(task_number)
            messagebox.showinfo("Result", result)
        except ValueError:
            messagebox.showerror("Error", "Invalid task number.")
        self.clear_entries()

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.remove_task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlannerApp(root)
    root.mainloop()
