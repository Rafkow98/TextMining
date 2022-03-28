import pandas as pd
from text_clean import cleanText
from text_stem import stemSentence


def readFile(path: str, col: str) -> list:
    data = pd.read_csv(path, usecols=[col], encoding='UTF-8')
    data = data.values.astype(str)
    cleared_data = []
    for row in data:
        cleared_data.append(str(stemSentence(cleanText(str(row)))))
    return cleared_data
