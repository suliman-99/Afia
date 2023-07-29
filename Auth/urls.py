from django.urls import path
from Auth.views import *


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('send-verification-code/', SendVerificationCodeView.as_view(), name='send_verification-code'),
    path('verify/', VerifyView.as_view(), name='verify'),
    path('refresh/', RefreshView.as_view(), name='refresh'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('change-email/', ChangeEmailView.as_view(), name='change-email'),
]

