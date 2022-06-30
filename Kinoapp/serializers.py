from rest_framework import serializers

from .models import *


class Aktyorserializers(serializers.ModelSerializer):
    class Meta:
        model = Aktyor
        fields = "__all__"

class Kinoserializers(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = "__all__"