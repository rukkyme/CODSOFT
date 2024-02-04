import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def save_tasks():
    task_list_contents = list(task_list.get(0, tk.END))
    with open("tasks.txt", "w") as file:
        for task in task_list_contents:
            file.write(task + "\n")
    #print("Tasks saved")
    messagebox.showinfo("Success", "Tasks saved")
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        print("No saved tasks found")
        return []

#add task
def add_task():
    task_text = task_entry.get()
    if len(task_text) == 0:
        return []
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task = f"{task_text} ({timestamp})"
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()


def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
        save_tasks()

def Task_completed():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.itemconfig(selected_task_index, {'bg': 'pink'})
        task_list.selection_clear(selected_task_index)
        save_tasks()

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("800x600")

#background configuration
root.configure(bg="#5F9EA0")


header_font = ("Brush Script MT", 30)
header_label = tk.Label(root,
    text="To-Do List",
    font=header_font,
    background="#ADD8E6",
    foreground="black"
)
header_label.pack(pady=20)

#This set the description for the entry text
entry_font = ("Consolas", "12", "bold")
task_entry = tk.Entry(root,  
    font=entry_font,
    width=70,
    background="white",
    foreground="black"
)
task_entry.pack()
#this 
task_list = tk.Listbox(root,
    selectmode=tk.SINGLE,
    background="white",
    foreground="blue"
)
task_list.pack(fill=tk.BOTH, expand=True)

# Load tasks from the file when the application starts
task_list_contents = load_tasks()
for task in task_list_contents:
    task_list.insert(tk.END, task)

#adding buttons and their descriptions
button_color = "#808080"
button_font = ("Brush Script MT", 14)
add_button = tk.Button(root, text="Add Task", command=add_task, bg=button_color, fg="white", font=button_font)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg=button_color, fg="white", font=button_font)
delete_button.pack()

complete_button = tk.Button(root, text="Task completed", command=Task_completed, bg=button_color, fg="white", font=button_font)
complete_button.pack()

# Adding optional elements
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=save_tasks)
filemenu.add_command(label="Load", command=lambda: load_and_insert_tasks())
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

def load_and_insert_tasks():
    task_list_contents = load_tasks()
    task_list.delete(0, tk.END)  # Clear existing tasks in the listbox
    for task in task_list_contents:
        task_list.insert(tk.END, task)

root.mainloop()
