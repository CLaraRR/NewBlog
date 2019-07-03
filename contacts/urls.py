from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact/post', views.contact_post, name = 'contact_post'),

]