import nltk, re, pprint

with open('sample.txt') as ft:
    document = ft.read()
    
sentences = nltk.sent_tokenize(document)
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [nltk.pos_tag(sent) for sent in sentences]
