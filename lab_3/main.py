from file_read import readFile
from wordcloud import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    read_and_cleaned_csv = readFile("./data/True.csv", "title")
    text = read_and_cleaned_csv[0]
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./wordcloud.png')
    plt.show()
