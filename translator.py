import re
import numpy as np
import googletrans
import srt
from googletrans import Translator
import sys

translator = Translator()
NAME = sys.argv[1]
file = open(r"{}.srt".format(NAME,"r"))
subs = list(srt.parse(file))
for i in range(len(subs)):
    line = subs[i].content
    current_translate = translator.translate(str(line), dest='cn').text.encode('utf-8').decode('utf-8')
    subs[i].content = current_translate
fo = open(r"{0}.srt".format(NAME),"wb")
fo.write(srt.compose(subs).encode('utf8'))
fo.close()
