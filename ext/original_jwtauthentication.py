import jwt
from typing import Any, Dict, Optional
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from django.conf import settings
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from datetime import datetime, timedelta, timezone


User = get_user_model()


class CustomJWT(BaseAuthentication):
    def authenticate(self, request) -> User:
        # token = self.extract_token(request=request)
        print(request)
        
    #     if token is None:
    #         return None
        
    #     try:
    #         payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
    #         self.verify_token(payload=payload)
            
    #         return User.objects.get(id=payload["user_id"]), None

    #     except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist):
    #         raise AuthenticationFailed("Error occured while validating token")
        
    def verify_token(self, payload: Dict[int, Any]) -> None:
        if "exp" not in payload:
            raise InvalidTokenError("Token has no expiry date")
        
        exp_timestamp = payload["exp"]
        current_timestamp = datetime.utcnow().timestamp()
        
        if current_timestamp > exp_timestamp:
            raise ExpiredSignatureError("Token has expired")
        
    # def extract_token(self, request) -> Any:
    #     auth_header = request.headers.get("Authorization")
        
    #     if auth_header and auth_header.startswith("Bearer"):
    #         return auth_header.split(" ")[1]
    #     return None
    
    @database_sync_to_async
    def authenticate_websocket(self, scope: Dict[str, Any], token: str) -> User | None:        
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
            self.verify_token(payload=payload)
            
            return User.objects.get(id=payload["user_id"])
            
        except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist):
            raise AuthenticationFailed("Error occured while validating token")