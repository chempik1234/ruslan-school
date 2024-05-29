from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, re_path, reverse_lazy
from .views import category_page   #  SignInView, SignUpView, logout_view, profile_view, email_reset_view

app_name = 'category_pages'

urlpatterns = [
    path("category/<int:category_pk>", category_page, name="category")
]

handler404 = 'category_pages.views.handler404'
