# Core imports.
from django.urls import path

# Third-party imports.
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView,
)

from .views import (
    VerificationCodeModelCreateAPIView,
    LoginOrRegisterUserByJWTCreateAPIView,
)


app_name = 'accounts'


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(
        'verification-code/',
        VerificationCodeModelCreateAPIView.as_view(),
        name='verification-code-create',
    ),
    path(
        'login/',
        LoginOrRegisterUserByJWTCreateAPIView.as_view(),
        name='user-login',
    ),
]
