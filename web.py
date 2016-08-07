from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen
import re
import requests
from pathlib import Path
# sudo apt-get install chromium-chromedriver

BASE = 'https://googledrive.com/host/'

def gdriveurl(durl,odir):
    html = urlopen(durl)
    txt = BeautifulSoup(html,'lxml').text

    flist = re.findall(r'd\d{7}.dt\d.h5',txt)

    if not flist:
        raise ValueError('no matching files found in this folder')

    for f in flist:
        download(f,odir)

def download(f,odir):
    odir = Path(odir).expanduser()
    ofn = odir / f

    print(ofn)

    url = BASE + f
    r = requests.get(url,stream=True)
    with ofn.open('wb') as o:
        for c in r.iter_content(chunk_size=1024):
            if c:
                o.write(c)

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('durl',help='folder URL copied from web browser')
p.add_argument('-o','--odir',help='output directory to download into',default='.')
p = p.parse_args()

gdriveurl(p.durl,p.odir)