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

REQUIRED_APPS = [
    'pyasys',
    'pyasys.contrib',
    'pyasys.contrib.auth',
    'pyasys.contrib.models',
]

REQUIRED_COMPONENTS = [
    'pyasys',
    'pyasys.components.MIDDLEWARE',
]

for required_app in REQUIRED_APPS:
    if not required_app in INSTALLED_APPS:
        INSTALLED_APPS.append(required_app)
        
for required_component in REQUIRED_COMPONENTS:
    if not required_component in INSTALLED_COMPONENTS:
        INSTALLED_COMPONENTS.append(required_component)