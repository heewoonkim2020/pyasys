"""
The authentication model for Pyasys.
"""

from .models import Model

class User(Model):
    def cred_check(self, password):
        # TODO Check password in encrypted connection
        pass