#!/usr/bin/env python3
"""
class to manage the API authentication.
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication"""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if excluded_path == normalized_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization'] if request.headers['Authorization'] else None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
