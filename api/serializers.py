from rest_framework import serializers

from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class VakansionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"

class ApplicattionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = "__all__"
