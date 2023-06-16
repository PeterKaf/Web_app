import streamlit as st
import functions as fun


def main():
    data = fun.read_json()
    st.title("Todo App")
    col1, col2, col3 = st.columns(3)
    with col1:
        entry_box = st.text_input(label="**Enter the activity you want to add:**",
                                  placeholder="Enter the activity you want to add:",
                                  label_visibility="hidden")
    with col2:
        st.markdown("**Select the priority:**")
        for entry in data:
            st.checkbox(entry["priority"])
    with col3:
        st.markdown("**Pick a deadline:**")


if __name__ == '__main__':
    main()
