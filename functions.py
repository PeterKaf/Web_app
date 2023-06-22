import json
import streamlit as st
import time
FILENAME = "todos.json"


def read_json(filename=FILENAME):
    """
    Retrieves todos from json file, creates one if there is none present.
    :param filename: relative path to the file FILENAME by default.
    :return: List of dictionaries
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return json.loads(content)
    except FileNotFoundError:
        # Create a new file with "[]"
        with open(filename, 'w') as file:
            file.write("[]")
        st.experimental_rerun()


def write_json(value, filename=FILENAME):
    """
    Updates json file with new entry.
    :param value: single entry to json file (dictionary).
    :param filename: relative path to the file FILENAME by default.
    :return: None
    """
    with open(filename, 'r') as f:
        existing_data = json.load(f)

    existing_data.append(value)

    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)


class TodoManager:
    def __init__(self, filename=FILENAME):
        """
        Constructor, sets filename to default value.
        :param filename: relative path to the file FILENAME by default.
        :return: None
        """
        self.filename = filename

    def add_todo(self, priorities_dict):
        """
        Reads the priority checkbox values, date, and name of a to-do and passes it to added to json file. Handles edge
        cases. Refactors user-friendly name for numerical one.
        :param priorities_dict: dictionary containing state of priority checkboxes.
        :return: None
        """
        for priority, value in priorities_dict.items():
            if value:
                tmp_priority = priority
        try:
            if tmp_priority == "High":
                num_priority = 0
            elif tmp_priority == "Medium":
                num_priority = 1
            else:
                num_priority = 2

            todo = {
                "task": st.session_state["enter_todo"],
                "priority": num_priority,
                "due_date": str(st.session_state["deadline"])
            }

            write_json(todo, self.filename)
            st.success("Todo added successfully")
            time.sleep(1)
            st.experimental_rerun()
        except UnboundLocalError:
            st.warning("Please select a priority")

    def edit_todo(self, data, checkbox_values):
        """
        Reads the to-dos from checkbox and string from text_box, switches selected to-dos with provided string.
        :param data: list containing contents of a checkboxes (to-do name)
        :param checkbox_values: list containing sorted (as they appear) boolean values for checkboxes
        :return: None
        """
        if True in checkbox_values:
            keys_to_edit = []
            for key, entry in enumerate(data):
                if checkbox_values[key]:
                    keys_to_edit.append(key)

            if keys_to_edit:
                for key in sorted(keys_to_edit, reverse=True):
                    data[key]['task'] = st.session_state["edit_todo"]

                with open(self.filename, 'w') as f:
                    json.dump(data, f, indent=4)
                st.success("Todo changed")
                time.sleep(1)
                st.experimental_rerun()
        else:
            st.warning("Please select one or more todos you wish to edit")

    def complete_todo(self, data, checkbox_values):
        """
        Reads the to-dos from checkbox and string from text_box, switches selected to-dos with provided string.
        :param data: list containing contents of a checkboxes (to-do name)
        :param checkbox_values: list containing sorted (as they appear) boolean values for checkboxes
        :return: None
        """
        if True in checkbox_values:
            keys_to_delete = []
            for key, entry in enumerate(data):
                if checkbox_values[key]:
                    keys_to_delete.append(key)

            if keys_to_delete:
                for key in sorted(keys_to_delete, reverse=True):
                    del data[key]

                with open(self.filename, 'w') as f:
                    json.dump(data, f, indent=4)
                st.success("Completed a todo/todos")
                time.sleep(1)
                st.experimental_rerun()
        else:
            st.warning("Select one or more todos you wish to complete")
