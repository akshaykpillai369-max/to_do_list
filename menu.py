import streamlit as st

class Menu:

    def __init__(self, db):

        self.db = db

    def add_task(self):

        st.subheader("Add Task")

        task_name = st.text_input("Enter The Task Name")

        options = st.selectbox(label="Select the urgency", options="High🔴, Medium🟡, Low🟢")

        submit = st.button("Save Task")

        if submit:
            if task_name and options:
                self.db.add_task(task_name, options)
                st.success("Task added successfully")

            else:

                st.error("Please fill the fields")
    
    def edit_task(self):

        st.subheader("Edit Task")

        sl_no = st.number_input("Enter the ID", min_value=1, step=1)

        task_name = st.text_input("Enter The Task Name")

        options = st.selectbox(label="Select the urgency", options="High🔴, Medium🟡, Low🟢")

        submit = st.button("Edit Task")

        if submit:
            if task_name and options and sl_no:
                self.db.edit_task(task_name, options)
                st.success("Task edited successfully")

            else:

                st.error("Please fill the fields")


    def delete_task(self):

        st.subheader("Delete Task")

        sl_no = st.number_input("Enter the ID", min_value=1, step=1)

        submit = st.button("Delete Task",type="primary")

        if submit:
            if sl_no:
                self.db.delete_task(sl_no)
                st.success("Task deleted successfully")

            else:

                st.error("Please fill the fields")

    def show_all_tasks(self):

        st.subheader("Ongoing Tasks")
        self.db.show_tasks()


