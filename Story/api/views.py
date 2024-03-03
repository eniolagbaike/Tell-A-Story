from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserProfileOwnerOrReadOnly
from .models import Profile
from .serializers import UserProfileSerializer, RegisterSerializer
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView


# Create your views here.
class UserList(generics.ListAPIView):
    """
    Retrieve a list of all users.
    """
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer

   
# Class based view to Get User Details using Token Authentication
class UserProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve the user profile of the currently logged-in user.
    """
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Retrieve the profile associated with the currently authenticated user
        return self.request.user.profile

class UserProfileEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Update the user profile of the currently logged-in user.
    """
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsUserProfileOwnerOrReadOnly]

    def get_object(self):
        # Retrieve the profile associated with the currently authenticated user
        return self.request.user.profile
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Profile has been deleted."}, status=status.HTTP_204_NO_CONTENT)
    

   


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    @swagger_auto_schema(operation_description="Register a new user")
    
    def post(self, request, *args, **kwargs):
      
        return super().post(request, *args, **kwargs)

# Logout view
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Logout and invalidate the user's token")
    def post(self, request):
        """
        Logout and invalidate the user's token.
        """
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out."})

