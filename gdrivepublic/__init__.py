from sys import stderr
import pathvalidate
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from urllib.request import urlopen
import re
import requests
# this URL enables downloading files by actual filename, not some hash
BASE = 'https://googledrive.com/host'
#%% public
def gdriveurl(durl,odir,clobber,pat,verbose):
    pat = re.compile(pat)

    html = urlopen(durl)
    assert html.code == 200,'URL not accessible'

    txt = BeautifulSoup(html,'lxml').text

    flist = re.findall(pat,txt)

    if not flist:
        raise FileNotFoundError('no matching files found in this folder')

    print(f'found {len(flist)} files under {durl}')

    for f in flist:
        download_public(f,durl,odir,clobber,verbose)

def download_public(f,durl,odir,clobber,verbose):
    fid = urlsplit(durl).path.split('/')[-1]

    odir = Path(odir).expanduser()
    ofn = odir / f
    if ofn.is_file() and not clobber: #NOTE doesn't verify checksum or size--need PyDrive and login for that...
        print('SKIPPING',ofn)
        return
#%% download
    url = '/'.join((BASE,fid,f))  # NOT urljoin()

    if verbose:
        print(url)

    r = requests.get(url, stream=True)
    if r.status_code != 200:
        print(f'ERROR code {r.status_code}:  {url}  ',file=stderr)
        return

    with ofn.open('wb') as o:
        for c in r.iter_content(chunk_size=1024):
            if c:
                o.write(c)

#%%
def isgdrive(path):
    path = Path(path).expanduser()

    for p in path.parents:
        print(p)
        gd = p/'.gd'
        if gd.is_dir() and (gd/'credentials.json').is_file():
            return True

    return False  # fallthru in case none of the parents were True

def safename(fn):
    """
    returns cross-platform safe name WITHOUT directory
    """
    if isinstance(fn,Path):
        fn = fn.name
    return pathvalidate.sanitize_filename(fn,'-')

def browser():
    from platform import system
    from selenium import webdriver

    syst = system().lower()
    try:
        drv = webdriver.Firefox()
        print('using Firefox')
    except Exception:
        if 'windows' in syst:
            chrome='c:\chromedriver\chromedriver.exe'
        elif 'linux' in syst:
            chrome='/usr/lib/chromium-browser/chromedriver'
        else:
            chrome=None

        drv = webdriver.Chrome(chrome)
        print('using Chrome')

    return drv
