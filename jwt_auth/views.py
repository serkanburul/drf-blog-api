from rest_framework import generics
from .models import CustomUser
from .serializers import CustomRegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer
