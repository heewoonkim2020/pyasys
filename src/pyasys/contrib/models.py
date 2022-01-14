"""
Model handling for Pyasys.
"""

class Model:
    def __init__(self, **kwargs):
        """
        A database model for authentication handling.
        
        :param kwargs: Attributes and context for the model.
        """
        self.attrs = kwargs
        if "type" in self.attrs:
            self.modelType = kwargs["type"]
    
    def get_attr(self, keyname):
        """
        Gets an attribute from the kwargs context.
        
        :param keyname: The key name to be looked up.
        :return: Returns the keyname value on context, returns None if key does not exist.
        """
        if keyname in self.attrs:
            return self.attrs[keyname]
        else:
            return None

class Prep_User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password.encode('utf-8')
    
    def get_login_info(self, password_attempt: str):
        if password_attempt == self.password.decode('utf-8'):
            return True
        else:
            # return: Can be used as a bool definition
            return False