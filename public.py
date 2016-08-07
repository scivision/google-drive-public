#!/usr/bin/env python
from pydrive.files import FileNotDownloadableError
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path
# pip install -e git+https://github.com/googledrive/PyDrive.git#egg=PyDrive

try:
    drive = GoogleDrive(gauth)
except NameError:
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

def download_gdrive(datestr, odir, inst):
    odir = Path(odir).expanduser()
    i0 = drilldown('PokerFlat')
#%% get into date directory
    i1 = drive.ListFile({'q': "'{}' in parents and title='{}' and trashed=false".format(i0,datestr)}).GetList()[0]['id']
#%% isr
    i2 = drive.ListFile({'q': "'{}' in parents and title='{}' and trashed=false".format(i1, inst)}).GetList()[0]['id']
#%% list files here
    flist = drive.ListFile({'q': "'{}' in parents and trashed=false".format(i2)}).GetList()

    for f in flist:
        ofn = odir / f['title']
        if ofn.is_file():
            continue
        try:
            f.GetContentFile(str(ofn))
            print(ofn)
        except FileNotDownloadableError:
            print('ERROR: {}'.format(ofn))

def drilldown(child,parentid=None):
    if parentid:
        return drive.ListFile({'q': "'{}' in parents and title='{}' and trashed=false".format(parentid,child)}).GetList()[0]['id']
    else:
        return drive.ListFile({'q': "title='{}' and trashed=false".format(child)}).GetList()[0]['id']

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('date',help='yyyy-mm-dd  e.g. 2013-05-01')
p.add_argument('-o','--odir',help='output directory',default='.')
p.add_argument('--inst',help='instrument',default='isr')
p = p.parse_args()

download_gdrive(p.date,p.odir,p.inst)