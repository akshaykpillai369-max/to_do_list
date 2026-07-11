import streamlit as st

class Menu:

    def __init__(self, db):

        self.db = db

    def add_task(self):

        task_name = st.text_input("Enter The Task Name")

        options = st.selectbox(label="Select the urgency", options="High🔴, Medium🟡, Low🟢")

        submit = st.button("Save Task")

        if submit:
            if task_name and options:
                self.db.add_task(task_name, options)
                st.success("Task added successfully")

            else:

                st.error("Please fill the fields")

