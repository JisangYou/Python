from django.shortcuts import render

# Create your views here.
# from rest_framework import viewsets
#
# from jayBlog.models import Person
# from jayBlog.serializers import PersonSerializer
#
#
# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from jayBlog.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer