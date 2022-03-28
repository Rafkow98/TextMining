import stopwords
import text_clean
import text_stem


def text_tokenizer(text: str) -> list:
    v1 = text_clean.text_clean(text)
    v2 = stopwords.stopwords_del(v1)
    v3 = text_stem.stemSentence(v2)
    word_list = []
    for word in v3:
        if len(word) > 3:
            word_list.append(word)
    return word_list
