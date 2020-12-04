from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers


class TagViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """Manage tags in the database"""
    # Requires token authentication is used
    authentication_classes = (TokenAuthentication,)
    # And the user is authenticated to use the API
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    # Filters queryset by user
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by("-name")

    # Hooks into the create process
    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)
