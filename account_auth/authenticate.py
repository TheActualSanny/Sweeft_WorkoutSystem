from .models import BlackListedTokens
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id            
        is_allowed_user = True
        token = str(request.auth)
        try:
            is_blackListed = BlackListedTokens.objects.get(user=user_id, token=token)
            if is_blackListed:
                is_allowed_user = False
        except BlackListedTokens.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user