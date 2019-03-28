import os
import re
words = []
file = open('diccionario-hunspell.txt', "r", encoding="utf-8")
for line in file:
    words.append(line.rstrip())
len(words)
file = open('../diccionario-rae-completo.txt', "r", encoding="utf-8")
for line in file:
    words.append(line.rstrip())
cleanWords = []
for word in words:
    if '/' in word:
        cleanWords.append(word.split('/')[0])
    else:
        cleanWords.append(word)
len(words)
len(cleanWords)
cleanWords = sorted(cleanWords)
words = sorted(list(set(cleanWords)))
len(words)
with open('../diccionario-rae-completo.txt', mode='wt', encoding='utf-8') as file:
    file.write('\n'.join(words))


