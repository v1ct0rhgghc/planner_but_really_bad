class Planner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, deadline):
        self.tasks.append({"task": task, "deadline": deadline})
        print(f"Task '{task}' added with deadline {deadline}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the planner.")
            return
        print("Tasks in the planner:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['task']} (Deadline: {task['deadline']})")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed from the planner.")
        else:
            print("Invalid task number.")

# Example usage
def main():
    planner = Planner()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            planner.add_task(task, deadline)
        elif choice == '2':
            planner.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            planner.remove_task(task_number)
        elif choice == '4':
            print("Exiting the planner.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
