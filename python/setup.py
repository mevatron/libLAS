from setuptools import setup, Extension
from sys import version_info

# Require ctypes egg only for Python < 2.5
install_requires = ['setuptools']
if version_info[:2] < (2,5):
    install_requires.append('ctypes')

import os

version = file('../nmake.opt').readline().strip()
version = version.split('=')[1]
print version

if os.name == 'nt':
    # Windows NT library
    lib_name = 'liblas%s.dll' % version
    data_files=[('DLLs', ['DLLs/%s'% lib_name]),]
else:
    data_files = None

print data_files
setup(name          = 'libLAS',
      version       = version,
      description   = 'LAS 1.0/1.1 LiDAR data format reader',
      license       = 'BSD',
      keywords      = 'DEM elevation LIDAR',
      author        = 'Howard Butler',
      author_email  = 'hobu.inc@gmail.com',
      maintainer    = 'Howard Butler',
      maintainer_email  = 'hobu.inc@gmail.com',
      url   = 'http://liblas.org',
      data_files = data_files,
#      long_description = readme_text,
      packages      = ['liblas'],
      install_requires = install_requires,
      test_suite = 'tests.test_suite',
      classifiers   = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
        ],
)

