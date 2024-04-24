#!/usr/bin/env python3

"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User
from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str,
                 hashed_password: str) -> User:
        """
        Adds a new user to the database.

        Args:
          email (str): The email of the user.
          hashed_password (str): The hashed password of the user.

        Returns:
          object: The newly created user object.

        Raises:
          ValueError: If either email or hashed_password is not
            provided.
          ValueError: If a user with the same email already
            exists in the database.
        """
        if email is None:
            return
        if hashed_password is None:
            return
        user = User(email=email, hashed_password=hashed_password)
        try:
            session = self._session
            session.add(user)
            session.commit()
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError("User with this email already exists")
        return user
