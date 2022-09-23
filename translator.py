import re
import numpy as np
import googletrans
import srt
from googletrans import Translator
import sys

translator = Translator()
NAME = sys.argv[1]
file = open(f"{NAME}.srt","r")
subs = list(srt.parse(file))
merge = True

for i in range(len(subs)):
    line = subs[i].content
    translated_line = translator.translate(str(line), dest='zh-CN').text.encode('utf-8').decode('utf-8').replace('\n','')
    if merge:
        subs[i].content = line + '\n' + translated_line
    else:
        subs[i].content = translated_line


if merge:
    output_file = f"{NAME}_merge.srt"
else:
    output_file = f"{NAME}_cn.srt"
fo = open(output_file,"wb")
fo.write(srt.compose(subs).encode('utf8'))
fo.close()
