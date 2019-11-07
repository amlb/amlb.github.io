#!/usr/bin/python3

import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

URL_CODES = "https://www.legifrance.gouv.fr/initRechCodeArticle.do"
URL_DOWNLOAD = "https://www.legifrance.gouv.fr/download_code_pdf.do?cidTexte=%s&dlType=pdf"

soup = BeautifulSoup(urlopen(URL_CODES).read(), "lxml")
codes = [option['value'] for option in soup.find('select').find_all('option')]

os.makedirs('codes_pdfs', exist_ok=True)
for code in codes:
    if 'LEGITEXT' in code:
        urlretrieve(URL_DOWNLOAD % code, 'codes_pdfs/' + code + '.pdf')
        