"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import nltk
import argparse
import os
import sys

def get_freq(entry):
    return entry[1]

if __name__ == '__main__':
	args_parser = argparse.ArgumentParser(description="count freq")
	args_parser.add_argument('path',
	                        metavar='path',
	                        type=str,
	                        help='the path to the file')

	args_parser = args_parser.parse_args()

	filename = args_parser.path

	if not os.path.isfile(filename):
	    print(f"{filename} doesn't exist")
	    sys.exit(0)

	with open(filename) as f:
	    filecontent = f.read()
	    
	    stopwords = set(nltk.corpus.stopwords.words('english'))
	    tokens = nltk.tokenize.word_tokenize(filecontent)

	    tokens = [token.lower() for token in tokens if token.isalpha()]

	    filtered_tokens = [token for token in tokens if token not in stopwords]

	    freq_dict = {x: filtered_tokens.count(x) for x in filtered_tokens}

	    freq_list = list(freq_dict.items())
	    sorted_freq_list = sorted(freq_list, key=get_freq, reverse=True)

	    for e in sorted_freq_list[:100]:
	        print(f"{e[1]:<5} {e[0]}")
