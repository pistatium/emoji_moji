# coding: utf-8

import os
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name='emoji_moji',
    version='0.0.1',
    url='https://github.com/pistatium/emoji_moji',
    author='pistatium',
    description='Convert chars to emoji image.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        str(i.req) for i in parse_requirements(
            os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=False) if not i.link
    ],
    entry_points={
        'console_scripts': [
            'emoji_moji=emoji_moji.cmd:main'
        ]
    },
)

