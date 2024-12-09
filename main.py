import time
from pathlib import Path
from urllib.parse import urlparse, urljoin

import requests

playlist_path = input('Path of m3u8 playlist (local path):') or "playlist.m3u8"
url = input('URL prefix of resources server (end with /):') or "www.google.com/"
download_dest = 'cache'

Path(download_dest).mkdir(parents=True, exist_ok=True)
playlist = open(playlist_path,'r')
for line in playlist.readlines():
    if line.startswith('#EXT') or line.strip() == '': continue
    else:
        download_path = urljoin(urlparse(url).geturl(), line.strip())
        with open(Path(download_dest).joinpath(line.strip()),'wb+') as f:
            time.sleep(0.3)
            print(f'downloading {download_path}...')
            f.write(requests.get(download_path).content)
