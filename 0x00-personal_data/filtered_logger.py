#!/usr/bin/env python3

"""
Model for Logging
"""


import re


def filter_datum(fields, redaction, message, separator) -> str:
    """returns the log message obfuscated"""
    return re.sub(
      r"(" + "|".join(fields) + r")=.*?(?=" + re.escape(separator) + r"|$)",
                  r"\1=" + redaction, message)
