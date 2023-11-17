from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReCaptchaV2.check, name="Index")
]
