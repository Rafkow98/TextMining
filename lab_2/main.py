import z1
import z2
import z3


if __name__ == '__main__':
    tekst = 'In our modern world, there are many factors that place the wellbeing of the planet in jeopardy. ' \
           'While some people have the opinion that environmental problems are just a natural occurrence, others' \
           'believe that human beings have a huge impact on the environment. Regardless of your viewpoint, ' \
           'take into consideration the following factors that place our environment as well as the planet ' \
           'Earth in danger. Global warming or climate change is a major contributing factor to environmental ' \
           'damage. Because of global warming, we have seen an increase in melting ice caps, a rise in sea ' \
           'levels, and the formation of new weather patterns. These weather patterns have caused stronger ' \
           'storms, droughts, and flooding in places that they formerly did not occur.'
    clean = z1.text_clean(tekst)
    print(clean)
    stopw = z2.stopwords_del(clean)
    print(stopw)
    res = z3.stemSentence(stopw)
    print(res)
