#!/usr/bin/env python3

"""
Model for Logging
"""


import re


def check(fie: list, red: str, mess: str, sep: str) -> str:
    """Handles obfuscation of log message"""
    pattern = r"(" + "|".join(fie) + r")=.*?(?=" + \
        re.escape(sep) + r"|$)"
    return re.sub(pattern, r"\1=" + red, mess)


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    return check(fields, redaction, message, separator)
