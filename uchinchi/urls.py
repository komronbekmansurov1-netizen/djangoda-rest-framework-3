from django.urls import path
from .views import Salom1ModelView, Salom2ModelView, Salom3ModelView, Salom4ModelView, Salom5ModelView

urlpatterns = [
    path('salom1/', Salom1ModelView.as_view({'get': 'list'})),
    path('salom1/<int:pk>', Salom1ModelView.as_view({'get': 'list'})),
    path('salom2/', Salom2ModelView.as_view({'get': 'list'})),
    path('salom2/<int:pk>', Salom2ModelView.as_view({'get': 'list'})),
    path('salom3/', Salom3ModelView.as_view({'get': 'list'})),
    path('salom3/<int:pk>', Salom3ModelView.as_view({'get': 'list'})),
    path('salom4/', Salom4ModelView.as_view({'get': 'list'})),
    path('salom4/<int:pk>', Salom4ModelView.as_view({'get': 'list'})),
    path('salom5/', Salom5ModelView.as_view({'get': 'list'})),
    path('salom5/<int:pk>', Salom5ModelView.as_view({'get': 'list'})),
]