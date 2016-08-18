#!/usr/bin/env python
"""
renames files in local or Google Drive directory to lowercase and makes "safe" cross-platform filenames
"""
from gdrivepublic import Path,safename

def rename_local(path,pat,verbose):
    path = Path(path).expanduser()

    flist = sorted(path.glob(pat))

    print('renaming {} files in {}'.format(len(flist),path))

    for old in flist:
        new = old.parent / safename(old).lower()

        try:
            if new.samefile(old):
                if verbose:
                    print('SKIPPING existing  {}'.format(new))
                continue
        except FileNotFoundError:
            pass #good, no conflict

        if p.verbose:
            print('{}  ==>  {}'.format(old,new))
        old.rename(new)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path',help='local path to rename to lowercase and cross-platform safe')
    p.add_argument('-p','--pat',help='glob pattern of files',default='*')
    p.add_argument('-v','--verbose',action='store_true')
    p = p.parse_args()

    rename_local(p.path, p.pat,p.verbose)