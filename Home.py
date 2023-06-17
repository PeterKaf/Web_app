import streamlit as st
import functions as fun


def main():
    data = fun.read_json()
    sorted_todos = sorted(data, key=lambda x: (x['due_date'], x['priority']))
    priorities = {"High": False, "Medium": False, "Low": False}
    st.title("Todo App")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Select the priority:**")
        for priority, selected in priorities.items():
            priorities[priority] = st.checkbox(priority, selected)
        if sum(priorities.values()) > 1:
            st.warning("Please select only one option")
    with col2:
        st.markdown("**Pick a deadline:**")
        selected_date = st.date_input("Select a date")  # YYYY-MM-DD
    with col3:
        st.markdown("**Submit a Todo:**")
        entry_box = st.text_input(label="**Enter the activity you want to add:**",
                                  placeholder="Enter here...")
    st.subheader("Currnet Todos:")
    for todo in sorted_todos:
        st.checkbox(todo["task"])


if __name__ == '__main__':
    main()
