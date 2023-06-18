"""
This file contains auxiliary functions
"""
import json
import streamlit as st
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
    except UnboundLocalError:
        st.warning("Please select a priority")


def edit_todo():
    pass


def complete_todo():
    pass

