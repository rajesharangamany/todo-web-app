
import streamlit as st
import os
# File path to Desktop
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
#FILENAME = os.path.join(desktop, "to-do.txt")
FILENAME = to-do.txt

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# View tasks
def view_tasks():
    if not st.session_state.tasks:
        st.info("✅ No tasks in your list!")
    else:
        st.subheader("📝 Your To-Do List:")
        for i, task in enumerate(st.session_state.tasks, start=1):
            st.write(f"{i}. {task}")

# Add task
def add_task():
    new_task = st.text_input("Enter the new task:")
    if st.button("Add"):
        if new_task.strip():
            st.session_state.tasks.append(new_task.strip())
            st.success(f"✅ Added task: {new_task}")
        else:
            st.warning("⚠️ Task cannot be empty.")

# Remove task
def remove_task():
    if not st.session_state.tasks:
        st.info("❌ No tasks to remove.")
        return
    task_number = st.number_input("Enter task number to remove:",
                                  min_value=1, max_value=len(st.session_state.tasks), step=1)
    if st.button("Remove"):
        removed = st.session_state.tasks.pop(task_number - 1)
        save_tasks(st.session_state.tasks)  # Auto-save after removal
        st.success(f"🗑️ Removed task: {removed}")

# Initialize tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

    # Title
st.title("🧠 To-Do List Web Menu")

# Menu dropdown simulating terminal input
menu_option = st.selectbox("Choose an option:",
                           ["Select...", "1. View Tasks", "2. Add Task", "3. Remove Task", "4. Save & Exit"])

# Dispatch based on menu option
if menu_option == "1. View Tasks":
    view_tasks()

elif menu_option == "2. Add Task":
    add_task()

elif menu_option == "3. Remove Task":
    remove_task()

elif menu_option == "4. Save & Exit":
    save_tasks(st.session_state.tasks)
    st.success(f"💾 Tasks saved to: {FILENAME}")
    st.balloons()
