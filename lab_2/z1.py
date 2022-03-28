import re


def text_clean(text):
    emot = ' '.join([str(i) for i in
                          re.findall(r'(?::\)|;\)|;\(|:>|:<|;<|:-\)|;-\))', text)])
    t1 = re.sub(r'(?::\)|;\)|;\(|:>|:<|;<|:-\)|;-\))', '', text)
    t2 = t1.lower()
    t3 = re.sub(r'\d', '', t2)
    t4 = re.sub(r'<.*?>', '', t3)
    t5 = re.sub(' +', ' ', t4)
    t6 = re.sub(r'[,;.]', '', t5)
    res = t6 + emot
    return res
