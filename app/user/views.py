from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    # This is all we need, as CreateAPIView will handle the rest.
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    # Renders in the django admin
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManagerUserView(generics.RetrieveUpdateAPIView):
    """Manager the authenticated user"""
    serializer_class = UserSerializer
    # We're using token authentication
    authentication_classes = (authentication.TokenAuthentication,)
    # The permission you need, is to be signed in
    permission_classes = (permissions.IsAuthenticated,)

    # Overwrite `get_object` to get the user that is authenticated
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
