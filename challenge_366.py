import requests
import sys
import hashlib
import timeit

url = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'
r = requests.get(url)
content = r.text
ht = {}
for x in content.split('\n'):
    ht[hashlib.blake2b(x.encode('utf-8')).digest()] = x

def get_words(word):

    out = []
    for i in range(len(word)):
        try:
            temp = word[:i] + word[i+1:]
            #https://stackoverflow.com/a/3559592
            temphash = hashlib.blake2b(temp.encode('utf-8')).digest()
            out.append(ht[temphash])
        except KeyError:
            continue
    return out

def wfunnel(words, length):

    if len(words[-1]) == 0:
        words = words[:-1]
        return words, length
    out = []
    for x in words[-1]:
        tmp = get_words(x)
        for y in tmp:
            out.append(y)
    words.append(out)
    length += 1
    return wfunnel(words, length)


def main():
    print('script : ' + sys.argv[0])

    if sys.argv[1] == 'bonus1':
        start = timeit.timeit()
        for x in content.split('\n'):
            word = [[x]]
            words,length = wfunnel(word, 0)
            if length == 10:
                for x in words:
                    print(x)
                print('length is: ' + str(length))
                end = timeit.timeit()
                time = end - start
                print('that took: ' + str(time) +  ' seconds' )
                return

    if sys.argv[1]:
        start = timeit.timeit()
        word = [[str(sys.argv[1])]]
        words,length = wfunnel(word, 0)
        for x in words:
            print(x)
        print('length is : ' + str(length))
        end = timeit.timeit()
        time = end - start
        print('that took: ' + str(time) + ' seconds' )

if __name__ == '__main__':
    main()
