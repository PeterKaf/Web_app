"""
This file contains auxiliary functions
"""
import json
FILENAME = "todos.json"


def read_json(filename=FILENAME):
    """
    Initiates json read funcitons,
    :param filename: relative path to the file
    :return: List of dictionaries
    """
    with open("todos.json", 'r') as file:
        content = file.read()
    return json.loads(content)


def write_json(value, filename=FILENAME):
    """
    Saves specified string into json file
    :param filename: relative path to the file
    :param value: string of an entry to be saved in json
    :return: None
    """
    pass

