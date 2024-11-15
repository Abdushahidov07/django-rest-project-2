from rest_framework import serializers

from .models import *


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class GenresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"

class ReviewerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = "__all__"
