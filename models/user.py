#!/usr/bin/python3
"""module for the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """represents instances of the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
