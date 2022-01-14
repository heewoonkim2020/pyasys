"""
The authentication model for Pyasys.
"""

from . import models

class User(models.Model, models.Prep_User):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password.encode('utf-8')