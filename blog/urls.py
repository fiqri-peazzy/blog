from ipaddress import v4_int_to_packed
from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/',views.single_post, name='single_post'),
    path('blog/',views.post_list, name='post_list'),
    path('blog/<slug:tag_slug>/', views.post_list, name='tag_post'),
    path('add_comment/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/remove/', views.remove_comment, name='remove_comment'),
    path('new_post/', views.new_post, name='new_post'),
    path('draft/', views.draft, name='draft'),
    path('draft/detail/<int:pk>/', views.draft_detail, name='draft_detail'),
    path('post_publish/<int:post_id>/', views.post_publish, name='post_publish'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    
]