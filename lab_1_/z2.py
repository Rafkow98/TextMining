import re


def text_print(text):
    print(text)


def hash_find(text):
    print(re.findall(r'(#\S+)\s', text))