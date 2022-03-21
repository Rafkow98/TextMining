import re


def text_print(text):
    print(text)


def headers_del(text):
    print(re.sub(r'<[^>]*>', '', text))
