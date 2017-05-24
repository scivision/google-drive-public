#!/usr/bin/env python
"""
allows downloading from Google Drive folders publicly shared without login
modify PAT to suit the file types you're downloading
Michael Hirsch, Ph.D.
"""
from gdrivepublic import gdriveurl
#PAT = 'd\d{7}.dt\d.h5'  # for AMISR HDF5 files.


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('durl',help='folder URL (immediately containing files copied from web browser')
    p.add_argument('-o','--odir',help='output directory to download into',default='.')
    p.add_argument('-p','--pat',help='regex for files to download',default='d\d{7}.dt\d.h5')
    p.add_argument('-c','--clobber',help='overwrite existing files',action='store_true')
    p.add_argument('-v','--verbose',action='store_true')
    p = p.parse_args()

    gdriveurl(p.durl, p.odir, p.clobber, p.pat, p.verbose)
