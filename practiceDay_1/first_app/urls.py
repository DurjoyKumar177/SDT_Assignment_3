from django.urls import path
from . import views

urlpatterns = [
    path('html_form/',views.html_form, name='html_form'),
    path('django_form/',views.django_form, name='django_form'),
    ]