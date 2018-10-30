from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import serializers, status
from rest_framework import mixins
from rest_framework.response import Response
from django.core.cache import cache

from zmunm.models import Language, Project


def test(request):
    return HttpResponse("Hello:")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class Api(GenericAPIView, mixins.ListModelMixin):
    queryset = Language.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectApi(GenericAPIView, mixins.ListModelMixin):
    queryset = cache.get_or_set('posts', Project.objects.all())
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            serializer = ProjectSerializer(
                self.queryset.get(pk=kwargs.get('id', 'Default Value if not there')),
                data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(request.data, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            return Response(
                self.queryset.get(pk=kwargs.get('id', 'Default Value if not there'))
                    .delete(),
                status=status.HTTP_202_ACCEPTED)
        except ObjectDoesNotExist:
            return Response(request.data, status=status.HTTP_404_NOT_FOUND)
