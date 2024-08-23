from django.urls import path
from . import views 
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='Login'),
    path('', include(router.urls)),
    path('profile/', views.profile_view, name='profile'),
]
