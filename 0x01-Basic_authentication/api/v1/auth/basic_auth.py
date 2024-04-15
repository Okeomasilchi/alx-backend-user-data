#!/usr/bin/env python3
"""
class to manage the API authentication.
"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class to manage the API authentication"""

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        if authorization_header is None or not isinstance(
            authorization_header,
            str
        ):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]
