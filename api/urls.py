from django.urls import path
from .views import LoginView, UploadKYCFormView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('uploadKycForm/', UploadKYCFormView.as_view()),
]
