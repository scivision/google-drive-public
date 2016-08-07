#!/usr/bin/env python
"""
allows downloading from Google Drive folders publicly shared without login
modify PAT to suit the file types you're downloading
Michael Hirsch
"""
from bs4 import BeautifulSoup
from six.moves.urllib.request import urlopen
import re
import requests
from gdrivepublic import Path

# this URL enables downloading files by actual filename, not some hash
BASE = 'https://googledrive.com/host'

PAT = r'd\d{7}.dt\d.h5'  # for AMISR HDF5 files

def gdriveurl(durl,odir,clobber,verbose):
    html = urlopen(durl)
    txt = BeautifulSoup(html,'lxml').text

    flist = re.findall(PAT,txt)

    if not flist:
        raise ValueError('no matching files found in this folder')

    for f in flist:
        download(f,durl,odir,clobber,verbose)

def download(f,durl,odir,clobber,verbose):
    fid = durl.split('/')[-1]

    odir = Path(odir).expanduser()
    ofn = odir / f
    if ofn.is_file() and not clobber: #NOTE doesn't verify checksum or size--need PyDrive and login for that...
        print('SKIPPING {}'.format(ofn))
        return

    print(ofn)
#%% download
    url = '/'.join((BASE,fid,f))

    if verbose:
        print(url)

    r = requests.get(url,stream=True)
    with ofn.open('wb') as o:
        for c in r.iter_content(chunk_size=1024):
            if c:
                o.write(c)

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('durl',help='folder URL (immediately containing files copied from web browser')
p.add_argument('-o','--odir',help='output directory to download into',default='.')
p.add_argument('-c','--clobber',help='overwrite existing files',action='store_true')
p.add_argument('-v','--verbose',action='store_true')
p = p.parse_args()

gdriveurl(p.durl,p.odir,p.clobber,p.verbose)
