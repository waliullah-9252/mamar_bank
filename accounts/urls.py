from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,UserBankAccountUpdateView, PassWordChangeForm


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', UserLogoutView.as_view(), name = 'logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name = 'profile'),
    path('profile/password-change/', PassWordChangeForm.as_view(), name = 'paswordchange'),
]