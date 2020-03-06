#!/bin/python3

import itertools
from pathlib import Path
from urllib.request import urlopen, Request

DOWNLOAD_FOLDER = Path("./tiles")
MIN_X, MAX_X = 127657, 128073
MIN_Y, MAX_Y = 90460, 90764

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'
base_url = 'https://wxs.ign.fr/an7nvfzojv5wa96dsga5nk8w/geoportail/wmts'
base_params = 'layer=ORTHOIMAGERY.ORTHOPHOTOS&style=normal&tilematrixset=PM&Service=WMTS'
base_params += '&Request=GetTile&Version=1.0.0&Format=image%2Fjpeg'

for (i, j) in itertools.product(range(MIN_X, MAX_X), range(MIN_Y, MAX_Y)):
    file_path = DOWNLOAD_FOLDER / f"{i}_{j}.jpg"
    if file_path.exists():
        continue
    params = f"TileMatrix=18&TileCol={i}&TileRow={j}"
    url = f"{base_url}?{base_params}&{params}"
    with urlopen(Request(url, headers={'User-Agent': user_agent})) as wf:
        with open(file_path, 'wb') as f:
	        f.write(wf.read())
