import json
import yaml
import sys
import os
from enum import Enum


class Mode(str, Enum):
    REMOVED = "removed"
    ADDED = "added"
    CHANGED = "changed"
    EQUAL = "equal"
    NESTED = "nested"


def compare(data1, data2):
    """ Compare data of two files"""
    res = {}
    removed_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()
    common_keys = data1.keys() & data2.keys()
    for key in removed_keys:
        res[key] = (Mode.REMOVED, data1[key])
    for key in added_keys:
        res[key] = (Mode.ADDED, data2[key])
    for key in common_keys:
        val1 = data1[key]
        val2 = data2[key]
        if isinstance(val1, dict) and isinstance(val2, dict):
            value = (Mode.NESTED, compare(val1, val2))
        elif val1 == val2:
            value = (Mode.EQUAL, val1)
        else:
            value = (Mode.CHANGED, (val1, val2))
        res[key] = value
    return res


def convert_file(file):
    _, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        res = json.load(open(file))
    elif file_extension == '.yml' or file_extension == '.yaml':
        res = yaml.safe_load(open(file))
    else:
        sys.exit('Invalid name (.json .yml .yaml are supported)')
    return res


def generate_diff(first_file, second_file, format_mode):
    data1 = convert_file(first_file)
    data2 = convert_file(second_file)
    unformatted_diff = compare(data1, data2)
    return format_mode(unformatted_diff)
