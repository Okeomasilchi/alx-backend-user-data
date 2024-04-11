#!/usr/bin/env python3

"""
Model for Logging
"""


import re
import logging
from typing import List
import os
import mysql.connector


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*",
                         f"{field}={redaction}", message)
    return message


PII_FIELDS = ('name', 'email', 'phone', 'password', 'ssn')


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = None):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields if fields else []

    def format(self, record: List[str]) -> str:
        """Formats the log record and applies data filtering"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Returns a logger object configured to log user
    data with redacted PII fields.

    Returns:
      logger (logging.Logger): The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

    formatter = RedactingFormatter(PII_FIELDS)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Retrieve database credentials from
    environment variables
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")

    try:  # try Connecting to the database
        connection = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=db_name
        )
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)
