from djang.conf.urls import include, url
from courses.views import CourseViewSet, UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

course_list = CourseViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

course_detail = CourseViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

user_list = UserViewSet.as_view({
    'get' : 'list'
})

user_detail = UserViewSet.as_view({
    'get' : 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^courses/', course_list, name = "course_list" ),
    url(r'^courses/(?P<pk>[0-9]+)/$', course_detail, name = 'course_detail' ),
    url(r'^users/', user_list, name = 'user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name = 'user_detail'),
])
