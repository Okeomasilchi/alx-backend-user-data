#!/usr/bin/env python3

"""
Model for Encrypt Password
"""


import bcrypt


def hash_password(password: str) -> bytes:
  """
  Hashes the given password using bcrypt.

  Args:
    password (str): The password to be hashed.

  Returns:
    bytes: The hashed password.

  """
  salt = bcrypt.gensalt()  # Generate a random salt
  # Hash the password with the salt
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hashed_password
