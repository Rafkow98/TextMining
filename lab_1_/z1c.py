import re


def text_print(text):
    print(text)


def inter_del(text):
    print(re.sub(r'\W | \s', '', text))