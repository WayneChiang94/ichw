import sys
from urllib.request import urlopen


def read_text():
    url = 'http://www.gutenberg.org/cache/epub/19033/pg19033.txt'
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    return docstr

def dictofwordcount(inputlistofwords):
    counts = {}
    for word in inputlistofwords:
        counts[word] = counts.get(word, 0) + 1
    return counts

def wcount241126(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    # your code goes here
    pass


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('url: URL of the txt file to analyze ')
        print('topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
        
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print(sys.argv[1])
        text = read_text()
        stroftext = text.decode("utf-8")
        listoflines = stroftext.splitlines()
        listofwords = []
        for eachline in listoflines:
            listofwords += eachline.split(' ')
        listofitems = list(dictofwordcount(listofwords).items())
        listofitems.sort(key=lambda x:x[1],reverse = True)
        if len(sys.argv) == 2:
            print(listofitems[0:10])
        else:
            print(listofitems[0:int(sys.argv[2])])
        sys.exit(0)


    # your code goes here
    # should anayze whether paras are right or not
