import z1a
import z1b
import z1c
import z2
import z3

if __name__ == '__main__':
    text_num = 'Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku'
    z1a.text_print(text_num)
    z1a.numbers_del(text_num)
    text_head = r'<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>'
    z1b.text_print(text_head)
    z1b.headers_del(text_head)
    text_inter = 'Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ' \
                 'Mauris egestas erat quam, ut faucibus eros congue et. Inblandit, mi eu porta; ' \
                 'lobortis, tortor nisl facilisis leo, at tristique augue risus eu risus.'
    z1c.text_print(text_inter)
    z1c.inter_del(text_inter)
    text_hash = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. ' \
                'Mauris #frasista egestas erat #tweetext quam, ut faucibus eros #frasier congue et. ' \
                'In blandit, mi eu porta lobortis, tortor nisl facilisis leo, at tristique ' \
                '#frasistas augue risus eu risus.'
    z2.text_print(text_hash)
    z2.hash_find(text_hash)
    text_emot = 'Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ' \
                'Mauris ;-) egestas erat quam, ut faucibus eros congue et. Inblandit, mi eu porta :); ' \
                'lobortis, tortor nisl facilisis leo :<, at tristique augue risus eu risus.'
    z3.text_print(text_emot)
    z3.emot_find(text_emot)
