#!/usr/bin/env python
"""
pulls globbed file pattern to Google Drive

You must first "drive init" with drive-google.
Softlinked paths under this directory are OK.

https://github.com/odeke-em/drive
"""
from pathlib import Path
from subprocess import call
from gdrivepublic import isgdrive

def drive_puller(remote,local,flist):
    # FIXME consider implementing 'drive list' techniques
    """
    remote: Google Drive directory (string)
    flist: list of filenames (within remote)
    local: gdrive folder on your PC
    """
    local = Path(local).expanduser()
    remote = str(remote)

    if not isgdrive(local):
        raise ValueError(f'{local} does not appear to be a initialized drive-google path.')

    for f in flist:
        call['drive','pull','-no-clobber','-no-prompt', '/'.join((remote,f))]

if __name__ == "__main__":
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('remote',help='Google Drive directory to put files in')
    p.add_argument('local',help='local gdrive root')
    p.add_argument('-f','--flist',help='file names to download (future: use drive list or public.py)',nargs='+')
    p = p.parse_args()


    drive_puller(p.remote, p.local, p.flist)