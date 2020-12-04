from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe
from recipe import serializers


class BaseRecipeAttrViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """Base ViewSet for user owned recipe attributes"""
    # Requires token authentication is used
    authentication_classes = (TokenAuthentication,)
    # And the user is authenticated to use the API
    permission_classes = (IsAuthenticated,)

    # Filters queryset by current authenticated user
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by("-name")

    # Hooks into the create process when creating an object
    # Setting the user to the authenticated user
    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

    # Used to override the base serializer
    def get_serializer_class(self):
        """Return appropriate serializer class"""
        # If the action is `retrieve` for a detail request
        if self.action == "retrieve":
            return serializers.RecipeDetailSerializer
        # else use the var serializer_class
        return self.serializer_class
