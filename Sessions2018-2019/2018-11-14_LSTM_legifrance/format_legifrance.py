#!/usr/bin/python3

import os
import re

DIR_PDF = "codes_pdfs"
CMD = 'pdftotext ' + DIR_PDF + '/%s tmp.txt'

if os.path.exists('legifrance.txt'):
    os.remove('legifrance.txt')

res_txt = ''
for pdf in os.listdir(DIR_PDF):
    print('Processing', pdf)
    os.system(CMD % pdf)
    with open('tmp.txt', 'r') as f:
        res_txt = f.read()
    os.remove('tmp.txt')

    # Removing Legifrance footer
    res_txt = re.sub(r'(?<=\n)\n*Code .* - Dernière modification le .* - Document généré le .*\sCopyright .* Legifrance\s*', '', res_txt)

    # Removing extra line returns inside text
    res_txt = re.sub(r'(?<=\n)([^\n]{80,})(\w+|L\.|,|°)\n(?=\w)', r'\1\2 ', res_txt)

    # Removing extra line returns inside titles
    """
    old_txt = ''
    while(old_txt != res_txt):
        old_txt = res_txt
        res_txt = re.sub(r'(?<=\n)([a-zA-Z\-]{5,20}) ([0-9]|V|I|X)+ : ([^\n]{40,})(\w+|L\.|,|°)\n(?=\w)', r'\1 \2 : \3\4', res_txt)
    """

    with open('legifrance.txt', 'a') as f:
        f.write(res_txt)
