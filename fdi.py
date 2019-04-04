import os
import re
import collections


def book_finder():
    #print("Insert the folder's name")
    #where = input()
    where = 'SONGS'
    file_address = '/Users/elizavetaersova/PycharmProjects/FDI/' + where
    # print(where)
    files = os.listdir(file_address)
    books = []
    for i in files:
        if i.endswith('.txt'):
            books.append(i)

    # print(files)
    print(books)
    return books, where


def word_lists():
    #print('Insert word list name')
    #name = input()
    names = ['CAE2.txt', 'FCE.txt', 'IELTS.txt']
    word_list = []
    for name in names:
        file_address = '/Users/elizavetaersova/PycharmProjects/FDI/' + name
        with open(file_address, mode='r', encoding='latin-1') as file:
            text = file.read()
            text = re.sub('\s\n', '\n', text)
            words = text.split('\n')
            for word in words:
                word_list.append(word)

    print(word_list)
    #print(word_list)
    return word_list


def text_search(books, where, word_list):
    rating = []
    for book in books:
        total_books = len(books)
        useful_words = collections.Counter()
        book_address = '/Users/elizavetaersova/PycharmProjects/FDI/' + where + '/' + book

        with open(book_address, mode='r', encoding='latin-1') as file:
            text = file.read()
            text = clean_text(text)
            words = text.split()
            total_words = len(words)
            checked = 0
            #words = lemmaizer(text)
            plurals = []
            for word in words:
                if word in word_list:
                    useful_words[word] += 1
                if word[:-2] != ''and word[:-2] in word_list:
                    useful_words[word] += 1
                    plurals.append(word)
                if word[:-1] != ''and word[:-1] in word_list:
                    useful_words[word] += 1
                    plurals.append(word)
                if word[:-3] + 'y' in word_list:
                    useful_words[word] += 1
                    plurals.append(word)
                checked += 1
            progress = (checked / total_words)
            print(progress)
        plurals = set(plurals)
        #print('plurals: ', len(plurals),  set(plurals))
        info = book + ' ' + 'useful words' + ' ' + str(len(useful_words)) + '; ' + 'total_words: ' + str(total_words) + ' ratio - ' + str((len(useful_words)/total_words)*100)
        rating.append(info)

        #print(book, len(useful_words), useful_words)
    for book in rating:
        print(book)


def clean_text(text):
    text = text.lower()
    text = re.sub('[,.?!:;"]', '', text)
    return text




def main():
    books, where = book_finder()
    word_list = word_lists()
    text_search(books, where, word_list)

if __name__ == '__main__':
    main()
