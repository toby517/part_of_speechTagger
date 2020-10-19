from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


path = '_articles-sports\_articlesSports\sportscapr14.txt'
file = open(path, encoding="utf8")
text = file.read()
print(text)