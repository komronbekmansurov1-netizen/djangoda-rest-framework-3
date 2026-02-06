from django.urls import path
from .views import Salom1ListView, Salom2ListView, Salom3ListView, Salom4ListView, Salom5ListView

urlpatterns = [
    path('salom1/', Salom1ListView.as_view()),
    path('salom1/<int:pk>', Salom1ListView.as_view()),
    path('salom2/', Salom2ListView.as_view()),
    path('salom2/<int:pk>', Salom2ListView.as_view()),
    path('salom3/', Salom3ListView.as_view()),
    path('salom3/<int:pk>', Salom3ListView.as_view()),
    path('salom4/', Salom4ListView.as_view()),
    path('salom4/<int:pk>', Salom4ListView.as_view()),
    path('salom5/', Salom5ListView.as_view()),
    path('salom5/<int:pk>', Salom5ListView.as_view()),
]