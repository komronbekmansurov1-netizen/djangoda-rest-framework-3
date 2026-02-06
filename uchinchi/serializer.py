from .models import Salom1, Salom2, Salom3, Salom4, Salom5
from rest_framework.serializers import ModelSerializer


class Salom1Serializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom1


class Salom2Serializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom2


class Salom3Serializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom3


class Salom4Serializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom4


class Salom5Serializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Salom5