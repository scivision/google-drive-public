#!/usr/bin/env python
req = ['nose','requests','lxml',]
pipreq = ['pathvalidate',
                     #'selenium',
],

import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)
# %%

from setuptools import setup

setup(name='google-drive-public',
      packages=['gdrivepublic'],
	  description='downloading from Google Drive public directories',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/google-drive-public',
	  install_requires=req+pipreq,
	  )


