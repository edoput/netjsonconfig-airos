#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
        name='netjsonconfig_airos',
        author='Edoardo Putti (edoput)',
        author_email='edoardo.putti@gmail.com',
        url='https://github.com/edoput/netjsonconfig-airos',
        version='0.0.0',
        description='airos compatible netjsonconfig backend',
        packages=find_packages(exclude=['tests', ]),
        entry_points={
            'netjsonconfig.backends': [
                'airos=netjsonconfig_airos.__init__:AirOs',
            ]
        },
        keywords=[
            'airos',
            'netjsonconfig',
        ],
        license='GPL3',
        zip_safe=False,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: System :: Networking',
        ],
    )
