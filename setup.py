#!/usr/bin/env python
from setuptools import setup

req = ['pathvalidate','lxml','requests','nose'
                     #'selenium',
],

setup(name='google-drive-public',
      packages=['gdrivepublic'],
	  description='downloading from Google Drive public directories',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scienceopen/google-drive-public',
	  install_requires=req,
	  )


