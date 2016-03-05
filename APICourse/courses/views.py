from django.shortcuts import render
from courses.models import Course
from django.contrib.auth.models import User
from courses.serializers import CourseSerializer, UserSerializer
from courses.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @detail_route(renderer_classes = [renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
