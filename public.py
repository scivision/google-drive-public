#!/usr/bin/env python
from pydrive.files import FileNotDownloadableError
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from gdrivepublic import Path
# pip install -e git+https://github.com/googledrive/PyDrive.git#egg=PyDrive

try:
    drive = GoogleDrive(gauth)
except NameError:
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

def download_gdrive(datestr, odir, inst, root):
    odir = Path(odir).expanduser()
    i0 = drilldown(root)
#%% get into date directory
    i1 = drilldown(datestr,i0)
#%% isr
    i2 = drilldown(inst,i1)
#%% list files here
    flist = drilldown(None,i2)

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
    if parentid and child:
        return drive.ListFile({'q': "'{}' in parents and title='{}' and trashed=false".format(parentid,child)}).GetList()[0]['id']
    elif child and not parentid:
        return drive.ListFile({'q': "title='{}' and trashed=false".format(child)}).GetList()[0]['id']
    elif parentid and not child:
        return drive.ListFile({'q': "'{}' in parents and trashed=false".format(parentid)}).GetList()

from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('date',help='yyyy-mm-dd  e.g. 2013-05-01')
p.add_argument('-o','--odir',help='output directory',default='.')
p.add_argument('-r','--root',help='topmost unique directory name',default='PokerFlat')
p.add_argument('--inst',help='instrument',default='isr')
p = p.parse_args()

download_gdrive(p.date,p.odir,p.inst,p.root)
