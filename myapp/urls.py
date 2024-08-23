from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.home, name='Home'),
    path('posts/', views.list_posts, name='post_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('create/', views.create_mymodel, name='create_mymodel'),

    path('create_object/', views.create_object, name='create_object'),
    path('getting_object/<int:object_id>/', views.get_object, name='get_object'),
    path('updating_object/<int:object_id>/update/', views.update_object, name='update_object'),
    path('deleting_object/<int:object_id>/delete/', views.delete_object, name='delete_object'),
]

router = DefaultRouter()
router.register(r'mymodel', views.MyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
