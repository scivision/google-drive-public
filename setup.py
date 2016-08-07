#!/usr/bin/env python
from setuptools import setup
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception:
    pass

setup(name='google-drive-public',
	  description='downloading from Google Drive public directories',
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/google-drive-public',
	  install_requires=[
                     #'selenium',
                     'pathlib2'],
      packages=['gdrivepublic'],
	  )


