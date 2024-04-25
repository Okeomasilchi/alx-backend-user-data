#!/usr/bin/env python3
"""
Auth model for all authentication mechanisms
"""


import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
        Hashes the given password using bcrypt.

        Args:
          password (str): The password to be hashed.

        Returns:
          bytes: The hashed password.
        """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(
        password.encode('utf-8'),
        salt
    )


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initializes an instance of the Auth class.

        The __init__ method is called when a new object of the
        Auth class is created. It initializes the instance
        variable _db with an instance of the DB class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> None:
        """
        Registers a user in the database.

        Args:
          email (str): The email address of the user.
          password (str): The password of the user.

        Returns:
          None
        """
        if self._db._session.query(User).filter_by(email=email).first():
            raise ValueError(f"User '{email}' already exists")

        return self._db.add_user(email, _hash_password(password))
