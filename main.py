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

grammar_all = nltk.CFG.fromstring("""
   S -> NP VP | VP NP
   VP -> V | V N | V N PP | V PP | V PP N | PP V | V V | V S
   PP -> P N   
   NP -> N | N P N
   V -> "наступило" | "поспела" | "собирают" | "будет" | "варить" | "будут" | "пить"
   N -> "лето" | "даша" | "смородина" | "алиса" | "ее" | "ведерко" | "мама" | "варенье" | "дети" | "чай" | "саду" | "вареньем" 
   P -> "у" | "в" | "и" | "из" | "с" 
   """)
i = 0
while i < len(sentences):
    structure = nltk.word_tokenize(sentences[i], language='russian')
    parser = nltk.RecursiveDescentParser(grammar_all)
    parses = list(parser.parse(structure))
    for tree in parser.parse(structure):
        tree.pretty_print()
        # print(tree, "\n")
    i = i + 1
