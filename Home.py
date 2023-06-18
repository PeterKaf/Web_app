import streamlit as st
import functions as fun


def main():
    data = fun.read_json()
    sorted_todos = sorted(data, key=lambda x: (x['due_date'], x['priority']))
    priorities = {"High": False, "Medium": False, "Low": False}
    st.title("Todo App")

    with st.form(key="form1"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Select the priority:**")
            for priority, selected in priorities.items():
                priorities[priority] = st.checkbox(priority, selected)
            if sum(priorities.values()) > 1:
                st.warning("Please select only one option")
        with col2:
            st.markdown("**Pick a deadline:**")
            selected_date = st.date_input("**Select a date**", key="deadline")  # YYYY-MM-DD
        with col3:
            st.markdown("**Submit a Todo:**")
            entry_box = st.text_input(label="**Enter the activity you want to add:**",
                                      placeholder="Enter here...", key="enter_todo")

            if st.form_submit_button("Submit"):
                fun.add_todo(priorities)

    with st.form(key="form2"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Current Todos:")
            for i, todo in enumerate(sorted_todos):
                st.checkbox(todo["task"], key=todo)
        with col2:
            st.subheader("")
            st.write("")
            edit_box = st.text_input(label="**Replace with:**",
                                     placeholder="Enter here...", key="edit_todo")
            finish_button = st.form_submit_button("Complete a todo")
            if finish_button:
                pass
        with col3:
            st.subheader("")
            st.subheader("")
            st.subheader("")

            edit_button = st.form_submit_button("Edit a todo")
            if edit_button:
                pass

    st.session_state


if __name__ == '__main__':
    main()
