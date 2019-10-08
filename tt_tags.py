import treetaggerwrapper, pprint, os, re

tagger = treetaggerwrapper.TreeTagger(TAGLANG='en', TAGDIR='tt/')
def get_text(filename):
    forbidden = ['clean/.DS_Store']
    if filename not in forbidden:

        with open(filename, encoding='utf-8') as f:
            try:
                text = f.read()
            except UnicodeDecodeError:
                print(filename)
        pattern = '(\w)\.(\w)'
        text = re.sub(pattern, r'\1\. \2', text)  # убираю то, что ломает прогу
        pattern = '(\w):'
        text = re.sub(pattern, r'\1 :', text)
    else:
        text = 0
    return text


def tagging(text):
    #print(text)
    text = re.sub('\s\s', ' ', text)
    lines = re.sub('\.\s', '.\n', text)
    lines = re.sub('\?\s', '?\n', lines)
    lines = re.sub('\!\s', '!\n', lines)
    sentences = lines.split('.txt\n')
    #print(sentences)
    text = ''
    for sentence in sentences:
        if sentence != '':
            l1 = sentence + '\n'
              # тупо таггерю
            tags = tagger.tag_text(sentence)

            sp = []
            for tag in tags:
                word, tag, lemma = tag.split(
                    '\t')  # привожу к формату треугольных скобочек, именно тут нерастагеренные штуки ломали прогу (не было \t)
                nl = '<' + word + ' ' + tag + '>'
                sp.append(nl)
            spstr = ''.join(sp)
            l2 = spstr + '@' +'\n'
            text += l1
            text += l2
        #print(text)
    return text



def output1(string, filename):
    folder = r'C:/Users/Prestigio/Desktop/Realec_tags/exam2014/'  # путь куда сохранять в формате стобиков
    filename = folder + filename[:-4] + '_tags.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(string)


def output2(string, filename):
    folder = 'folder3/'  # путь куда сохранять в формате треугольных скобочек
    filename = folder + filename
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(string)


def main():
    directory = 'folder/'  # путь откуда брать реалек, таггерю папки по очереди
    files = os.listdir(directory)

    b = 0
    for file in files:

        name = directory + file
        print(name)
        a = get_text(name)
        if a != 0:
            c = tagging(a)
            output2(c, file)
            b += 1
        else:
            print('ERROR')

        #d = '\n'.join(b)
        #output1(d, file)


main()
##a = get_text(r'') #для поиска ошибок
##b = tagging(a)
##pprint.pprint(b)
