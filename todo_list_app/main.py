import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = entry.get().strip()
    if task == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

# Function to delete selected task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showerror("Selection Error", "No task selected!")

# Function to clear all tasks
def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="📝 My To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

# Entry for new task
entry = tk.Entry(root, font=("Helvetica", 14), width=25)
entry.pack(pady=10)

# Add Task Button
add_btn = tk.Button(root, text="Add Task", command=add_task, width=15, bg="#4CAF50", fg="white")
add_btn.pack(pady=5)

# Task Listbox
listbox = tk.Listbox(root, font=("Helvetica", 14), width=30, height=10, selectbackground="#a6a6a6")
listbox.pack(pady=10)

# Delete and Clear Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

delete_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task, width=15, bg="#f44336", fg="white")
delete_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear All", command=clear_all, width=15, bg="#2196F3", fg="white")
clear_btn.grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()
