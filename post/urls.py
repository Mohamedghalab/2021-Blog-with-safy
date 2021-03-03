from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new_post', views.new_post, name='new_post'),
    path('<int:post_id>/edit', views.post_edit, name="edit"),
    path('<int:post_id>/details', views.post_detail, name="detail"),
    path('<int:post_id>/delete', views.post_delete, name="delete"),
]
