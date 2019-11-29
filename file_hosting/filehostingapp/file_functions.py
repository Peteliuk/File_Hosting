import os
import re
import random

# Find base folder
basedir = os.path.abspath(os.path.dirname(__file__))

# Allowed file's formats
ALLOWED_EXTENSIONS = set(['txt',
                          'pdf',
                          'png',
                          'jpg',
                          'jpeg',
                          'gif',
                          'doc',
                          'docx',
                          'ppt',
                          'csv',
                          'xls'])


def allowed_extentions():
    return list(ALLOWED_EXTENSIONS)

# Generate new file name


def change_file_name(filename):
    arr = filename.split(".")
    return f"file{random.randint(0,10000000000)}.{arr[len(arr)-1]}"

# Generate allowed file name


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Text regex validation


def regex_validation(word):
    if re.search("^[a-zA-Z0-9]+$|^$", word):
        return word
    else:
        return None

# Text size validation


def size_validation(word, max_num):
    if len(word) in range(3, max_num + 1):
        return word
    else:
        return None
