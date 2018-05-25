#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
        name='netjsonconfig_airos',
        version='0.0.0',
        description='airos compatible netjsonconfig backend',
        packages=find_packages(),
        entry_points={
            'netjsonconfig.backends': [
                'airos=netjsonconfig_airos.__init__:AirOs',
            ]
        }
    )
