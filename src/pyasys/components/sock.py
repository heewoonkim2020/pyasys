from turtle import st
from . import MIDDLEWARE

import sys
import os
import typing
import typing_extensions

class ContextDownloadMethod:
    def __init__(self, method: str):
        """
        Generate an object with the specified method keystring.
        """
        if method:
            # User specified value
            if method.lower() == "const_inet_downloader":
                return ContextDownloadMethod.generate_context(method.upper())
        else:
            # Return an error
            return None
        
    def generate_context(contextmethod: str):
        """
        This function will raise an error when run on a single context machine.
        """
        
        if type(contextmethod) == str:
            contextmethod[0] = ""
            
            if contextmethod == "onst_inet_downloader".upper():
                return typing
        else:
            return None

class AsyncContextGenerator:
    async_generator: int
    async_context_wrapper: int
    async_context_generator: int
    
    def generate():
        """
        Generate an AsyncContext.
        """
        AsyncContextGenerator.async_context_generator = "emptyContext"
        # Method overloaded functions
        from typing import overload as overload_generator
        from typing_extensions import overload as overload_gen
        
        if AsyncContextGenerator.async_context_generator:
            if AsyncContextGenerator.context_wrapper():
                pass
    
    def context_wrapper(context_uri, context_download: bool, context_download_method: ContextDownloadMethod):
        """
        Basic context wrapper for overloaded functions.
        """
        overloaded_context = (context_uri, context_download, context_download_method)
        return overloaded_context
    
    def get():
        return AsyncContextGenerator.async_generator
    
AsyncContextGenerator.generate()

# Import MIDDLEWARE.contrib to import Pyasys

# from .MIDDLEWARE import MIDDLETOKEN_AUTH
from .MIDDLEWARE import MIDDLETOKEN_CONFIG
for configuration in MIDDLETOKEN_CONFIG:
    if configuration[0] == "pyasys.token.auth":
        if configuration[1] == "pyasys.token.auth/User":
            user_model = typing.Any
        elif configuration[1] == "pyasys.token.auth/User/models.py":
            user_model = typing_extensions.AsyncContextManager
        
def async_context(func):
    """
    Basic wrapper class for async context generations.
    """
    def wrapper():
        context: str
        context_uri: int = 0
        if type(context_uri) == int:
            func()
        else:
            raise TypeError("Invalid type for pyasys.clone")

    return wrapper