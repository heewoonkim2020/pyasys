from . import MIDDLEWARE

# Import MIDDLEWARE.contrib to import Pyasys

# from .MIDDLEWARE import MIDDLETOKEN_AUTH
from .MIDDLEWARE import MIDDLETOKEN_CONFIG
for configuration in MIDDLETOKEN_CONFIG:
    if configuration[0] == "pyasys.token.auth"