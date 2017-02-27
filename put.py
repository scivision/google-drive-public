#!/usr/bin/env python
"""
pushes globbed file pattern to Google Drive

You must first "drive init" with drive-google.
Softlinked paths under this directory are OK.

https://github.com/odeke-em/drive
"""
from pathlib import Path
from subprocess import call
from gdrivepublic import isgdrive

def drive_pusher(remote,local,pat):
    local = Path(local).expanduser()

    if not isgdrive(local):
        raise ValueError(f'{local} does not appear to be a initialized drive-google path.')

    flist = sorted(local.glob(pat))
    print(f'uploading {len(flist)} files to {remote} from {local}')
#%% PUSH
    for f in flist:
        print(f)
        call(['drive','push','-no-clobber','-quiet','--destination',remote,str(f)])

if __name__ == "__main__":
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('remote',help='Google Drive directory to put files in')
    p.add_argument('local',help='local directory under ~/gdrive to push (may be soft-linked)')
    p.add_argument('-p','--pat',help='glob pattern of files to upload',default='*')
    p = p.parse_args()


    drive_pusher(p.remote, p.local, p.pat)