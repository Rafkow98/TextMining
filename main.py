from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from tokenizer import text_tokenizer
from visualisation import visualisation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn import metrics, svm

if __name__ == '__main__':

    # Importing data

    data = pd.read_csv('./data/tweets_airline.csv', encoding='unicode_escape', usecols=[1, 10])
    x = data['text']
    y = data['airline_sentiment']
    data_neutral = data[y == 'neutral']
    data_positive = data[y == 'positive']
    data_negative = data[y == 'negative']

    # Wordcloud



    # Visualisation

    plt.pie(y.value_counts(), labels=np.flipud(y.unique()), autopct='%.1f%%')
    plt.legend(loc='upper right')
    plt.title("Percentage of sentiment in the dataset")
    plt.show()
    table = PrettyTable()
    table.title = 'Sentiment in the dataset'
    table.field_names = ['Sentiment', 'Count', 'Percentage']
    table.add_row(['Positive', data_positive['airline_sentiment'].count(),
                   data_positive['airline_sentiment'].count() / y.count() * 100])
    table.add_row(['Neutral', data_neutral['airline_sentiment'].count(),
                   data_neutral['airline_sentiment'].count() / y.count() * 100])
    table.add_row(['Negative', data_negative['airline_sentiment'].count(),
                   data_negative['airline_sentiment'].count() / y.count() * 100])
    table.add_row(['Sum', y.count(),
                   y.count() / y.count() * 100])
    print(table)

    vect_positive = vect_neutral = vect_negative = CountVectorizer(tokenizer=text_tokenizer)

    X_transform_positive = vect_positive.fit_transform(data[y == 'positive']['text'])
    tokens_positive = pd.DataFrame(X_transform_positive.sum(axis=0), columns=vect_positive.get_feature_names_out())
    visualisation(tokens_positive.T.sort_values(by=0, ascending=False).head(10),
                  "Most frequent tokens in positive messages")

    X_transform_neutral = vect_neutral.fit_transform(data[y == 'neutral']['text'])
    tokens_neutral = pd.DataFrame(X_transform_neutral.sum(axis=0), columns=vect_neutral.get_feature_names_out())
    visualisation(tokens_neutral.T.sort_values(by=0, ascending=False).head(10),
                  "Most frequent tokens in neutral messages")

    X_transform_negative = vect_negative.fit_transform(data[y == 'negative']['text'])
    tokens_non_spam = pd.DataFrame(X_transform_negative.sum(axis=0), columns=vect_negative.get_feature_names_out())
    visualisation(tokens_non_spam.T.sort_values(by=0, ascending=False).head(10),
                  "Most frequent tokens in negative messages")

    vect_tfidf = TfidfVectorizer(tokenizer=text_tokenizer)

    X_transform_tfidf = vect_tfidf.fit_transform(data['text'])
    tokens_tfidf = pd.DataFrame(X_transform_tfidf.sum(axis=0), columns=vect_tfidf.get_feature_names_out())
    visualisation(tokens_tfidf.T.sort_values(by=0, ascending=False).head(10), "Most important tokens (TF-IDF)")

    # Classification

    vectorizer = CountVectorizer(tokenizer=text_tokenizer)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    x_train = vectorizer.fit_transform(x_train)
    x_test = vectorizer.transform(x_test)

    clf = DecisionTreeClassifier()
    clf = clf.fit(x_train, y_train)
    decision_tree = clf.predict(x_test)
    print("Accuracy (decision tree): ", metrics.accuracy_score(y_test, decision_tree))
    print("Classification (decision tree): \n", metrics.classification_report(y_test, decision_tree))

    clf = RandomForestClassifier()
    clf = clf.fit(x_train, y_train)
    random_forest = clf.predict(x_test)
    print("Accuracy (random forest): ", metrics.accuracy_score(y_test, random_forest))
    print("Classification (random forest): \n", metrics.classification_report(y_test, random_forest))

    clf = svm.SVC(kernel='linear')
    clf = clf.fit(x_train, y_train)
    svm = clf.predict(x_test)
    print("Accuracy (SVM): ", metrics.accuracy_score(y_test, svm))
    print("Classification (SVM): \n", metrics.classification_report(y_test, svm))

    clf = AdaBoostClassifier()
    clf = clf.fit(x_train, y_train)
    adaboost = clf.predict(x_test)
    print("Accuracy (AdaBoost): ", metrics.accuracy_score(y_test, adaboost))
    print("Classification (AdaBoost): \n", metrics.classification_report(y_test, adaboost))

    clf = BaggingClassifier()
    clf = clf.fit(x_train, y_train)
    bagging = clf.predict(x_test)
    print("Accuracy (Bagging): ", metrics.accuracy_score(y_test, bagging))
    print("Classification (Bagging): \n", metrics.classification_report(y_test, bagging))

    print(f'Accuracies: \nDecision tree classifier: {metrics.accuracy_score(y_test, decision_tree)} \n'
          f'Random forest classifier: {metrics.accuracy_score(y_test, random_forest)} \n'
          f'SVM classifier: {metrics.accuracy_score(y_test, svm)} \n'
          f'AdaBoost classifier: {metrics.accuracy_score(y_test, adaboost)} \n'
          f'Bagging classifier: {metrics.accuracy_score(y_test, bagging)}')

    print(f'Spośród klasyfikatorów branych pod uwagę najlepiej poradził sobie klasyfikator SVM, '
          f'którego skuteczność wynosi około 76%. Wyniki dla tego klasyfikatora zostały ponownie pokazane poniżej\n'
          f'{metrics.classification_report(y_test, bagging)}\n'
          f'W zbiorze testowym znalazły się 4392 rekordy\n'
          f'Wartość precision dla negatywnych opinii wynosi około 0,84 (precision - stosunek dobrze sklasyfikowanych '
          f'wiadomości pozytywnych do wszystkich wiadomości sklasyfikowanych jako pozytywne)\n'
          f'Wartość recall dla negatywnych opinii wynosi około 0,86 (recall - stosunek dobrze sklasyfikowanych'
          f'wiadomości pozytywnych do wszystkich prawdziwie pozytywnych wiadomości)\n'
          f'Wartość F1 dla negatywnych opinii wynosi około 0,85 (F1 - 2 * (precision * recall) / (precision + recall))\n'
          f'Wartości mogą się trochę różnić z powodu minimalnej losowości klasyfikatorów')
