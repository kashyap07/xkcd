#! /usr/bin/env python
# @Author: Suhas Kashyap
# @Last Modified time: 2016-06-21
# @https://github.com/kashyap07

import os

try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

setup(
  name = 'xkcd_downloader',
  version = '2.1',
  author = 'Suhas Kashyap',
  author_email = 'kashyapsuhas07@gmail.com.com', 
  description = "Download all of xkcd comics",
  long_description = "Use threadings to download all of xkcd comics really fast"
  url = 'https://github.com/kashyap07/xkcd', 
  install_requires = [
    "beautifulsoup4>=4.4.1",
    "requests>=2.8.1",
  ],

  classifiers = [
      'Development Status :: 3 - Alpha'
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
  ],
  keywords = ['xkcd', 'threads', 'download', 'comic'], 
)