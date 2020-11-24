from rest_framework import serializers
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('review', 'user')


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y.%m.%d %H:%M", required=False, read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user')
        