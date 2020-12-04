from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        # The model we're basing the serializer from
        model = get_user_model()
        # Fields which will be converted to and from the db
        fields = ("email", "password", "name")
        # Extra variables for our password to make it write
        # only and have a min lengths
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        # Creates user using the validated data from the serializer
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        # The style in your django admin will likely now be password
        # e.g. obscured
        style={"input_type": "password"},
        # Doesn't allow spaces in password
        trim_whitespace=False
    )

    # Validate makes sure that the fields are good, and the user is valid
    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get("email")
        password = attrs.get("password")

        # Authenticate helper
        user = authenticate(
            # The context of the request
            request=self.context.get("request"),
            username=email,
            password=password
        )

        # If not authenticated, raise error. Msg is able to translated.
        if not user:
            msg = _("Unable to authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code="authentication")

        # Put user into the attributes
        attrs["user"] = user
        return attrs
