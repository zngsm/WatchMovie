from rest_framework import serializers
from .models import Nowplaying, Popular, Upcoming

class NowplayingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nowplaying
        fields = '__all__'


class PopularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Popular
        fields = '__all__'


class UpcomingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upcoming
        fields = '__all__'


