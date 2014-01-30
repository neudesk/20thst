#!/usr/bin/env python

from setuptools import setup

setup(
    name='Church of Christ',
    version='1.0.1',
    description='Official Church Website',
    author='Jonathan Senence Canaveral',
    author_email='neumerance@live.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django==1.5.5',
                      'PIL',
                      'django-imagekit',
                      'south',
                      'django-merchant',
                      'django-paypal',
                      'django-ckeditor',
                      'django-suit',
                      'django-gravatar2',
                      'django-endless-pagination',
                      'requests',
                      'django-cleanup',
                      'django-widget-tweaks',
                      'django-uuidfield',
                      'Paste',
                      'django-tables2'],
)
