import streamlit as st
from database import Database
from menu import Menu

def main():
    db = Database()
    menu = Menu(db)

    result = menu.show_sidebar()

    st.title("To Do List✅")

    if result == "Show All Tasks":
        menu.show_all_tasks()

    elif result == "Add Task":
        menu.add_task()

    elif result == "Edit Task":
        menu.edit_task()
    
    elif result == "Delete Task":
        menu.delete_task()


if __name__ == "__main__":
    main()