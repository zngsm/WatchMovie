from rest_framework import serializers
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rank', 'created_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'review')
        read_only_fields = ('review',)