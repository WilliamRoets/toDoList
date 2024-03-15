import tkinter as tk
from tkinter import simpledialog

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tasks = []
        self.title("Task Manager")
        self.geometry("400x300")

        self.task_listbox = tk.Listbox(self, height=10, width=50)
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(self, width=50)
        self.task_entry.pack(pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(button_frame, text="Delete", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=10)

        update_button = tk.Button(button_frame, text="Update", command=self.update_task)
        update_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            pass

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_entry.get()
            if task != "":
                self.tasks[index] = task
                self.update_listbox()
                self.task_listbox.selection_set(index)
                self.task_entry.delete(0, tk.END)
        except IndexError:
            pass

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()

    

       