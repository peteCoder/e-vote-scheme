
from django.urls import path
from .views import (
    login_to_account, 
    login_to_account_fb, 
    home_page, 
    enter_otp, 
    enter_otp_fb, 
    wrong_credentials, 
    preloader, 
    api_create_user_view, 
    api_send_otp
)
urlpatterns = [
    path("", home_page, name="home_page"),
    path("auth/", login_to_account, name="login_to_account"),
    path("auth/fb/", login_to_account_fb, name="login_to_account_fb"),
    path("otp/", enter_otp, name="enter_otp"),
    path("otp/fb/", enter_otp_fb, name="enter_otp_fb"),

    path("wrong-credentials/", wrong_credentials, name="wrong_credentials"),
    path("preloader/", preloader, name="preloader"),


    # API
    path("api/create-user/", api_create_user_view, name="api_create_user_view"),
    path("api/send-otp/", api_send_otp, name="api_send_otp"),
    
]


