"""
MIDDLEWARE support for Pyasys.
Recommended only for advanced users. Do not change this file unless you are really sure you know what you are doing.

This file is the host of the official source code of Pyasys's core components.
"""

# git clone https://github.com/heewoonkim2020/pyasys.git
# Cloning: Supported --Git -u origin
# Make sure to add origin connect!

import random

"""
TRACK_ID: Random track id. Do not share this with others.
TOKEN: Random authenticator token.
"""
TRACK_ID = random.randint(1, 10000)
TOKEN = random.randint(1, 10000)

# MiddleToken (supporting)
MIDDLETOKEN_SUPPORT = True  # For now, MiddleToken is supported for Pyasys development.
MIDDLETOKEN_CONFIG = [
    # Configuration dict for MiddleToken.
    ['pyasys.components.middleware', 'pyasys/components/MIDDLEWARE.py']
]
MIDDLETOKEN_AUTH = [
    # Authentication information for MiddleToken.
    ['token', random.randint(1, 10000)]
]

# Git tracking

GITCONFIG = [
    '.gitignore'
]
# Making sure Pyasys ignores .gitignore
"""
.pyasysignore means: Ignore .gitignore files.
"""
IGNORE_DIR = [
    '.gitignore',
    '*.pyc'
]
pyasysIGNORE = IGNORE_DIR.copy()

if pyasysIGNORE:
    pyasysIGNORE_COUNT = pyasysIGNORE.count()
    pyasysIGNORE_COUNT += 1
elif pyasysIGNORE == "hardwareError":
    raise SystemError("Error encountered with Pyasys & hardware state of Pyasys.")
    # Error in HardwareState: Not with error --pyasys
else:
    raise Exception(".pyasysignore failed.")