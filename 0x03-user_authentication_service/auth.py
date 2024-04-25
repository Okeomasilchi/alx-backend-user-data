#!/usr/bin/env python3
"""
Auth model for all authentication mechanisms
"""


import bcrypt


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
