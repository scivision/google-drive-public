#!/usr/bin/env python
"""
renames files in local or Google Drive directory to lowercase and makes "safe" cross-platform filenames
"""
from pathlib import Path
from gdrivepublic import safename

def rename_local(path,pat,verbose):
    path = Path(path).expanduser()

    flist = sorted(path.glob(pat))

    print(f'renaming {len(flist)} files in {path}')

    for old in flist:
        new = old.parent / safename(old).lower()

        try:
            if new.samefile(old):
                if verbose:
                    print(f'SKIPPING existing  {new}')
                continue
        except FileNotFoundError:
            pass #good, no conflict

        if p.verbose:
            print(f'{old}  ==>  {new}')
        old.rename(new)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('path',help='local path to rename to lowercase and cross-platform safe')
    p.add_argument('-p','--pat',help='glob pattern of files',default='*')
    p.add_argument('-v','--verbose',action='store_true')
    p = p.parse_args()

    rename_local(p.path, p.pat,p.verbose)
