import streamlit as st

class Menu:

    def __init__(self, db):

        self.db = db

    def show_sidebar(self):

        st.sidebar.header("To Do List")
        decision = st.sidebar.radio(label="Select from the options", options= ["Show All Tasks", "Add Task", "Edit Task", "Delete Task"])
        return decision
    

    def add_task(self):

        st.subheader("Add Task")

        with st.form("add_task", clear_on_submit=True):

            task_name = st.text_input("Enter The Task Name")

            options = st.selectbox(label="Select the urgency", options=["High🔴", "Medium🟡", "Low🟢"], index=None)

            submit = st.form_submit_button("Save Task")

            if submit:
                if task_name and options:
                    self.db.add_task(task_name, options)
                    st.success("Task added successfully")

                else:

                    st.error("Please fill the fields")
    
    def edit_task(self):

        st.subheader("Edit Task")

        with st.form("add_task", clear_on_submit=True):

            sl_no = st.number_input("Enter the ID", min_value=1, step=1)

            task_name = st.text_input("Enter The Task Name")

            options = st.selectbox(label="Select the urgency", options=["High🔴", "Medium🟡", "Low🟢"], index= None)

            submit = st.form_submit_button("Edit Task")

            if submit:
                if task_name and options and sl_no:

                    self.db.edit_task(task_name, options, sl_no)
                    st.success("Task edited successfully")

                else:

                    st.error("Please fill the fields")
        
        


    def delete_task(self):

        st.subheader("Delete Task")

        with st.form("add_task", clear_on_submit=True):

            sl_no = st.number_input("Enter the ID", min_value=1, step=1)

            submit = st.form_submit_button("Delete Task",type="primary")

            if submit:
                if sl_no:
                    self.db.delete_task(sl_no)
                    st.success("Task deleted successfully")

                else:

                    st.error("Please fill the fields")

    def show_all_tasks(self):

        st.subheader("Ongoing Tasks")

        columns = st.columns(3)
        results = self.db.show_tasks()

        if results:

            for index, result in enumerate(results):

                with columns[index % 3] :

                    with st.container(border= True) :

                        st.markdown(f"### TITLE : {results[index][1]}")
                        st.write(f"**Priority** : {results[index][2]}")
                        st.write(f"**ID** : {results[index][0]}")
        else:
            st.warning("**No Tasks Added!, Consider Adding One!**")


