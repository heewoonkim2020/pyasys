"""
MIDDLEWARE support for Pyasys.
Recommended only for advanced users. Do not change this file unless you are really sure you know what you are doing.
"""

import random

"""
TRACK_ID: Random track id. Do not share this with others.
TOKEN: Random authenticator token.
"""
TRACK_ID = random.randint(1, 10000)
TOKEN = random.randint(1, 10000)