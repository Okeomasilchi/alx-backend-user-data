#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
from db import DB
email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()
db = DB()
auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))

print(db.find_user_by(email=email).__dict__)