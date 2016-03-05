from courses.models import Course
from rest_framework import serializers
from django.contrib.auth.models import User

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = "owner.username")

    class Meta:
        model = Course
        fields = ('url', 'owner', 'title', 'description')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many = True, view_name = "course-detail", read_only = True)

    class Meta:
        model  = User
        fields = ('id', 'username','courses')
