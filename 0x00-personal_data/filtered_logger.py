#!/usr/bin/env python3

"""
Model for Logging
"""


import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*",
                         f"{field}={redaction}", message)
    return message


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
