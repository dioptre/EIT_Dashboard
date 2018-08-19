from setuptools import setup, find_packages

NAME = 'OpenEIT_Dashboard'
VERSION = '0.1.0'
AUTHOR = 'Jean Rintoul'
LICENSE = 'LICENSE'
INSTALL_REQUIRES = [
                    'imageio~=2.2.0',
                    'matplotlib~=2.1.1',
                    'numpy~=1.14.0',
                    'pyserial~=3.4',
                    'scikit-image~=0.13.1',
                    'scipy~=1.0.0',
                    'six~=1.11.0',
                    'Adafruit_BluefruitLE~=0.9.10'
                ]

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    license=LICENSE,
    packages = find_packages(),
    install_requires=INSTALL_REQUIRES,
)
