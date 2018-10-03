import requests
import sys
import hashlib

def wfunnel(word):
    url = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'
    r = requests.get(url)
    content = r.text
    ht = {}
    for x in content.split('\n'):
        ht[hashlib.blake2b(x.encode('utf-8')).digest()] = x

    temphash = hashlib.blake2b(word).digest()
    if ht[temphash]:
        print('yes is word')


def main():
    print('script : ' + sys.argv[0] )
    if sys.argv[1]:
        wfunnel(sys.argv[1].encode('utf-8'))

if __name__ == '__main__':
    main()
