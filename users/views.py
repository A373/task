from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import News_feed

# Create your views here.
@api_view(['POST'])
def sign_in(request):
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)
    confirm_password = request.POST.get('confirm_password', None)
    if user_name is None or password is None or confirm_password is None:
        content = {
            'message': 'user_name,password and confirm_password are mandatory'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif user_name is not None:
        new_user = User.objects.create_user(username=user_name, password=password)
        new_user.save()

        content = {
            'user_id': new_user.id,
            'user_name': new_user.username,
            'message': 'new_user has been created succesfully'
        }
        return Response(content, status=status.HTTP_200_OK)


@api_view(['POST'])
def log_in(request):
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)
    user = authenticate(username=user_name, password=password)
    if user is None:
        content = {
            'message': 'incorrect user_name or password'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        content = {
            'user_name': user.username,
            'message': 'log_in succesfully'
        }
        return Response(content, status=status.HTTP_200_OK)



@api_view(['POST'])
def news_feed(request):
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)
    user = authenticate(username=user_name, password=password)
    if user is None:
        content = {
            'message': 'invalid user_name or password'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif user is not None:
        news_feed = News_feed.objects.filter(user_id=user.id)
        feed = []
        for news_feed_ in news_feed:
            temp = {
                'feed_id': news_feed_.id,
                'news': news_feed_.news,
            }
            feed.append(temp)
        content = {
            'news_feed': feed
        }
        return Response(content, status=status.HTTP_200_OK)


@api_view(['POST'])
def support(request):
    user_name = request.POST.get('user_name', None)
    password = request.POST.get('password', None)
    user = authenticate(username=user_name, password=password)
    if user is None:
        content = {
            'message': 'Hii, you are not a user of our community--',
            'support_number': '108'
        }
        return Response(content, status=status.HTTP_200_OK)
    if user is not None:
        content = {
            'message': 'Welcome to our community--' + user.username,
            'support_number': '100'
        }
        return Response(content, status=status.HTTP_200_OK)