#!/usr/bin/env python3
"""
Main file
"""

import logging

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

print(type(get_logger()))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))