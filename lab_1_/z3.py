import re


def text_print(text):
    print(text)


def emot_find(text):
    print(re.findall(r'(?::\)|;\)|;\(|:>|:<|;<|:-\)|;-\))', text))