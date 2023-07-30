from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class CustomJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        try:
            access = super().get_validated_token(raw_token)
            if self.get_user(access).accepted:
                return access
        except:
            pass
        raise InvalidToken()
    
    def get_user(self, validated_token):
        try:
            return self.user
        except:
            self.user = super().get_user(validated_token)
            return self.user
        
