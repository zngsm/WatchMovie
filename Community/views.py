from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ReviewSerializer
from .models import Review
# Create your views here.
@api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def review_list_create(request):
    # 보여지는 로직
    if request.method == 'GET':
        reviews = Review.objects.all()
        # serializer = ReviewSerializer(request.user.todos, many=True)
        serializer = ReviewSerializer(reviews, many=True)
    else: # POST -> 글 작성 로직
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(user=request.user)
            serializer.save()
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])   
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated]) 
def review_update_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    # 수정 요청
    if request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else: # delete 요청
        review.delete()
        return Response({'id':pk,})


# def like(request, pk):
#     review = get_object_or_404(Review, pk=pk)