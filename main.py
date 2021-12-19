import os
from googletrans import Translator
import googletrans as tran
from pprint import pprint
from reverso_api.context import ReversoContextAPI
import sys

trans = Translator()
if len(sys.argv) < 3:
    print(f"usage: python {sys.argv[0]} wordlist sourcelang targetlang")
    sys.exit(-1)
    # quit()
wordlist = sys.argv[1]
if not os.path.exists(wordlist):
    print(f"Error wordlist path not valid!")
    print(f"usage: python {sys.argv[0]} wordlist sourcelang targetlang")
    sys.exit(-1)
targetlang = sys.argv[3]
sourcelang = sys.argv[2]
langs = list(tran.LANGUAGES.keys())

if targetlang not in langs or sourcelang not in langs:
    print('valid languages: ', langs)
    exit(-1)


def googletranslate(word):
    return trans.translate(word, src=sourcelang, dest=targetlang).text


def reversotranslate(word):
    api = ReversoContextAPI(word, "", sourcelang, targetlang)
    try:
        return next(api.get_translations()).translation
    except:
        return googletranslate(word)


if os.path.exists("out.txt"):
    os.remove("out.txt")

output = open('out.txt', 'w+')


try:
    with open(wordlist, 'r+') as wordfile:
        lines = wordfile.readlines()
        for i, line in enumerate(lines):
            l = line.strip()
            # print("[+] ", l, " , ", end=' ')
            # if reversotranslate(l) != "":
            # res = "insert into ru_ar(ru, ar) values('%s','%s')\n" % (
            #    l, reversotranslate(l))
            output.write(reversotranslate(l))
            # output.write(f"{l},{reversotranslate(l)}")
            print(f'[{i}] ', reversotranslate(l))
except KeyboardInterrupt:
    print("Good Bye...")
