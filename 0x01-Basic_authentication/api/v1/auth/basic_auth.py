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
        """
        Extract the Base64 encoded part of a
        Basic Authorization header.

        Args:
          authorization_header (str): The authorization
              header from which the Base64 encoded string
              is to be extracted.

        Returns:
          str: The Base64 encoded string if the header is
              valid and contains the
              expected prefix. Otherwise, None.

        Note:
            This function only validates the prefix and
            the presence of the header. It does not validate
            whether the Base64 string is properly encoded or
            decode the Base64 string.
        """
        if authorization_header is None or not isinstance(
            authorization_header,
            str
        ):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]
