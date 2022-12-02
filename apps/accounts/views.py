# Third-party imports.
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers.internals import (
    InternalVerificationCodeModelSerializer,
    InternalLoginOrRegisterUserByJWTModelSerializer,
)


class VerificationCodeModelCreateAPIView(CreateAPIView):
    permission_classes = (~IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = InternalVerificationCodeModelSerializer


class LoginOrRegisterUserByJWTCreateAPIView(CreateAPIView):
    permission_classes = (~IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = InternalLoginOrRegisterUserByJWTModelSerializer
