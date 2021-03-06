from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ReviewSerializer, CommentSerializer
from .models import Review, Comment

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request):
    # 보여지는 로직
    if request.method == 'GET':
        reviews = Review.objects.order_by('-pk')
        serializer = ReviewSerializer(reviews, many=True)
        # serializer = ReviewSerializer(request.user.reviews, many=True)
    else: # POST -> 글 작성 로직
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            # serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_page(request, page_pk):
    reviews = Review.objects.order_by('-pk')[(page_pk-1)*10:page_pk*10]
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])   
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated]) 
def review_update_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user == review.user:
    # 수정 요청
        if request.method == 'PUT':
            serializer = ReviewSerializer(instance= review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: # delete 요청
            review.delete()
            return Response({'id':pk,})
    else:
        return Response({'error':'접근이 불가합니다'})


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(review=review).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        # serializer = CommentSerializer(request.user.comment, many=True)
        return Response(serializer.data)
    # post의 경우
    else:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            comment.delete()
            return Response({'id': comment_pk})
    else:
        return Response({'error': '접근이 불가합니다'})