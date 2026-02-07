from django.urls import path, include
from rest_framework.routers import DefaultRouter
from uchinchi.views import (Salom1ModelView, Salom2ModelView, Salom3ModelView, Salom4ModelView, Salom5ModelView)


router = DefaultRouter()
router.register(r'1', Salom1ModelView, basename='salom1')
router.register(r'2', Salom2ModelView, basename='salom2')
router.register(r'3', Salom3ModelView, basename='salom3')
router.register(r'4', Salom4ModelView, basename='salom4')
router.register(r'5', Salom5ModelView, basename='salom5')


urlpatterns = [
    path('', include(router.urls)),
]