from django.urls import path
from .views import Salom1View, Salom2View, Salom3View, Salom4View, Salom5View

urlpatterns = [
    path('salom1/', Salom1View.as_view()),
    path('salom1/<int:pk>', Salom1View.as_view()),
    path('salom2/', Salom2View.as_view()),
    path('salom2/<int:pk>', Salom2View.as_view()),
    path('salom3/', Salom3View.as_view()),
    path('salom3/<int:pk>', Salom3View.as_view()),
    path('salom4/', Salom4View.as_view()),
    path('salom4/<int:pk>', Salom4View.as_view()),
    path('salom5/', Salom5View.as_view()),
    path('salom5/<int:pk>', Salom5View.as_view()),
]