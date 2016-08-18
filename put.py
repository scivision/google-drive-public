#!/usr/bin/env python
"""
pushes globbed file pattern to Google Drive

You must first "drive init" with drive-google.
Softlinked paths under this directory are OK.

https://github.com/odeke-em/drive
"""
from subprocess import call
from gdrivepublic import Path, isgdrive

def drive_pusher(remote,local,pat):
    local = Path(local).expanduser()

    if not isgdrive(local):
        raise ValueError('{} does not appear to be a initialized drive-google path.'.format(local))

    flist = sorted(local.glob(pat))
    print('uploading {} files to {} from {}'.format(len(flist),remote,local))
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