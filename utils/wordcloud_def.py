from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud(df, title):
    uniques = list(set(df))
    bow = {unique: df.count(unique) for unique in uniques}
    wc = WordCloud(width=1000, height=1000, background_color='white',
                   colormap='Blues')
    wc_freq = wc.generate_from_frequencies(bow)
    plt.axis("off")
    plt.imshow(wc_freq, interpolation='bilinear')
    plt.title(title)
    plt.show()
