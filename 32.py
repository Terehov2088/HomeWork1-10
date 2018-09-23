"""
Задача 32. Написать функцию, которая выведет N самых часто встречающихся слов в файле.
Для этого функция будет получать путь к файлу с текстом и кол-во самых часто встречающихся слов для печати.
Поскольку в большинстве языков самыми часто используемыми словами являются союзы, предлоги, артикли и т.д.,
то для литературных произведений данная функция вернет в top N слов именно их, что мало интересно с точки зрения анализа текста.
Поэтому, кроме пути к файлу с текстом, необходимо в функцию передать путь к файлу с т.н. стоп-словами, которые необходимо исключить из подсчета.
Пример файла с английским стоп-словами: https://github.com/dbradul/python_classes/blob/master/basics/stop2.txt

def count_words(file_path_text, file_path_stop_words, top_n):
# returns list of top_n most frequent words in file_path_text file, except words from file_path_stop_words file
"""

import string
import pprint

def the_most_common_words1(file_path_text, file_path_stop_words):

    def complation_word(word_list, stop_list, top_words):
        for word in word_list:
            if word not in stop_list:
                if word not in top_words:
                    top_words[word] = 0
        return top_words

    file_text = open(file_path_text)
    file_stop = open(file_path_stop_words)


    line = file_text.readline()
    stop = file_stop.read()
    stop_list = [str(word.strip("!@#$%.^&*():;[]{]\", |'?-_=+\/,.")) for word in stop.split()]
    top_words = {}
    while line:
        line = line.lower()
        word_list = [str(word.strip("!@#$%^&,*():\"| [.]{];'-?_=+\/,.")) for word in line.split()]
        top_words = complation_word(word_list, stop_list, top_words)
        line = file_text.readline()

    file_text.close()
    file_stop.close()

    file_text = open(file_path_text)
    file_stop = open(file_path_stop_words)

    line = file_text.readline()

    while line:
        line = line.lower()
        word_list = [str(word.strip("!@#$%^&,*():\"|[.] {];'-?_=+\/,.")) for word in line.split()]
        for word in word_list:
            if word in top_words:
                top_words[word] += 1
        line = file_text.readline()

    file_text.close()
    file_stop.close()

    return top_words


top_words = the_most_common_words1('galaxy.txt', 'stop_word.txt')

def get_value_by_key(key):
    return top_words[key]


for key in sorted(top_words.keys(), key=get_value_by_key, reverse=True):
    print('%s -> %s' % (key, top_words[key]))



















    # while line:
    #     for char in line:
    #         new_char = processor(char)
    #         file_out.write(new_char)
    #     line = file_in.readline()
    #
    # file_in.close()
    # file_out.close()















# def encoder(char):
#     return shift_char(char, +5)
#
#
# def decoder(char):
#     return shift_char(char, -5)
#
# def process_file(filepath_in, filepath_out, processor):
#     file_in = open(filepath_in)
#     file_out = open(filepath_out, 'w+')
#
#     line = file_in.readline()
#     while line:
#         for char in line:
#             new_char = processor(char)
#             file_out.write(new_char)
#         line = file_in.readline()
#
#     file_in.close()
#     file_out.close()
#
#
# process_file('galaxy.txt', 'galaxy_enc.txt', encoder)
# process_file('galaxy_enc.txt', 'galaxy_dec.txt', decoder)
#
#
# # comprehension
# symbols = {chr(code): 0 for code in range(ord("a"), ord("z")+1)}
# pprint.pprint(symbols)
#
# es2en_dict = {v: k for k, v in en2es_dict.items()}
# pprint.pprint(es2en_dict)
# print(es2en_dict['mundo'])
#
# text = open('lesson_dict.py').read()
# text = text.lower()
# print(text)
#
# for char in text:
#     if char in symbols:
#         symbols[char] += 1
#
# pprint.pprint(symbols)