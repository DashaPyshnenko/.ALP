import re
import nltk
import pymorphy2
from nltk.parse.dependencygraph import DependencyGraph
text = 'Наступило лето. В саду поспела смородина. Даша и Алиса собирают ее в ведерко. Мама будет варить варенье. Дети будут пить чай с вареньем.'
sentences = re.compile(r'[.|!|?|…]').split(text.lower())
print(sentences)

tokens = nltk.word_tokenize(text.lower(), language="russian")
tagged = nltk.pos_tag(tokens)
print(tagged)
morph = pymorphy2.MorphAnalyzer(lang='ru')
gramm = {}
for word in tokens:
    p = morph.parse(word)[0]
    if word not in gramm:
        gramm[word] = p.tag
print(gramm)