"""
Settings configuration for Pyasys.
"""

DEBUG = True
LICENSE = "MIT"

INSTALLED_APPS = [
    'pyasys',
    'pyasys.contrib.auth',
    'pyasys.contrib.models',
]

INSTALLED_COMPONENTS = [
    'pyasys',
    'pyasys.components.MIDDLEWARE'
]