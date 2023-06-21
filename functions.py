"""
This file contains settings and helper functions
"""
import json
import streamlit as st
import time
FILENAME = "todos.json"


def read_json(filename=FILENAME):
    """
    Initiates json read funcitons,
    :param filename: relative path to the file
    :return: List of dictionaries
    """
    with open(filename, 'r') as file:
        content = file.read()
    return json.loads(content)


def write_json(value, filename=FILENAME):
    """
    Saves specified string into json file
    :param filename: relative path to the file
    :param value: dictionary representing one entry in json
    :return: None
    """
    # Load existing JSON data from file
    with open(filename, 'r') as f:
        existing_data = json.load(f)

    # Append new data to the existing data list
    existing_data.append(value)

    # Write the updated data back to the JSON file
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)


def add_todo(priorities_dict):
    """
    Appends a to-do into data dictionary and json file via write_json function
    :param priorities_dict: dictionary with information on set statuses of priority checkbox
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

        todo = {"task": st.session_state["enter_todo"], "priority": num_priority,
                "due_date": str(st.session_state["deadline"])}

        write_json(todo)
        st.success("Todo added successfuly")
        time.sleep(1)
        st.experimental_rerun()
    except UnboundLocalError:
        st.warning("Please select a priority")


def edit_todo(data, checkbox_values):
    if True in checkbox_values:
        # Get the keys of selected entries to delete
        keys_to_edit = []
        for key, entry in enumerate(data):
            if checkbox_values[key]:
                keys_to_edit.append(key)

        if keys_to_edit:
            # Delete the selected entries
            for key in sorted(keys_to_edit, reverse=True):
                data[key]['task'] = st.session_state["edit_todo"]

            # Write the updated data back to the JSON file
            with open(FILENAME, 'w') as f:
                json.dump(data, f, indent=4)
            st.success("Todo changed")
            time.sleep(1)
            st.experimental_rerun()
    else:
        st.warning("Please select one or more todos you wish to edit")


def complete_todo(data, checkbox_values):
    if True in checkbox_values:
        # Get the keys of selected entries to delete
        keys_to_delete = []
        for key, entry in enumerate(data):
            if checkbox_values[key]:
                keys_to_delete.append(key)

        if keys_to_delete:
            # Delete the selected entries
            for key in sorted(keys_to_delete, reverse=True):
                del data[key]

            # Write the updated data back to the JSON file
            with open(FILENAME, 'w') as f:
                json.dump(data, f, indent=4)
            st.success("Completed a todo/todos")
            time.sleep(1)
            st.experimental_rerun()
    else:
        st.warning("Select a one or more todos you wish to complete")
