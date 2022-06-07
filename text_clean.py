import re


def cleanText(text: str):
    emot = ' '.join([str(i) for i in
                    re.findall(r'(?::\)|;\)|;\(|:>|:<|;<|:-\)|;-\))', text)])
    emot_del = re.sub(r'(?::\)|;\)|;\(|:>|:<|;<|:-\)|;-\))', '', text)
    low = emot_del.lower()
    numbers = re.sub(r'\d', '', low)
    html = re.sub(r'<.*?>', '', numbers)
    multiple_blank = re.sub(' +', ' ', html)
    http = re.sub('http', ' ', multiple_blank)
    punct_marks = re.sub(r'[,;.\']', '', http)
    result = punct_marks + emot
    return result
