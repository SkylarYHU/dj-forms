from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("contact/", views.contact_view, name="contact"),
    path("upload/", views.upload_view, name="upload"),
    path("success/", views.upload_success_view, name='success')
]
