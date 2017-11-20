#!/usr/bin/env python
req = ['nose','requests','lxml','beautifulsoup4','pathvalidate']

# %%
from setuptools import setup,find_packages

setup(name='google-drive-public',
      packages=find_packages(),
      version='0.2.0',
	  description='downloading from Google Drive public directories',
	  author='Michael Hirsch, Ph.D.',
	  url='https://github.com/scivision/google-drive-public',
	  install_requires=req,
	  python_requires='>=3.6',
	  extras_require={'web':['selenium']},
	  )


