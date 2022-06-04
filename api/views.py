from django.shortcuts import render
from .serializers import *

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

from main.models import *

class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


class AccountViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountSerializers
    queryset = Account.objects.all()

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class CardsViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = CardsSerializers
    queryset = Cards.objects.all()

    def get_queryset(self):
        return Cards.objects.filter(creator=self.request.user)

