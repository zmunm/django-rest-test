from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework import mixins

from zmunm.models import Language


def test(request):
    return HttpResponse("Hello:")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class Api(GenericAPIView, mixins.ListModelMixin):
    queryset = Language.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
