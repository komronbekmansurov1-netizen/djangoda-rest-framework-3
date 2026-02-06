from .serializer import Salom1Serializer, Salom2Serializer, Salom3Serializer, Salom4Serializer, Salom5Serializer
from .models import Salom1, Salom2, Salom3, Salom4, Salom5
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class Salom1ModelView(ModelViewSet):
    serializer_class = Salom1Serializer
    queryset = Salom1.objects.all()


class Salom2ModelView(ModelViewSet):
    serializer_class = Salom2Serializer
    queryset = Salom2.objects.all()


class Salom3ModelView(ModelViewSet):
    serializer_class = Salom3Serializer
    queryset = Salom3.objects.all()


class Salom4ModelView(ModelViewSet):
    serializer_class = Salom4Serializer
    queryset = Salom4.objects.all()


class Salom5ModelView(ModelViewSet):
    serializer_class = Salom5Serializer
    queryset = Salom5.objects.all()