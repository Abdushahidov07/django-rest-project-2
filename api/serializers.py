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

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class MovieCastSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieCast
        fields = "__all__"


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
