from stopwords import stopwords_del
from text_clean import cleanText
from text_stem import stemSentence


def text_tokenizer(text: str) -> list:
    cleaned = cleanText(text)
    stopw = stopwords_del(cleaned)
    stemmed = stemSentence(stopw)
    word_list = []
    for word in stemmed:
        if len(word) > 3:
            word_list.append(word)
    return word_list
