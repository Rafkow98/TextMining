import re


def text_print(text):
    print(text)


def numbers_del(text):
    print(re.sub(r'\d', '', text))

#z1a
print(re.sub(r'\d', '', 'Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku'))
#z1b
print(re.sub(r'<[^>]*>', '', r'<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>'))
#z1c
print(re.sub(r'\W | \s', '', 'Lorem ipsum dolor sit amet, consectetur; adipiscing elit.'
                              'Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. '
                              'Inblandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus'
                              'eu risus.'))
#z2
print(re.findall(r'(#\S+)\s', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                         'Sed #texting eget mattis sem. Mauris #frasista egestas erat #tweetext quam, '
                         'ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, '
                         'tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus.'))
#z3
print(re.findall(r'(?::\)|;\)|;\(|:>|:<|;<|:-\)|;-\))', 'Lorem ipsum dolor sit amet, consectetur; adipiscing elit.'
                              'Sed eget mattis sem. Mauris ;-) egestas erat quam, ut faucibus eros congue et. '
                              'Inblandit, mi eu porta :); lobortis, tortor nisl facilisis leo :<, at tristique augue risus'
                              'eu risus.'))

#zmodularyzować
