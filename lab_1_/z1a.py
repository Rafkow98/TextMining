import re


def text_print(text):
    print(text)


def numbers_del(text):
    print(re.sub(r'\d', '', text))
