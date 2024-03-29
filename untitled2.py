# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GCy9__YJVsgVa8c5HALoRObeMuOUynYK
"""

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description, priority=0):
        self.tasks[description] = priority

    def remove_task(self, description):
        if description in self.tasks:
            del self.tasks[description]
        else:
            print("Task not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for idx, (description, priority) in enumerate(self.tasks.items(), start=1):
                print(f"{idx}. {description} - Priority: {priority}")

    def prioritize_task(self, description, priority):
        if description in self.tasks:
            self.tasks[description] = priority
        else:
            print("Task not found.")

    def recommend_task(self):
        if not self.tasks:
            print("No tasks.")
        else:
            sorted_tasks = sorted(self.tasks.items(), key=lambda x: x[1], reverse=True)
            print("Recommended Task:")
            print(f"{sorted_tasks[0][0]} - Priority: {sorted_tasks[0][1]}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Task")
        print("5. Recommend Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (0-10): "))
            task_manager.add_task(description, priority)
        elif choice == "2":
            description = input("Enter task description to remove: ")
            task_manager.remove_task(description)
        elif choice == "3":
            task_manager.list_tasks()
        elif choice == "4":
            description = input("Enter task description to prioritize: ")
            priority = int(input("Enter new priority (0-10): "))
            task_manager.prioritize_task(description, priority)
        elif choice == "5":
            task_manager.recommend_task()
        elif choice == "6":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()