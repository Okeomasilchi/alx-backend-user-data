#!/usr/bin/env python3

"""
Model for Logging
"""


import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """
    Filter sensitive data from a message.

    Args:
      fields (list): A list of strings representing
        the sensitive fields to be filtered.
      redaction (str): The string to replace the sensitive
        data with.
      message (str): The message containing the sensitive data.
      separator (str): The separator used to separate the
        fields in the message.

    Returns:
      str: The filtered message with the sensitive data replaced.
    """
    regex = r"(" + "|".join(fields) + r")=.*?(?=" + \
        re.escape(separator) + r"|$)"
    return re.sub(regex, r"\1=" + redaction, message)
