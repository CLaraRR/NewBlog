from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
    path('comment/post/<int:post_id>/', views.post_comment, name = 'post_comment'),

]