import requests
import sys
import hashlib

url = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'
r = requests.get(url)
content = r.text
ht = {}
for x in content.split('\n'):
    ht[hashlib.blake2b(x.encode('utf-8')).digest()] = x

def get_words(word):

    out = []
    for i in range(len(word)-1):
        try:
            temp = word[:i] + word[i+1:]
            #https://stackoverflow.com/a/3559592
            temphash = hashlib.blake2b(temp).digest()
            out.append(ht[temphash])
        except KeyError:
            continue
    return out

def wfunnel(word):

    temphash = hashlib.blake2b(word).digest()
    try:
        print(str(ht[temphash]) + ' is a valid starting word')
    except KeyError:
        print(sys.argv[1] +  ' is not a valid starting word')
        return

    quit = False
    test = get_words(word)
    print(len(test))

def main():
    print('script : ' + sys.argv[0] )
    if sys.argv[1]:
        wfunnel(sys.argv[1].encode('utf-8'))

if __name__ == '__main__':
    main()
