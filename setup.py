#!python

from setuptools import setup, find_packages

setup(name='Ringing In Ross',
      version='0.1',
      description='Wedding site',
      author='Joshua Ross',
      author_email='joshualross@gmail.com',
      url='https://www.ringinginross.com/',
      packages=find_packages(),
      # package_dir={'application': 'application'},

      # data_files=[('config', ['application/config/base.yaml'])],
)
