from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from utils.tokenizer import text_tokenizer
from utils.visualisation import visualisation
from utils.wordcloud_def import wordcloud
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn import metrics, svm

# E-Mail classification NLP: https://www.kaggle.com/datasets/datatattle/email-classification-nlp

if __name__ == '__main__':

    # Importing data

    data_source1 = pd.read_csv('./data/SMS_test.csv', encoding='unicode_escape')
    data_source2 = pd.read_csv('./data/SMS_train.csv', encoding='unicode_escape')
    data = pd.concat([data_source1, data_source2])
    x = data['Message_body']
    y = data['Label']
    data_spam = data[y == 'Spam']
    data_non_spam = data[y == 'Non-Spam']

    # Wordclouds

    all_messages_str = " ".join(message for message in x.astype(str))
    wordcloud(text_tokenizer(all_messages_str), "Tokens in all messages")
    spam_messages_str = " ".join(message for message in x.astype(str))
    wordcloud(text_tokenizer(spam_messages_str), "Tokens in spam messages")
    non_spam_messages_str = " ".join(message for message in x.astype(str))
    wordcloud(text_tokenizer(non_spam_messages_str), "Tokens in non-spam messages")

    # Visualisation

    plt.pie(y.value_counts(), labels=np.flipud(y.unique()), autopct='%.1f%%')
    plt.legend(loc='upper right')
    plt.title("Percentage of spam and non-spam messages in the dataset")
    plt.show()
    table = PrettyTable()
    table.title = 'Spam messages dataset basic statistics'
    table.field_names = ['Type', 'Count', 'Percentage']
    table.add_row(['Spam', data_spam['Label'].count(),
                   data_spam['Label'].count() / y.count() * 100])
    table.add_row(['Non-Spam', data_non_spam['Label'].count(),
                   data_non_spam['Label'].count() / y.count() * 100])
    table.add_row(['Sum', y.count(),
                   y.count() / y.count() * 100])
    print(table)

    vect_spam = vect_non_spam = CountVectorizer(tokenizer=text_tokenizer)

    X_transform_spam = vect_spam.fit_transform(data[y == 'Spam']['Message_body'])
    tokens_spam = pd.DataFrame(X_transform_spam.sum(axis=0), columns=vect_spam.get_feature_names_out())
    visualisation(tokens_spam.T.sort_values(by=0, ascending=False).head(10), "Most frequent tokens in spam messages")

    X_transform_non_spam = vect_non_spam.fit_transform(data[y == 'Non-Spam']['Message_body'])
    tokens_non_spam = pd.DataFrame(X_transform_non_spam.sum(axis=0), columns=vect_non_spam.get_feature_names_out())
    visualisation(tokens_non_spam.T.sort_values(by=0, ascending=False).head(10),
                  "Most frequent tokens in non-spam messages")

    vect_tfidf = TfidfVectorizer(tokenizer=text_tokenizer)

    X_transform_tfidf = vect_tfidf.fit_transform(data['Message_body'])
    tokens_tfidf = pd.DataFrame(X_transform_tfidf.sum(axis=0), columns=vect_tfidf.get_feature_names_out())
    visualisation(tokens_tfidf.T.sort_values(by=0, ascending=False).head(10), "Most important tokens (TF-IDF)")

    # Classification

    vectorizer = CountVectorizer(tokenizer=text_tokenizer)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
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
