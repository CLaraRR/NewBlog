from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('blog/', views.BlogsView.as_view(), name = 'blog'),
    path('post/<int:pk>/', views.PostPageView.as_view(), name = 'post_page'),
    path('archive/<int:year>/<int:month>/', views.ArchiveView.as_view(), name = 'archive'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name = 'category'),
    path('tag/<int:pk>/', views.TagView.as_view(), name = 'tag'),
    path('about/', views.about_page, name = 'about'),
    path('contact/', views.contact_page, name = 'contact'),
    # path('search/', views.search, name = 'search'),


]
