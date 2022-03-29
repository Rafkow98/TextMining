from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from tokenizer import text_tokenizer
import pandas as pd


if __name__ == '__main__':
    data = pd.read_csv('./data/True.csv', usecols=['title', 'text'])
    vectorizer = CountVectorizer(tokenizer=text_tokenizer)
    x_transform = vectorizer.fit_transform(data['title'][:10])
    print(vectorizer.get_feature_names_out())
    print(x_transform.toarray())
    sample = data['title'].sample(10)
    x_transform_sample = vectorizer.fit_transform(sample)
    print(vectorizer.get_feature_names_out())
    print(x_transform_sample.toarray())
